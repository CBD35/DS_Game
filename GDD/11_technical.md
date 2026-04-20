# Dark Sun: Shattered Lands — Remake GDD
## 11: Technical Design

**Version:** 0.2
**Last Updated:** 2026-04-20

---

## Table of Contents
1. [Engine and Technology Stack](#engine-and-technology-stack)
2. [Isometric Rendering](#isometric-rendering)
3. [Map and Level Architecture](#map-and-level-architecture)
4. [Save System](#save-system)
5. [World State Management](#world-state-management)
6. [Combat System Architecture](#combat-system-architecture)
7. [Audio System](#audio-system)
8. [Performance Targets](#performance-targets)
9. [Modding Support](#modding-support)
10. [Platform-Specific Requirements](#platform-specific-requirements)

---

## Engine and Technology Stack

### Engine: Godot 4.x
**Rationale:**
- Open-source; no per-seat licensing costs for a small team
- Native isometric support via tile maps and camera configuration
- GDScript (Python-like) and C# both supported; team can use either
- Strong 2D rendering pipeline appropriate for hand-painted texture assets
- Built-in scene/resource system suits the game's modular level design
- Active community; plugin ecosystem for turn-based game patterns
- Export to Windows, Linux, macOS, Web, Android, iOS from a single project
- Steam Deck runs Linux (SteamOS); Godot's Linux export is first-class

### Language: GDScript (primary) + C# (performance-critical systems)
- GDScript for: game logic, dialogue, UI, quest systems, AI
- C# for: pathfinding, combat resolution math, world state queries
- Reason: GDScript is faster to iterate; C# handles hot paths

### Source Control: Git
- Git LFS for binary assets (art, audio)
- Branch model: main (stable), develop (integration), feature/* (per-feature)

### Asset Pipeline
- Sprites: exported from Aseprite (pixel art) or Photoshop/Krita (hand-painted)
- Tilemaps: Tiled editor → Godot import pipeline
- Audio: FMOD Studio for adaptive music and environmental audio layering
- Localization: GNU gettext `.po` files; Godot's built-in translation system

---

## Isometric Rendering

### Camera and Projection
- **Isometric projection:** 2:1 pixel ratio (standard isometric); 60-degree angle
- **Tile size:** 64×32 pixels (base ground tile)
- **Sprite height:** Characters are 64–128 px tall depending on race (Half-Giants are 256 px)
- **Sorting:** Y-sort enabled globally; objects sort by their base position's Y coordinate to handle depth correctly

### Tile Layers
Each map is built from multiple layers:
1. **Ground** — base terrain tiles
2. **Decals** — sand ripples, ash marks, bloodstains; non-interactive
3. **Object Base** — furniture, rocks, trees; blocks movement if flagged
4. **Characters** — party and NPCs; Y-sorted
5. **Object Top** — overhanging elements (cave ceilings, awnings); renders above characters in certain tiles
6. **Weather/FX** — particle systems (sand, heat shimmer, psionic effects)
7. **UI Overlay** — combat indicators, selection rings, path previews; always on top

### Defilement Visual System
When a Defiler casts, the Ash Ring effect is:
1. A particle burst expanding outward from the caster
2. A permanent tile modification — ground tiles in the ring switch to a Defiled variant
3. Defiled tile variants: grey-brown, cracked, no plant sprites
4. This is stored per-tile in the map's defilement layer; persistent across sessions

### Lighting
Athas's red sun creates specific lighting conditions:
- Ambient color: warm orange-red with a slightly higher gamma than neutral
- Shadow direction shifts with time of day (sun position arc)
- Torchlight: warm yellow-orange point lights; dynamic shadow casting
- Psionic effects: brief white-blue desaturated flashes (contrast with warm ambient)
- Underground areas: deep shadow with point lights only; no ambient fill

---

## Map and Level Architecture

### Map Types
| Type | Purpose | Streaming? |
|---|---|---|
| City district | Large explorable areas; NPCs, shops, quests | Yes — district-by-district |
| Dungeon | Linear or branching combat environments | No — fully loaded |
| Wilderness encounter | Random encounter maps; ~20×20 tiles | No — small |
| Arena | Specialized combat maps with crowd simulation | No |
| World map | Node-based travel interface; not a 3D space | N/A |

### Tile-Based Navigation
Movement uses A* pathfinding on a tile grid. Each tile has:
- **Passable flag:** Can characters move through this tile?
- **Difficult terrain flag:** Costs 2 movement to enter
- **Elevation level:** 0–3 (flat, raised, high, ceiling); affects line of sight and ranged attacks
- **Cover flag:** Provides half or three-quarters cover to occupants
- **Defilement level:** 0–5; affects plant sprites and local survival checks
- **Hazard type:** None, fire, acid, electrical, psionic anomaly

### Line of Sight
LOS is calculated tile-by-tile using Bresenham's line algorithm. Tiles with solid objects block LOS. Partial cover tiles reduce attack rolls but do not block LOS.

### Encounter Streaming
City districts are loaded in segments — the player's current district plus adjacent districts are held in memory; distant districts are unloaded. Transition between segments is seamless (no loading screen within a city).

---

## Save System

### Save Structure
The game uses a **continuous autosave** model with **manual quicksave** slots.

| Save Type | Count | When |
|---|---|---|
| Autosave | 3 (rotating) | On entering any new area; on leaving a dialogue; on completing a quest |
| Manual Quicksave | 10 slots | Player-initiated; any time outside combat |
| Checkpoint Save | Automatic | Before any irreversible narrative event (flagged in design) |
| New Game+ Save | Separate slot | Created at game completion |

### Save File Contents
Each save file stores:
- Party state: all characters, levels, HP, inventory, equipped items
- World state (see below)
- Faction reputation values
- Quest journal state (active, completed, failed)
- Map states: visited areas, modified tiles (defilement, opened locks, destroyed objects)
- Companion loyalty values
- Codex entries unlocked
- Timestamp and play duration

### Save Compression
Save files use zstd compression. Target size: < 5 MB per save file.

---

## World State Management

### The World State Object
A global singleton tracks all persistent world changes. This object is:
- Queried by: NPC dialogue systems, quest triggers, encounter scripts, UI systems
- Modified by: combat outcomes, dialogue choices, quest completions, defilement events
- Saved with every save file

### Key World State Flags (Examples)
```
arena_escaped: bool
kalak_ritual_anchor_1_destroyed: bool
kalak_ritual_anchor_2_destroyed: bool
kalak_ritual_anchor_3_destroyed: bool
desh_arak_alliance_cell_found: bool
sadira_defiler_path: bool
world_defilement_counter: float  # 0.0 - 100.0
tyr_templar_faction_active: bool
rikus_family_found: bool
morthek_status: enum [alive, dying, dead, revealed]
player_freed_arena_slaves: bool
gulg_oba_met: bool
```

### Reactive NPC System
NPCs query the World State before generating dialogue. Every named NPC has a dialogue tree with conditional branches based on World State flags. This ensures that freeing slaves in Act 1 is remembered by a slave NPC in Act 3.

Implementation: Dialogue files reference World State flags directly. The dialogue compiler validates that all referenced flags exist at build time.

---

## Combat System Architecture

### Turn Manager
A singleton `CombatManager` handles all combat:
- Initializes initiative order at combat start
- Tracks whose turn it is
- Routes action requests to the appropriate resolution system
- Handles end-of-combat cleanup (XP award, loot generation, defilement application)

### Action Resolution Pipeline
1. Player or AI submits an Action object (type, source, target, modifiers)
2. `ActionValidator` checks if the action is legal (has PP, is in range, target is valid)
3. `AttackResolver` or `SpellResolver` or `PsionicResolver` calculates result
4. `EffectApplicator` applies damage, conditions, and world changes
5. `CombatLog` receives an event describing what happened
6. UI systems receive update signals

### AI Behavior
Enemy AI uses a priority-weighted decision tree:
1. If critically wounded (< 25% HP) and morale rating ≤ 6: evaluate flee
2. If a high-value target (Psionicist, wounded character) is in range: attack it
3. If a better position provides flanking or elevation: move first, then attack
4. Default: attack the nearest enemy

Templars have higher morale and smarter target selection. Named boss enemies have scripted behavior phases.

### Psionic Combat Integration
`PsionicCombatOverlay` is a parallel state machine that:
- Runs on the same initiative timeline as physical combat
- Is activated when any psionicist declares a psionic attack
- Tracks PP for all combatants with psionic ability
- Resolves independently of the physical combat pipeline
- Reports results to the main `CombatLog`

---

## Audio System

### FMOD Studio Integration
The game uses FMOD Studio for adaptive audio:
- Music: layered stems that add/remove based on context (exploration → tension → combat → resolution)
- Environmental audio: ambient loops with randomized one-shot events
- Combat sounds: per-weapon, per-hit-type, per-creature audio banks

### Music System
Three music states with smooth transitions:
- **Exploration:** Low-intensity; percussion-forward; regional variants (city / wastes / dungeon / arena)
- **Tension:** When enemies are nearby but not engaged; partial combat stems added
- **Combat:** Full intensity; tempo tied loosely to initiative speed; boss encounters have unique themes

The Defiler casting theme — a deep resonant scrape of bone on stone, overlaid with the sound of things dying — plays on every defilement event.

### Athasian Instrument Palette
No orchestral strings. No brass horns. Instruments used:
- Frame drums (doumbek, riq)
- Long-neck lutes (saz, oud — desert-adjacent)
- Reed flutes (ney)
- Bowed strings (kemençe)
- Prepared percussion (bone, shell, stone percussion)
- Vocal: wordless, distant, dry-throat style

---

## Performance Targets

| Platform | Target FPS | Resolution | Settings |
|---|---|---|---|
| PC (recommended) | 60 | 1920×1080 | High |
| PC (minimum) | 30 | 1280×720 | Low |
| Steam Deck | 60 | 1280×800 | Medium |
| Console (PS5/Xbox) | 60 | 3840×2160 (4K) | High (post-launch) |

### Optimization Strategy
- Tile maps are chunked; only visible chunks are processed
- NPC pathfinding is throttled to once per 2 frames for off-screen NPCs
- Particle effects (defilement ash rings) use GPU instancing
- Audio occlusion handled by FMOD's built-in geometry system
- Save file operations run on a background thread; no gameplay stutter on autosave

---

## Modding Support

### Scope
The remake ships with a modding-friendly structure but no dedicated modding SDK at launch. Post-launch, the project structure is released to allow community mods.

### What Modders Can Modify (at Launch)
- Dialogue files (plain text JSON with branching logic)
- Item databases (JSON)
- Spell/power lists (JSON)
- Tilemap tilesets (standard PNG format)
- Music (FMOD project is not included, but audio banks can be replaced)

### Post-Launch Modding SDK (Planned)
- Full Godot 4 project structure released
- Documentation for World State flag system
- Encounter scripting API
- Custom quest framework with visual node editor

---

## Platform-Specific Requirements

### Windows
- DirectX 12 / Vulkan renderer
- Minimum: Windows 10, 8GB RAM, GTX 1060 or equivalent
- Recommended: Windows 11, 16GB RAM, RTX 2070 or equivalent
- Steam integration: achievements, cloud saves, Workshop (post-launch)

### Linux
- Vulkan renderer
- Native build; not a Proton port
- Steam Deck is a first-class Linux target

### macOS
- Metal renderer
- Universal binary (Apple Silicon + Intel)
- Minimum macOS 12 (Monterey)

### Steam Deck Specifics
- Verified target (not just compatible)
- All UI elements readable at 1280×800
- Default settings profile auto-applied on Deck detection
- Battery: target 3+ hours at medium settings; benchmark-tested

### Save File Location
- Windows: `%APPDATA%\DarkSunRemake\saves\`
- Linux/Deck: `~/.local/share/DarkSunRemake/saves/`
- macOS: `~/Library/Application Support/DarkSunRemake/saves/`
- Cloud saves sync automatically via Steam Cloud on all platforms
