# Tools — Dark Sun: Shattered Lands Reborn

## game_watcher.py — Live Playthrough Note Taker

Watches your DOSBox window and listens to your voice commentary in real time.
Sends periodic snapshots to Claude API (with vision) which writes structured notes
directly to `PLAYTHROUGH_NOTES/session_log.md`.

### What It Does

Every 45 seconds (configurable), it:
1. Captures a screenshot of your DOSBox window
2. Grabs the last 60 seconds of your voice (transcribed locally with Whisper)
3. Sends both to Claude API
4. Claude extracts: location, NPCs, dialogue, items, story beats, atmosphere, anything that looks cut/unfinished
5. Appends a structured note to `PLAYTHROUGH_NOTES/session_log.md`

You can also press **F9** at any time to trigger an immediate capture.

---

### Setup

#### 1. Python
Python 3.9+ required. Check with `python --version`.

#### 2. Install dependencies

```bash
cd tools
pip install -r requirements.txt
```

**Windows note:** If `sounddevice` fails, install PortAudio first:
```
pip install pipwin
pipwin install pyaudio
```
Then try `pip install sounddevice` again.

**Linux note:** You may need:
```bash
sudo apt install portaudio19-dev python3-dev
sudo apt install xdotool   # for window detection
```

**Mac note:** You may need:
```bash
brew install portaudio
```

#### 3. Set your Anthropic API key

**Windows (PowerShell):**
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-YOUR_KEY_HERE"
```

**Mac/Linux:**
```bash
export ANTHROPIC_API_KEY=sk-ant-YOUR_KEY_HERE
```

Get your key at: https://console.anthropic.com/

#### 4. (Optional) Faster Whisper model

The first time you run with audio, it downloads the Whisper model (~250MB for `small`).
You can change the model size in the CONFIG section of the script:
- `tiny` — fastest, lower accuracy
- `small` — good balance (recommended)
- `medium` — more accurate, slower
- `large-v3` — best accuracy, slow on CPU

---

### Running

1. Start DOSBox and load the game
2. Open a terminal in the `tools/` directory
3. Run:

```bash
python game_watcher.py
```

4. Switch back to your game — the watcher runs in the background
5. Talk about what you see — the mic is always recording (nothing is sent until a capture fires)
6. **F9** = take a note right now
7. **F10** = quit

---

### Configuration

Edit the `CONFIG` block at the top of `game_watcher.py`:

```python
CAPTURE_INTERVAL  = 45       # seconds between auto-captures
AUDIO_BUFFER_SEC  = 60       # seconds of voice audio per capture
WINDOW_TITLE      = "DOSBox" # partial window title to capture
WHISPER_MODEL     = "small"  # tiny | base | small | medium | large-v3
NOTE_FILE         = "../PLAYTHROUGH_NOTES/session_log.md"
```

If `WINDOW_TITLE` doesn't match your DOSBox window, either:
- Change it to match (check your window's title bar)
- Set it to `""` to capture the full primary screen

---

### Output

Notes go to `PLAYTHROUGH_NOTES/session_log.md`. Each note looks like:

```markdown
## Note #3  [14:22:07]  +12min  (auto)

**LOCATION:** Slave Pens — Northwest corridor
**WHAT'S ON SCREEN:** Party in a corridor, Trustee NPC visible, health bars shown
**NPCS / DIALOGUE:** Trustee: "Dinos in the kitchen can heal your friend."
**ITEMS:** Water pot visible at location 6
**PLAYER SAID:** "This Trustee guy seems to know where everything is..."
**STORY / QUEST:** Pointing toward Dinos to heal Gilal
**ATMOSPHERE:** Brown brick walls, torchlit, oppressive
**UNFINISHED / CUT?** nothing notable
```

After your session, you (or Claude) can organize the log into the structured
`02_characters.md`, `03_locations.md`, etc. files.

---

### Cost

Each capture sends one screenshot (~50–150KB) plus a text prompt to Claude API.
At claude-sonnet-4-6 pricing, a 2-hour session with 45-second intervals ≈ 160 captures.
Estimated cost: ~$1–3 depending on screenshot content.

---

### Troubleshooting

**"Missing packages" error:** Run `pip install -r requirements.txt`

**No audio transcription:** Check your default microphone in system settings.
Test with: `python -c "import sounddevice; print(sounddevice.query_devices())"`

**Wrong window captured:** Set `WINDOW_TITLE = ""` to capture full screen instead.

**F9/F10 not working:** The script needs focus on the terminal occasionally.
On some systems, global hotkeys require accessibility permissions (Mac) or
running as administrator (Windows).
