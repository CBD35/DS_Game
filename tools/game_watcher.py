#!/usr/bin/env python3
"""
Dark Sun: Shattered Lands — Live Playthrough Note Taker
========================================================
Captures your game screen and microphone commentary.
Sends periodic snapshots to Claude API (vision) for structured note-taking.
Notes are written to ../PLAYTHROUGH_NOTES/session_log.md in real time.

SETUP
-----
1.  pip install anthropic mss pillow sounddevice numpy faster-whisper pynput
2.  Set your API key:  export ANTHROPIC_API_KEY=sk-ant-...
3.  Run DOSBox with the game
4.  Run this script:   python game_watcher.py

CONTROLS (while running)
------------------------
  F9      — capture a note right now (manual trigger)
  F10     — quit and finalize session log

CONFIG (edit the CONFIG block below)
-------------------------------------
  CAPTURE_INTERVAL   seconds between automatic captures (default: 45)
  AUDIO_BUFFER_SEC   seconds of audio to send with each capture (default: 60)
  WINDOW_TITLE       partial title of the DOSBox window to focus-capture
                     (leave empty to capture the full primary screen)
  WHISPER_MODEL      faster-whisper model size: tiny/base/small/medium/large-v3
                     (tiny = fastest, least accurate; small = good balance)
  NOTE_FILE          path to write notes (relative to this script)
"""

import os
import sys
import time
import threading
import base64
import queue
import textwrap
from datetime import datetime
from pathlib import Path
from io import BytesIO

# ── CONFIG ───────────────────────────────────────────────────────────────────
CAPTURE_INTERVAL  = 45          # seconds between auto-captures
AUDIO_BUFFER_SEC  = 60          # seconds of voice audio to include per capture
WINDOW_TITLE      = "DOSBox"    # partial window title; empty = full screen
WHISPER_MODEL     = "small"     # tiny | base | small | medium | large-v3
NOTE_FILE         = "../PLAYTHROUGH_NOTES/session_log.md"
CLAUDE_MODEL      = "claude-sonnet-4-6"
# ─────────────────────────────────────────────────────────────────────────────

SCRIPT_DIR = Path(__file__).parent
NOTE_PATH  = (SCRIPT_DIR / NOTE_FILE).resolve()

# ── DEPENDENCY CHECKS ────────────────────────────────────────────────────────
def check_deps():
    missing = []
    for pkg, import_name in [
        ("anthropic",      "anthropic"),
        ("mss",            "mss"),
        ("pillow",         "PIL"),
        ("sounddevice",    "sounddevice"),
        ("numpy",          "numpy"),
        ("faster-whisper", "faster_whisper"),
        ("pynput",         "pynput"),
    ]:
        try:
            __import__(import_name)
        except ImportError:
            missing.append(pkg)
    if missing:
        print(f"\n[ERROR] Missing packages: {', '.join(missing)}")
        print(f"  Install with:  pip install {' '.join(missing)}\n")
        sys.exit(1)

check_deps()

import anthropic
import mss
import numpy as np
import sounddevice as sd
from PIL import Image
from faster_whisper import WhisperModel
from pynput import keyboard as kb

# ── GLOBALS ──────────────────────────────────────────────────────────────────
audio_chunks   = []          # rolling audio buffer
audio_lock     = threading.Lock()
stop_event     = threading.Event()
capture_now    = threading.Event()
note_counter   = 0
session_start  = datetime.now()

client         = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY", ""))
whisper        = None        # loaded lazily on first audio use

# ── AUDIO RECORDING ──────────────────────────────────────────────────────────
SAMPLE_RATE = 16000
CHANNELS    = 1

def audio_callback(indata, frames, time_info, status):
    with audio_lock:
        audio_chunks.append(indata.copy())

def get_audio_transcript() -> str:
    """Grab the last AUDIO_BUFFER_SEC of audio and transcribe it."""
    global whisper
    with audio_lock:
        if not audio_chunks:
            return ""
        chunks = list(audio_chunks)

    # Keep only the last AUDIO_BUFFER_SEC worth
    samples_needed = AUDIO_BUFFER_SEC * SAMPLE_RATE
    all_audio = np.concatenate(chunks, axis=0).flatten()
    if len(all_audio) > samples_needed:
        all_audio = all_audio[-samples_needed:]

    if np.max(np.abs(all_audio)) < 0.005:
        return ""  # silence — skip transcription

    if whisper is None:
        print(f"  [audio] Loading Whisper model ({WHISPER_MODEL})…")
        whisper = WhisperModel(WHISPER_MODEL, device="cpu", compute_type="int8")

    segments, _ = whisper.transcribe(all_audio, language="en", vad_filter=True)
    text = " ".join(s.text.strip() for s in segments).strip()
    return text

