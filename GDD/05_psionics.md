# Dark Sun: Shattered Lands — Remake GDD
## 05: Psionics

**Version:** 0.2
**Last Updated:** 2026-04-20


> ⚠️ **DRAFT — Pending rewrite.** This file contains errors (game is set in **Draj under Tectuktitlay**, not Urik/Hamanu). Content not verified against source PDFs. See `GDD/MASTER_PROJECT_FILE.md` for the authoritative reference.
---

## Table of Contents
1. [Overview](#overview)
2. [Wild Talents](#wild-talents)
3. [Psionic Disciplines](#psionic-disciplines)
4. [Power Point Economy](#power-point-economy)
5. [Psionic Combat](#psionic-combat)
6. [Powers by Discipline](#powers-by-discipline)
7. [Psionics and the World](#psionics-and-the-world)

---

## Overview

On Athas, psionics are not rare. Every living being has the potential for psionic ability. Most manifest only a single **wild talent** — a raw, untrained psionic power that emerged naturally. Psionicists are the professionals: trained, disciplined, and operating at a level of psionic mastery that wild talents cannot approach.

The psionic system runs in **parallel to physical and magical systems** — it is not a subset of either. A Psionicist can operate in combat rounds alongside fighters and wizards, but psionic combat is a separate overlay that only psionicists and creatures with psionic ability engage in.

### Psionics vs Magic
- Magic draws from the world's life force. Psionics draws from the individual's mind.
- Psionics cannot be suppressed by anti-magic effects. Magic cannot be suppressed by psionic dampening (except in Var-Khet's suppression grid — a specific plot device).
- Defiler magic leaves physical marks. Psionic combat leaves mental marks (trauma, confusion, permanent psychological scars in extreme cases).
- The two systems do not interact unless a specific power or spell explicitly creates interaction.

---

## Wild Talents

### Acquisition
All non-Psionicist characters have a racial chance of manifesting one wild talent (see 02_races.md). This is rolled once at character creation. The talent is random (from the Wild Talent table) and cannot be chosen.

### Wild Talent Rules
- Wild talents are weaker versions of standard psionic powers
- They cost Power Points to use (all characters with a wild talent receive a small PP pool: 10 + WIS modifier)
- Wild talents are not tied to a discipline — they cannot be improved through discipline training
- The Psionicist class can convert a wild talent into a full power (with GM-approved discipline fit) at level 3

### Wild Talent Table (d20, sample)
| Roll | Wild Talent | Base Cost | Effect |
|---|---|---|---|
| 1 | Mindlink | 3 PP | One-way telepathic contact; 30 ft range |
| 2 | Precognition | 2 PP | +1 to AC for 3 rounds |
| 3 | Body Equilibrium | 4 PP | Walk on unstable surfaces (sand, silt) without sinking |
| 4 | Object Reading | 3 PP | Sense strong emotional imprint on a held object |
| 5 | Telempathy | 2 PP | Sense surface emotions of one target within 30 ft |
| 6 | Kinetic Burst | 4 PP | 1d8 force damage; knockback 5 ft |
| 7 | Cell Adjustment | 5 PP | Heal 1d6 HP |
| 8 | Danger Sense | 2 PP | +3 to initiative; cannot be Surprised |
| 9 | Far Sight | 3 PP | See clearly up to 120 ft; bypass mundane concealment |
| 10 | Levitation | 4 PP | Float 10 ft off ground; combat speed halved |
| 11 | Conceal Thoughts | 2 PP | Immune to telepathic reading for 1 hour |
| 12 | Displacement | 5 PP | Attackers have -2 to hit for 2 rounds |
| 13 | Recall Agony | 4 PP | 1d10 psychic damage; no physical saving throw |
| 14 | Psionic Blast | 5 PP | All creatures in 20-ft cone: Stunned 1 round (Will DC 13 negates) |
| 15 | Body Weaponry | 4 PP | Natural weapon attack dealing 1d8 + STR |
| 16 | Dimension Slide | 6 PP | Teleport up to 30 ft to a visible location |
| 17 | Domination | 8 PP | Control one creature for 1 round (Will DC 15 negates) |
| 18 | Time Shift | 6 PP | Delay one result by 1 round |
| 19 | Death Field | 10 PP | Deal 2d8 damage to all creatures within 10 ft (no save) |
| 20 | Choose any tier-1 power from any discipline | — | — |

---

## Psionic Disciplines

The Psionicist class organizes psionic powers into five disciplines. At level 1, the Psionicist chooses 2 disciplines and gains access to their power lists. Additional disciplines are gained at levels 4, 7, 10, and 13.

### 1. Telepathy
*The discipline of minds — reading, influencing, communicating with, and destroying the mental fabric of other beings.*

**Flavor:** The most socially versatile and narratively impactful discipline. Telepathy powers can be used outside combat in dialogue, exploration, and stealth contexts.

**Signature Powers:**
- **Mindlink** (2 PP): Two-way telepathic communication; 60 ft range; 10 minutes
- **Telempathy** (3 PP): Read surface emotions; Wisdom check DC to detect the reading
- **Mind Thrust** (varies): Psionic attack mode (see Psionic Combat)
- **Ego Whip** (varies): Psionic attack mode
- **Thought Shield** (varies): Psionic defense mode
- **Mass Domination** (15 PP): Control one creature/level for 3 rounds (Will DC 17 negates)
- **Mind Blank** (8 PP): Target becomes immune to all mental effects for 1 hour
- **Probe** (6 PP): Deep telepathic reading — access memories if Will save DC 14 fails; traumatic
- **Identity Penetration** (10 PP): Strip away personality masks; target must answer questions truthfully for 1 round

### 2. Psychokinesis
*The discipline of force — moving, shaping, heating, and detonating matter with mental power alone.*

**Flavor:** The most combat-effective offensive discipline. Direct damage and battlefield control.

**Signature Powers:**
- **Kinetic Thrust** (3 PP): 2d6 force damage; 1 target; 60 ft range
- **Telekinesis** (4 PP): Move objects up to 50 lbs; 30 ft range; can be used as improvised attack
- **Detonate** (8 PP): 3d8 force damage; 20 ft radius; Reflex DC 15 half
- **Ballistic Attack** (5 PP): Hurl an object as a ranged attack; damage based on object size
- **Heat Metal** (7 PP): Heat any metal object; 1d8 fire/round; iron objects become Fragile immediately — of note since metal is so rare, this power is socially significant
- **Animate Object** (10 PP): Animate one inanimate object to fight under Psionicist's direction for 5 rounds
- **Matter Manipulation** (12 PP): Reshape material; game applications: seal doors, create barriers, shape weapons from available materials

### 3. Psychometabolism
*The discipline of the body — healing, transforming, hardening, and pushing the physical form beyond natural limits.*

**Flavor:** Defensive and utility. The Psionicist who masters Psychometabolism is extremely difficult to kill.

**Signature Powers:**
- **Cell Adjustment** (5 PP): Heal 2d8 HP; can be used in combat as Standard Action
- **Biofeedback** (4 PP): Reduce incoming physical damage by 3 for 5 rounds
- **Body Equilibrium** (3 PP): Move over water, silt, or sand without sinking; 10 minutes
- **Enhanced Strength** (6 PP): +4 STR for 5 rounds
- **Flesh Armor** (8 PP): +4 natural AC for 3 rounds; skin hardens visibly
- **Metamorphosis** (15 PP): Transform into any creature of equal size for 10 minutes; gain its physical attacks and movement types; lose psionic ability while transformed
- **Complete Healing** (20 PP): Restore all HP; remove all conditions; extremely costly; once per long rest maximum
- **Share Strength** (4 PP): Transfer up to 4 STR points from Psionicist to one ally for 5 rounds

### 4. Clairsentience
*The discipline of perception — seeing what is hidden, sensing what is distant, and knowing what has been and what may be.*

**Flavor:** Exploration and investigation utility. Clairsentience powers provide information advantages rather than direct combat benefit. Many dialogue options unlock when the Psionicist has clairsentience.

**Signature Powers:**
- **Danger Sense** (2 PP): +4 to initiative; immune to Surprise; lasts 1 hour
- **Object Reading** (3 PP): Sense psychic impressions on a held object; duration depends on power of impression
- **Clairvoyance** (5 PP): See any location you can clearly visualize within 1 mile; passive observation
- **Precognition** (6 PP): Preview the result of one decision before making it; the DM reveals one likely consequence
- **Sensitivity to Psychic Impressions** (4 PP): Sense residual emotions in a location; reveals "what happened here" at an emotional level
- **All-Around Vision** (6 PP): 360-degree awareness for 10 minutes; cannot be Flanked; Stealth checks against you at +5 DC
- **Fate Link** (8 PP): Link fate to one ally; when that ally takes damage, reduce it by half and transfer the remaining half to the Psionicist

### 5. Psychoportation
*The discipline of space — moving instantly, banishing enemies, and rearranging the battlefield.*

**Flavor:** Tactical repositioning and emergency extractions. The most dangerous discipline in skilled hands; requires precision.

**Signature Powers:**
- **Dimensional Door** (8 PP): Teleport self up to 200 feet to a seen or memorized location
- **Teleport** (15 PP): Teleport anywhere on the current map (not across maps); risk of mis-teleport if target not clearly visualized (5% per 100 feet beyond line of sight)
- **Banishment** (12 PP): Force one creature to teleport to a location you specify within 60 ft; Will DC 16 negates
- **Time Hop** (10 PP): Move self or one target 1 round into the future; target effectively skips their next turn
- **Probability Travel** (20 PP): Emergency escape — exit any combat encounter; the party teleports to the nearest safe location; unreliable (cannot choose destination)
- **Anchor** (5 PP): Mark a location; can return to marked location via Dimensional Door at 50% PP cost; marks persist until replaced

---

## Power Point Economy

### Recovery
- **Long Rest:** Full PP recovery (requires 8 hours sleep, food, water)
- **Short Rest:** Recover WIS modifier × 3 PP (minimum 1)
- **Power Point Font:** Rare consumable; restores 20 PP
- **Meditation** (Psionicist only): Once per short rest, spend 10 minutes in meditation to recover level + WIS modifier PP without a full short rest

### Overspending
If a character attempts to use a power and lacks the PP:
- Roll a Will save DC 12 + (PP deficit)
- Success: Power activates at reduced effect (half damage, half duration); character is Psionic Daze for 1 round
- Failure: Power fails; character takes 1d6 psychic damage per PP deficit; Psionic Daze for 1d3 rounds

### Augmentation
Many powers can be augmented — spending additional PP to improve their effect:
- Standard augment: +2 PP for +1 die of damage or +1 to save DC
- Each power has a listed maximum augmentation (typically 2–4 additional PP)

---

## Psionic Combat

Psionic combat is a parallel to physical combat — it occurs in the same initiative order but on a separate mental plane. A Psionicist can engage in psionic combat on the same turn they take a physical action.

### Who Engages in Psionic Combat
- All Psionicists
- Creatures with psionic ability (marked in bestiary)
- Characters with wild talents **only if they know a mental attack or defense mode**
- Wild talent holders default to one innate defense mode each (see below)

### Mental Attack Modes (5 total — Psionicist knows all at level 1)
| Mode | PP Cost | Effect | Defense Required |
|---|---|---|---|
| Mind Thrust | 2 | 1d10 psychic damage; fast, cheap | Thought Shield or Mental Barrier |
| Ego Whip | 4 | 1d4 CHA damage; Demoralized for 2 rounds | Ego Shield |
| Psychic Crush | 5 | Stun 1d4 rounds; Fort save DC 14 negates | Tower of Iron Will |
| Id Insinuation | 6 | Target loses Standard Action for 2 rounds; multiple Will saves | all defenses reduce |
| Psionic Blast | 7 | 30-ft cone; 2d8 psychic damage; Stunned 1 round (no save) | Tower of Iron Will (partial) |

### Mental Defense Modes (5 total)
| Mode | PP Cost/Round | Protection Against |
|---|---|---|
| Thought Shield | 1 | Reduces Mind Thrust by 1d6; small PP drain |
| Mental Barrier | 2 | +4 to all Will saves vs psionic attacks; 1 round |
| Ego Shield | 2 | Prevents CHA/WIS damage; 1 round |
| Intellect Fortress | 3 | All allies within 10 ft gain +2 to Will saves |
| Tower of Iron Will | 4 | Immunity to one mental attack per round; highest cost |

### Wild Talent Holders (Default Defense)
Characters with a wild talent but no discipline training have one innate defense: **Thought Shield** (costs 1 PP per round, blocks 1d6 from Mind Thrust only). They have no mental attack modes.

### Psionic Combat Sequence
1. Psionicist declares a mental attack against a target
2. Target may declare a mental defense (costs PP from defender's pool)
3. Attack effect is resolved; defense reduces or negates it
4. This takes no additional time — it occurs on the Psionicist's turn
5. Targets that run out of PP have no defense: attacks land at full effect

### Psionic Combat Interface
- A secondary "mental combat" overlay appears when psionic combat is initiated
- Shows both combatants' PP pools, available attack/defense modes, and ongoing mental combat effects
- Physical combat continues simultaneously on the main screen
- The Psionicist must manage both planes at once — this is the core difficulty and skill expression of the class

---

## Psionics and the World

### Social Perception
Psionics are not feared on Athas the way arcane magic is — they are respected, envied, and guarded against. Common people know that a Psionicist can read their mind. Nobles and Templars use psionic dampening amulets. The Sorcerer-Kings have psionic abilities that exceed any player character.

### Psionic Suppression
Var-Khet's obelisk grid suppresses psionic ability within the city walls:
- Wild talents: completely suppressed
- Psionicist class powers: cost double PP
- Mental combat: unavailable
- Disabling the grid is a major early-game objective

### Psionics and the Veiled Alliance
The Veiled Alliance is primarily Preservers, but their intelligence network uses Psionicists extensively. A Psionicist player character receives unique Veiled Alliance dialogue options throughout Act 2.

### The Dragon's Psionic Capability
Borys the Dragon has psionic power that simply cannot be resisted — his mental presence causes Psychic Damage to any psionicist within 100 feet who is actively using psionic powers. This is communicated as an environmental hazard, not a combat encounter.
