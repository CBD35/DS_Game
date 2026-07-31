# Dark Sun: Shattered Lands — Remake GDD
## 10: UI/UX Design

**Version:** 0.2
**Last Updated:** 2026-04-20


> ⚠️ **DRAFT — Pending rewrite.** This file contains errors (game is set in **Draj under Tectuktitlay**, not Urik/Hamanu). Content not verified against source PDFs. See `GDD/MASTER_PROJECT_FILE.md` for the authoritative reference.
---

## Table of Contents
1. [Design Philosophy](#design-philosophy)
2. [Visual Language](#visual-language)
3. [Main HUD](#main-hud)
4. [Combat Interface](#combat-interface)
5. [Inventory System](#inventory-system)
6. [The Journal and Codex](#the-journal-and-codex)
7. [World Map](#world-map)
8. [Dialogue System](#dialogue-system)
9. [Accessibility](#accessibility)
10. [Controller and Steam Deck Support](#controller-and-steam-deck-support)

---

## Design Philosophy

The original Shattered Lands was keyboard-driven with a small icon-based interface. It was functional for 1993 and opaque by modern standards. The remake's UI must be:

1. **Immediately readable** — a new player should understand what's happening in combat within 2 minutes without reading a manual
2. **Informationally complete** — a veteran player should never need to mouse over something 3 times to find a number they need
3. **Aesthetically Athasian** — every UI element should feel like it was made from bone, hide, obsidian, and ceramic. No metal. No chrome. No fantasy-generic blue glow.
4. **Non-intrusive** — the world is the focus; the UI serves it

---

## Visual Language

### Materials and Texture
All UI panels are made from the materials of Athas:
- **Bone:** Panel borders, button frames, scroll dividers
- **Stretched hide:** Background fills, tooltip backgrounds (slightly translucent)
- **Obsidian:** Accent elements, selected-state indicators (high-contrast black glass)
- **Ceramic:** Rounded containers (water units display as ceramic jugs)
- **Sand:** Texture on inactive/disabled elements

### Color Palette
| Purpose | Color | Notes |
|---|---|---|
| Primary text | Off-white (bone) | Never pure white — too harsh |
| Highlight / selected | Deep amber | Warm; readable |
| Danger / critical | Ochre-red | Sun-bleached blood; not bright red |
| Safe / positive | Dusty sage green | Scarce on Athas; stands out |
| Disabled | Ashen grey | Defiled earth |
| Enemy elements | Muted rust | |
| Ally elements | Muted gold | |

### Typography
- **Headings:** A hand-inscribed serif; scratched-stone aesthetic
- **Body / tooltip text:** Clean, readable sans-serif; legible at small sizes
- **No in-world text is typed — everything appears hand-written** (within the fiction; rendered as font)

---

## Main HUD

The HUD during exploration and combat is minimal. Everything is visible without opening menus.

### Party Panel (Bottom Left)
Four character portraits in a vertical strip. Each portrait shows:
- Character name
- HP bar (bone-colored track; fills with red as HP drops)
- Condition icons (up to 4 visible; more overflow to a tooltip)
- Water icon (small ceramic jug, fill level shows WU remaining)
- Psionic indicator (glowing amber eye if active psionic effect; blank if none)

Clicking a portrait opens that character's full status screen.

### Selected Character Info (Bottom Center)
When a character is selected (in combat or exploration):
- Name, class, level
- Current HP / Max HP
- AC
- Current conditions (text list)
- Active buffs / debuffs with remaining durations

### Action Bar (Bottom, Center-Right)
In combat: the selected character's available actions for this turn.
- Standard Action slot (left): Attack options, spell/power use, item use
- Move Action slot (center): Move, special movement, interact
- Reaction indicator (right): Shows if Reaction has been used this round
- Full Attack toggle: Clicking "Full Attack" merges both slots into an all-attacks action

In exploration: streamlined — just inventory access, map, and journal shortcuts.

### Resource Indicators (Top Right)
- **Party Water:** Total WU remaining across all party members (large ceramic jug icon; fill level)
- **Party Food:** Total FU remaining (bone-shaped container; fill level)
- **Time of Day:** Sun position arc across the top of the screen (ambient indicator; also shows heat stage via color)
- **World Defilement Counter:** A small crack in the earth icon; deeper crack = higher defilement. Subtle but always visible.

### Mini-Map (Top Right corner)
Toggle on/off. Shows explored area, party position, and marked locations. No enemy positions unless actively scouted.

---

## Combat Interface

### Initiative Order (Top Center)
A horizontal track showing all combatants in initiative order. Each has a small portrait or creature icon. The active combatant is highlighted. Hovering over any icon shows that creature's visible stats (HP, conditions, next expected action if knowable).

### Combat Log (Right Side Panel — toggleable)
Scrolling text log of all combat events. Clear, concise language:
- "Rikus attacks Sand Raider (2) for 14 damage [Bone Spear]"
- "Sand Raider (2) is Bloodied (below 50% HP)"
- "Neeva uses Full Attack — 3 attacks, 2 hit (total 22 damage)"

### Targeting
- Hovering over an enemy shows: HP bar, AC, visible conditions, name
- Hovering over an attack option shows: expected damage range, hit probability (as text: "likely to hit", "difficult", "unlikely" — not a percentage, to preserve tension)
- Right-click on an enemy shows full stat block for that creature type (if the party has fought one before; otherwise shows "Unknown")

### Psionic Combat Overlay
When psionic combat initiates, a translucent secondary panel slides in from the right showing:
- The Psionicist's PP pool
- Available mental attack modes (grayed if insufficient PP)
- The target's visible mental state (PP estimate, known defenses if any)
- Previous round's psionic exchange log

This overlay does not pause physical combat. Both tracks continue simultaneously.

### Area of Effect Preview
Before confirming a spell or area attack, the AoE is previewed on the map as a semi-transparent template. Allied characters within the AoE are highlighted in amber (warning, not locked). Player must confirm or cancel.

### End Turn
Prominent button (or keyboard shortcut). Shows which characters have remaining actions (amber indicator). A turn is not automatically ended — the player must confirm.

---

## Inventory System

### Philosophy
Inventory is encumbrance-based, not slot-based. Carrying capacity is tracked in pounds per character. Every item has a weight.

### Inventory Screen Layout
- Left: Character portrait + encumbrance bar (Light/Medium/Heavy/Overloaded)
- Center: Grid of items (icon + name + weight)
- Right: Selected item details (description, stats, fragility, special notes)
- Bottom: Equipped slots — head, body, hands, feet, weapon (main), weapon (off), shield

### Equipment Slots
| Slot | Types Accepted |
|---|---|
| Head | Helmet (chitin, bone, hardened leather) |
| Body | Armor (hide, chitin, bone-plate, no metal) |
| Hands | Gloves (hide, chitin) |
| Feet | Sandals or boots (hide, bone sole) |
| Weapon (main) | Any single-hand or two-hand weapon |
| Weapon (off-hand) | One-hand weapon, shield, or empty |
| Shield | Hide shields, bone-rimmed, large chitin |

Thri-Kreen have four weapon slots (primary L/R, secondary L/R) and no shield slot.
Half-Giants cannot use standard-size equipment — their gear is marked Large and costs 3× standard.

### Party Inventory / Shared Storage
A shared party inventory is accessible from any character's inventory screen. Items can be transferred between characters. Kanks (if owned) appear as additional inventory containers with their own capacity.

### Item Fragility Display
Weapons with Fragility Ratings show a small crack indicator on their icon:
- No crack: Full durability
- One crack: Hairline (icon shows a thin crack)
- Two cracks (destroyed): Shattered icon; item grayed out

---

## The Journal and Codex

### Journal
Tracks active and completed quests. Each entry shows:
- Quest name and giver
- Current objective (concise, specific)
- Known related NPCs
- Player-writable notes field (optional free-text notes the player can add)
- Map markers (quest locations highlighted on world map)

Quests are categorized: Main Story / Faction / Personal (companion) / Side / Exploration

### Codex
A growing reference document populated as the party discovers information:
- **Bestiary:** Enemy entries unlock after first combat with each creature type; show stats and tactics
- **Locations:** Brief description of each discovered area
- **Factions:** Updated as faction relationships develop; shows current reputation and available rewards
- **Characters:** NPC profiles; updated as dialogue reveals more
- **Lore:** Fragments of Athasian history found through exploration, dialogue, and the Thief's Read Languages skill
- **Items:** Entries for notable items found; special items include in-world descriptions

The Codex is never required to play. It is for players who want to understand the world more deeply.

---

## World Map

### Overview
The world map is a node-based travel interface. Locations appear as points connected by routes. Unexplored routes are shown as dashed lines with distance indicators.

### Map Layers (toggleable)
- **Standard:** Locations, routes, party position
- **Defilement Overlay:** Color wash showing defilement levels per region (green → grey)
- **Faction Territory:** Color wash showing city-state claimed territory and disputed zones
- **Water Sources:** Highlights known water sources (oases, wells, city purchase points)

### Travel Interface
Clicking a connected node shows:
- Estimated travel time
- Estimated resource cost (WU, FU)
- Known hazards (if the party has scouted or been informed)
- Random encounter rate (shown as threat icons: 1–4 skulls)
- Confirm / Cancel

---

## Dialogue System

### Layout
Dialogue uses a portrait system:
- Left: Speaking NPC (large portrait, name, title)
- Right: Player character responding (smaller portrait)
- Bottom: NPC dialogue text
- Center bottom: Response options (up to 5; additional options in a scroll if needed)

### Response Labeling
Each response option shows:
- The response text (what the character will say/do)
- A small tag indicating type: [Persuade], [Intimidate], [Lie], [Ask About X], [Psionic], [Leave]
- Skill check options show their DC: [Persuade — DC 14]
- Race-specific options shown only if relevant: [As a Mul...]
- Class-specific options shown only if relevant: [As a Psionicist, you sense...]

### No "Good/Evil" Tagging
Responses are never tagged as "good" or "evil." The consequences are in the game world, not in the UI.

### Companion Reactions
During significant dialogue moments, companion portraits briefly animate (expression change) to show their reaction. This is subtle — no floating text, no approval/disapproval popup. Players who are paying attention notice it; players who aren't don't.

---

## Accessibility

### Visual
- Colorblind mode: All color-coded indicators have a secondary shape/pattern indicator
- Text size: Small / Normal / Large
- UI scale: 80% – 150%
- High contrast mode: Increases UI element borders and text contrast

### Input
- Full mouse support (primary)
- Full keyboard shortcut support (remappable)
- Controller support (see below)
- Pause-at-any-time in combat (no real-time elements)

### Difficulty and Assistance
- **Survival Mode toggle:** Turn off survival mechanics (water/food/heat) for players who want the story and combat without resource management
- **Combat Tutorial:** Extended tutorials available for all major system introductions
- **Persistent tooltips:** Can be set to always-on (vs hover-only)
- **Slow Mode:** All combat animations can be set to 0.5× speed for readability

---

## Controller and Steam Deck Support

### Controller Layout (Default)
| Button | Context: Exploration | Context: Combat |
|---|---|---|
| Left stick | Move party | Cursor movement |
| Right stick | Camera pan | Camera pan |
| A / Cross | Interact | Confirm / Select action |
| B / Circle | Cancel / Back | Cancel / Deselect |
| X / Square | Open Inventory | Full Attack toggle |
| Y / Triangle | Open Journal | End Turn |
| LB | Previous party member | Previous combatant (initiative) |
| RB | Next party member | Next combatant (initiative) |
| LT | Hold: Sprint | Hold: AoE preview |
| RT | Hold: Cursor mode | Hold: Aim mode (ranged) |
| D-pad | Shortcuts (Journal/Map/Codex/Camp) | Quick-select actions |
| Start | Menu | Menu / Pause |

### Steam Deck Specifics
- Target: 1280×800; all UI elements tested at this resolution minimum
- Font size minimum 14pt at 1280×800
- Touch screen support for map interaction and inventory dragging
- Gyro aiming: optional for ranged attacks in combat

### Input Notification
The UI automatically detects input method and switches between mouse-cursor UI and controller-optimized UI (larger hit targets, different selection model). Switching is seamless and instant.