# ── SCREEN CAPTURE ───────────────────────────────────────────────────────────
def capture_screenshot() -> str:
    """Return a base64-encoded PNG of the game window (or full screen)."""
    with mss.mss() as sct:
        if WINDOW_TITLE:
            monitor = find_window_region(sct)
        else:
            monitor = sct.monitors[1]   # primary monitor

        raw = sct.grab(monitor)
        img = Image.frombytes("RGB", raw.size, raw.bgra, "raw", "BGRX")

        # Scale down if very large (saves API tokens)
        max_dim = 1280
        if img.width > max_dim or img.height > max_dim:
            img.thumbnail((max_dim, max_dim), Image.LANCZOS)

        buf = BytesIO()
        img.save(buf, format="PNG", optimize=True)
        return base64.standard_b64encode(buf.getvalue()).decode()

def find_window_region(sct):
    """
    Try to locate the DOSBox window on screen.
    Falls back to primary monitor if not found.
    Platform-specific helpers below.
    """
    try:
        if sys.platform == "win32":
            return _win_find_window(sct)
        elif sys.platform == "darwin":
            return _mac_find_window(sct)
        else:
            return _linux_find_window(sct)
    except Exception:
        return sct.monitors[1]

def _win_find_window(sct):
    import ctypes
    hwnd = ctypes.windll.user32.FindWindowW(None, None)
    # Walk windows looking for WINDOW_TITLE
    result = None
    def enum_cb(h, _):
        nonlocal result
        length = ctypes.windll.user32.GetWindowTextLengthW(h)
        buf = ctypes.create_unicode_buffer(length + 1)
        ctypes.windll.user32.GetWindowTextW(h, buf, length + 1)
        if WINDOW_TITLE.lower() in buf.value.lower():
            rect = ctypes.wintypes.RECT()
            ctypes.windll.user32.GetWindowRect(h, ctypes.byref(rect))
            result = {"top": rect.top, "left": rect.left,
                      "width": rect.right - rect.left,
                      "height": rect.bottom - rect.top}
            return False
        return True
    import ctypes.wintypes
    WNDENUMPROC = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)
    ctypes.windll.user32.EnumWindows(WNDENUMPROC(enum_cb), 0)
    return result or sct.monitors[1]

def _mac_find_window(sct):
    import subprocess, json
    out = subprocess.check_output([
        "osascript", "-e",
        f'tell application "System Events" to get {{position, size}} of '
        f'(first window of (first process whose name contains "{WINDOW_TITLE}"))'
    ]).decode().strip()
    # AppleScript returns comma-separated numbers
    nums = [int(x.strip()) for x in out.split(",")]
    x, y, w, h = nums[0], nums[1], nums[2], nums[3]
    return {"top": y, "left": x, "width": w, "height": h}

def _linux_find_window(sct):
    import subprocess
    out = subprocess.check_output(
        ["xdotool", "search", "--name", WINDOW_TITLE, "getwindowgeometry", "--shell"],
        stderr=subprocess.DEVNULL
    ).decode()
    props = {}
    for line in out.strip().split("\n"):
        if "=" in line:
            k, v = line.split("=", 1)
            props[k.strip()] = v.strip()
    return {
        "top":    int(props.get("Y", 0)),
        "left":   int(props.get("X", 0)),
        "width":  int(props.get("WIDTH",  sct.monitors[1]["width"])),
        "height": int(props.get("HEIGHT", sct.monitors[1]["height"])),
    }

# ── CLAUDE NOTE-TAKING ────────────────────────────────────────────────────────
SYSTEM_PROMPT = textwrap.dedent("""
    You are a game archivist taking structured notes on a playthrough of
    Dark Sun: Shattered Lands (SSI, 1993), a turn-based RPG set in the
    city-state of DRAJ on the dying world of Athas.

    You receive:
    1. A screenshot from the game
    2. A transcription of the player's voice commentary (may be empty)

    Your job: extract and structure everything observable.
    Be concise. Use bullet points. Only note what you can actually see or
    what the player says — do not invent or assume.
    Flag anything that looks unfinished, abrupt, or narratively incomplete.
""").strip()

NOTE_PROMPT_TEMPLATE = textwrap.dedent("""
    PLAYER VOICE COMMENTARY (last ~{buf}s):
    {transcript}

    ---
    Extract structured notes from this game capture. Format your response as:

    **LOCATION:** (name of area if visible, or "unknown")
    **WHAT'S ON SCREEN:** (brief description of what the screenshot shows)
    **NPCS / DIALOGUE:** (any NPC names or dialogue text visible)
    **ITEMS:** (any items, inventory, or loot visible)
    **PLAYER SAID:** (summary of voice commentary, or "—" if none)
    **STORY / QUEST:** (any story beat, quest step, or choice visible)
    **ATMOSPHERE:** (visual tone, music mentioned, anything about the feel)
    **UNFINISHED / CUT?** (anything that seems incomplete or abruptly ended — or "nothing notable")
""").strip()

def send_to_claude(screenshot_b64: str, transcript: str) -> str:
    """Send screenshot + transcript to Claude, return formatted note."""
    prompt = NOTE_PROMPT_TEMPLATE.format(
        buf=AUDIO_BUFFER_SEC,
        transcript=transcript if transcript else "(no voice detected)",
    )
    try:
        resp = client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=1024,
            system=SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": [
                    {
                        "type":       "image",
                        "source":     {
                            "type":       "base64",
                            "media_type": "image/png",
                            "data":       screenshot_b64,
                        },
                    },
                    {"type": "text", "text": prompt},
                ],
            }],
        )
        return resp.content[0].text.strip()
    except Exception as e:
        return f"[API error: {e}]"

# ── NOTE WRITING ─────────────────────────────────────────────────────────────
def write_note(note_text: str, trigger: str = "auto"):
    global note_counter
    note_counter += 1
    ts = datetime.now().strftime("%H:%M:%S")
    elapsed = int((datetime.now() - session_start).total_seconds() // 60)

    header = (
        f"\n\n---\n"
        f"## Note #{note_counter}  [{ts}]  +{elapsed}min  ({trigger})\n\n"
    )
    entry = header + note_text + "\n"

    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(NOTE_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"\n  ✓ Note #{note_counter} written → {NOTE_PATH.name}")
    # Print a short preview
    preview = note_text[:200].replace("\n", " ")
    print(f"    {preview}…\n")

# ── KEYBOARD LISTENER ─────────────────────────────────────────────────────────
def on_press(key):
    try:
        if key == kb.Key.f9:
            print("\n  [F9] Manual capture triggered…")
            capture_now.set()
        elif key == kb.Key.f10:
            print("\n  [F10] Stopping…")
            stop_event.set()
            return False   # stops listener
    except Exception:
        pass

# ── CAPTURE LOOP ─────────────────────────────────────────────────────────────
def capture_and_note(trigger: str = "auto"):
    print(f"  [{trigger}] Capturing screenshot…", end=" ", flush=True)
    try:
        screenshot = capture_screenshot()
        print("ok. Transcribing audio…", end=" ", flush=True)
        transcript = get_audio_transcript()
        status = f"({len(transcript.split())} words)" if transcript else "(silent)"
        print(f"{status}. Sending to Claude…", end=" ", flush=True)
        note = send_to_claude(screenshot, transcript)
        write_note(note, trigger=trigger)
    except Exception as e:
        print(f"\n  [capture error] {e}")

def main_loop():
    last_auto = time.time()
    while not stop_event.is_set():
        # Manual trigger
        if capture_now.is_set():
            capture_now.clear()
            capture_and_note(trigger="manual/F9")

        # Auto trigger
        if time.time() - last_auto >= CAPTURE_INTERVAL:
            capture_and_note(trigger="auto")
            last_auto = time.time()

        time.sleep(1)

# ── MAIN ─────────────────────────────────────────────────────────────────────
def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or api_key == "sk-ant-...":
        print("\n[ERROR] Set your API key first:")
        print("  export ANTHROPIC_API_KEY=sk-ant-YOUR_KEY_HERE\n")
        sys.exit(1)

    # Session log header
    NOTE_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(NOTE_PATH, "a", encoding="utf-8") as f:
        f.write(
            f"\n\n# Session — {session_start.strftime('%Y-%m-%d %H:%M')}\n"
            f"*Auto-generated by game_watcher.py*\n"
            f"*Interval: {CAPTURE_INTERVAL}s | Audio buffer: {AUDIO_BUFFER_SEC}s | Whisper: {WHISPER_MODEL}*\n"
        )

    print("\n" + "═" * 60)
    print("  Dark Sun: Shattered Lands — Live Note Taker")
    print("═" * 60)
    print(f"  Notes → {NOTE_PATH}")
    print(f"  Auto-capture every {CAPTURE_INTERVAL}s")
    print(f"  F9  = capture now   |   F10 = quit")
    print("═" * 60)
    print("  Starting audio recording…", end=" ", flush=True)

    # Start audio stream
    stream = sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=CHANNELS,
        dtype="float32",
        callback=audio_callback,
        blocksize=int(SAMPLE_RATE * 0.5),   # 0.5s chunks
    )
    stream.start()
    print("ok.")
    print("  Keyboard listener active. Switch to your game now.\n")

    # Start keyboard listener (non-blocking)
    listener = kb.Listener(on_press=on_press)
    listener.start()

    try:
        main_loop()
    except KeyboardInterrupt:
        pass
    finally:
        stream.stop()
        stream.close()
        listener.stop()
        elapsed = int((datetime.now() - session_start).total_seconds() // 60)
        print(f"\n  Session ended. {note_counter} notes written in {elapsed} minutes.")
        print(f"  Log → {NOTE_PATH}\n")

if __name__ == "__main__":
    main()
