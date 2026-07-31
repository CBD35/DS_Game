# Dark Sun: Shattered Lands — Remake GDD
## 06: Magic — Defilers, Preservers, and Elemental Power

**Version:** 0.2
**Last Updated:** 2026-04-20


> ⚠️ **DRAFT — Pending rewrite.** This file contains errors (game is set in **Draj under Tectuktitlay**, not Urik/Hamanu). Content not verified against source PDFs. See `GDD/MASTER_PROJECT_FILE.md` for the authoritative reference.
---

## Table of Contents
1. [Overview](#overview)
2. [Defiler Magic](#defiler-magic)
3. [Preserver Magic](#preserver-magic)
4. [The World Defilement Counter](#the-world-defilement-counter)
5. [Elemental Cleric Magic](#elemental-cleric-magic)
6. [Spell Lists](#spell-lists)
7. [Interactions Between Magic Types](#interactions-between-magic-types)

---

## Overview

Arcane magic on Athas does not draw from a divine source, a ley line network, or an ambient magical field. It draws from **living matter**. Every arcane spell consumes biological energy — the vitality stored in plants, soil microorganisms, and (at higher power levels) animal and humanoid life.

A **Preserver** draws the minimum required energy with surgical precision, leaving the rest intact. The ecosystem is stressed but not destroyed.

A **Defiler** draws everything available, burning out all life in the casting radius for maximum power. The ground is left ash-grey and dead. Nothing grows there for years.

Both wizards cast from the same spell list. The difference is entirely in the method and the consequences.

---

## Defiler Magic

### Casting Mechanics
When a Defiler casts any arcane spell:
1. An **Ash Ring** expands from the caster, radius = spell level × 5 feet
2. All plant life within the ring is destroyed — visually and persistently (the map shows dead zones)
3. Small creatures in the ring take 1 damage per spell level
4. Any conscious being in the ring feels the drain (they know what happened)
5. The spell effect is enhanced (see below)

### Defiler Enhancement
| Spell Level | Enhancement |
|---|---|
| 1 | +1 damage die step (1d4→1d6, 1d6→1d8, etc.) |
| 2 | +1 damage die step, +1 save DC |
| 3 | +1 damage die step, +1 save DC, +1 range increment |
| 4+ | As level 3, +1 duration increment |

### Social and Political Consequences
- Casting in a city: **all NPCs within visual range witness a Defiler cast**. Reaction varies:
  - Common people: Fear, then hostility; -2 Disposition; some flee
  - Templars: First offense = warning + fine; second offense = arrest attempt; third = execute-on-sight
  - Veiled Alliance: Automatic Hostile to the casting character specifically
  - Sorcerer-Kings: Grudging respect — power is respected. Political complexity.
- Casting in the wilderness: Only party members and any NPCs present witness it. No city-state consequences.

### Defiler Unique Abilities
- **Life Drain:** At level 5, Defilers can cast without verbal or somatic components while draining — silent casting
- **Power Surge:** Once per long rest, a Defiler can cast a spell at double power (double dice, +2 save DC, doubled duration) by expanding the Ash Ring to its maximum radius (level × 15 feet)
- **Emergency Reserve:** If reduced to 0 HP, a Defiler may drain 10 feet of surrounding life to immediately gain 2d8 HP. This drains all life in a 10-foot radius. This is instinctual — it triggers automatically and can be disabled in options.

### Defiler NPCs
Key Defiler NPCs in the game respond to a Defiler player character with a specific register — recognition, calculation, or contempt depending on their position. Sorcerer-King Templars treat a Defiler party member as a liability (powerful but uncontrolled) or an asset (useful for controlled defilement operations).

---

## Preserver Magic

### Casting Mechanics
When a Preserver casts any arcane spell:
1. The casting is invisible to casual observers — no visible environmental effect
2. The Preserver draws energy from a diffuse area too large to visually indicate
3. No plants are killed; no animals harmed
4. The spell effect is standard (no enhancement)
5. Veiled Alliance NPCs nearby may subtly recognize the casting pattern

### Preserver Advantages
- **Social:** Can cast anywhere without triggering hostile NPC responses
- **Veiled Alliance Access:** Preservers start with +2 Disposition with the Veiled Alliance; exclusive quest content
- **Ritual Magic:** Preservers can cast **Ritual Spells** — slower versions of spells (10 minutes instead of 1 round) that cost no spell slots. Defilers cannot cast rituals.
- **Verdant Touch:** Once per long rest, a Preserver can cast a spell that simultaneously nourishes the surrounding area — plants within 20 feet bloom briefly. This is cosmetic but has dialogue implications in certain locations.

### Preserver Ritual Spell Examples
| Ritual | Cast Time | Effect | Slot Cost |
|---|---|---|---|
| Purify Water | 10 min | Render 1 gallon contaminated water safe | 0 |
| Plant Growth | 30 min | Accelerate plant growth in 20-ft radius; creates Difficult Terrain | 0 |
| Commune with Nature | 10 min | Learn general terrain features and creature presence within 1 mile | 0 |
| Ward Area | 1 hour | Alarm ward on a 30-ft area; triggers if any creature enters | 0 |
| Slow Poison | 10 min | Delay the onset of a poison's effects by 24 hours | 0 |

### Preserver Narrative Weight
The game does not tell the player Preservers are the "good" choice. The narrative is deliberately ambiguous:
- Preservers are weaker in direct combat — and on Athas, the weak die
- Defilers have done things that matter: the Sorcerer-Kings' power built civilization (of a horrific kind, but civilization)
- The Veiled Alliance has committed atrocities in the name of Preservation
- A Preserver player character who never defiles is making a real sacrifice with real costs

---

## The World Defilement Counter

### What It Is
A persistent world-state tracker measuring the cumulative damage done to Athas by defiler magic — both from the player's party and from background events (Sorcerer-King rituals, random NPC defiler encounters).

The counter is displayed in the game's map interface as a color overlay — green (minimal damage) to deep grey (maximum defilement) on each region of the Tablelands.

### How It's Modified
| Action | Counter Change |
|---|---|
| Defiler casts a 1st-level spell in wilderness | +0.1 |
| Defiler casts a 3rd-level spell in wilderness | +0.3 |
| Defiler casts a 5th-level spell in wilderness | +0.5 |
| Defiler Power Surge (double defilement) | ×2 effect |
| Preserver casts a spell | -0.05 (minor restoration) |
| Preserver Verdant Touch | -0.2 |
| Sorcerer-King background ritual (story event) | +5.0 |
| Serath's immortality ritual (main plot) | +20.0 if not stopped |

The counter starts at approximately 65 (Athas is already mostly dead). At 100, a "final defilement" cutscene triggers — the game's worst ending is available only if the counter reaches 100.

### Regional Consequences
As a region's defilement level increases:
- 70–79: Carbo trees begin dying; water sources yield 50% less
- 80–89: Erdlu herds migrate away; food scarcity increases
- 90–99: The sun appears brighter (hotter); heat stages intensify
- 100: The region becomes a permanent dead zone; any NPCs there die or flee

Players can **counteract** rising defilement by completing Veiled Alliance quests, planting preserved verdant zones, and most critically — stopping the main plot's defilement events.

---

## Elemental Cleric Magic

### Source
Elemental clerics do not draw from living matter. They draw from the elemental planes themselves — a separate layer of reality that underlies Athas. This means elemental magic does not defile and does not affect the Defilement Counter.

### Obtaining Elemental Power
A cleric must be **attuned** to their element. At character creation, this is pre-established (the character has already built the relationship). For new attuners in the fiction: finding an elemental node and performing a 24-hour ritual.

### Elemental Nodes
Scattered across the Tablelands, elemental nodes are locations where the elemental plane is close to the surface. They are visually distinct:
- **Earth nodes:** Unnaturally solid rock formations; slight rumble
- **Air nodes:** Perpetual breeze regardless of weather; sometimes levitating dust
- **Fire nodes:** Persistent flame without fuel; superheated air
- **Water nodes:** Springs, pools, or moisture in otherwise bone-dry areas

Mechanics at a node:
- Cleric spell slots restore at twice the normal rest rate
- Tier-3+ spells can be cast as rituals (no slot cost)
- The node can be "drained" (one-time extraction of a powerful effect) but takes weeks to recover

---

## Spell Lists

### Wizard (Defiler/Preserver) — Arcane

#### Cantrips
- **Acid Splash:** 1d4 acid to one target
- **Chill Touch:** 1d6 necrotic; target cannot regain HP until start of caster's next turn
- **Dancing Lights:** Create 4 floating lights
- **Fire Bolt:** 1d10 fire; 120 ft range
- **Light:** Object glows for 1 hour
- **Mending:** Repair a crack in a non-metal object (fragility removed)
- **Minor Illusion:** Illusory sound or image
- **Prestidigitation:** Minor magical effects
- **Ray of Frost:** 1d8 cold; target speed -10 ft until next turn

#### Level 1
- **Burning Hands:** 3d6 fire; 15-ft cone; Reflex half
- **Charm Person:** Target treats caster as friendly for 1 hour; Will DC 13 negates
- **Detect Magic:** Sense magical auras within 30 ft for 10 minutes
- **Disguise Self:** Change apparent appearance for 1 hour
- **Feather Fall:** Up to 5 falling creatures land safely
- **Fog Cloud:** 20-ft radius of fog; lightly obscures
- **Grease:** 10-ft square becomes slippery; Dexterity save or fall Prone
- **Identify:** Learn properties of a magical item
- **Magic Missile:** 3 darts, 1d4+1 each; auto-hits
- **Shield:** +5 AC for 1 round (reaction)
- **Sleep:** Affect up to 5d8 HP worth of creatures (lowest HP first); unconscious 1 minute
- **Thunderwave:** 2d8 thunder; 15-ft cube; pushes targets 10 ft

#### Level 2
- **Blindness/Deafness:** Blind or Deafen one target; Constitution save DC 14 negates
- **Blur:** Attacks against caster have disadvantage for 1 minute
- **Darkness:** 15-ft radius of magical darkness for 10 minutes
- **Hold Person:** Paralyze one humanoid; Will save DC 14 each round to end
- **Invisibility:** One creature invisible until attacks or casts
- **Knock:** Open any locked door or container
- **Levitate:** Float one creature up to 20 ft off the ground
- **Mirror Image:** Create 3 illusory duplicates; attackers hit duplicates first
- **Scorching Ray:** 3 rays, 2d6 fire each; separate attack rolls
- **Web:** 20-ft cube of webbing; restrained until DC 12 Strength check escape

#### Level 3
- **Dispel Magic:** End one magical effect
- **Fireball:** 8d6 fire; 20-ft radius; Reflex DC 15 half — DEFILER VERSION: 10d6; doubled radius
- **Fly:** Target gains fly speed 60 ft for 10 minutes
- **Haste:** One creature gets extra action and +2 AC for 1 minute
- **Lightning Bolt:** 8d6 lightning; 100-ft line; Reflex DC 15 half
- **Major Image:** Fully sensory illusion up to 20-ft cube
- **Slow:** Up to 6 creatures; speed halved; -2 attack and AC; Will DC 15 negates
- **Stinking Cloud:** Nauseating cloud; Constitution save or lose action
- **Tongues:** Understand and speak any language for 1 hour

#### Level 4
- **Banishment:** Banish one creature to a harmless demi-plane for 1 minute; Will DC 16 negates
- **Confusion:** All creatures in 10-ft radius act randomly for 1 minute; Will DC 16 negates
- **Dimension Door:** Teleport up to 500 ft
- **Greater Invisibility:** Target invisible even while attacking
- **Ice Storm:** 2d8 cold + 4d6 bludgeoning in 20-ft cylinder
- **Wall of Fire:** 60-ft line or 20-ft ring of fire; 5d8 damage per round inside

#### Level 5
- **Dominate Person:** Fully control one humanoid; Will DC 18 negates
- **Hold Monster:** Paralyze any creature; Will save DC 17 each round
- **Telekinesis:** Lift or hurl up to 1,000 lbs; or attack creatures
- **Wall of Stone:** Create up to 10 panels of stone

---

### Cleric — Elemental Domains

#### Earth Domain Spells
- **1st:** Shillelagh (weapon is magically stone), Thunderous Smite
- **2nd:** Earthbind (hold target to ground; no flying), Spike Growth
- **3rd:** Meld into Stone (merge with rock), Stone Shape
- **4th:** Stoneskin (+10 AC for 1 hour; heavy and slow), Guardian of Stone (stone elemental ally)
- **5th:** Wall of Stone, Earthquake (local tremor; Difficult Terrain + Prone checks)

#### Air Domain Spells
- **1st:** Feather Fall, Gust (push target 10 ft)
- **2nd:** Gust of Wind (60-ft line; push Small/Medium creatures back 15 ft), Levitate
- **3rd:** Wind Wall (40-ft wall stops ranged attacks), Call Lightning
- **4th:** Freedom of Movement (ignore difficult terrain; immune to restraint), Storm Sphere
- **5th:** Control Winds, Cyclone (massive knockback area)

#### Fire Domain Spells
- **1st:** Burning Hands, Faerie Fire (outlines creatures; no hiding)
- **2nd:** Flaming Sphere (2d6 fire, rolls to attack), Heat Metal
- **3rd:** Fireball (standard, not enhanced), Protection from Energy (fire immunity 1 hour)
- **4th:** Wall of Fire, Fire Shield
- **5th:** Flame Strike (4d6 fire + 4d6 radiant; no divine flavor — pure elemental)

#### Water Domain Spells
- **1st:** Cure Wounds (1d8+WIS), Bless
- **2nd:** Healing Word (bonus action heal), Lesser Restoration (remove one condition)
- **3rd:** Mass Healing Word, Tidal Wave (3d8 damage + Prone in area)
- **4th:** Greater Restoration (remove curses, max HP reduction, conditions), Water Walk
- **5th:** Mass Cure Wounds (all allies in 30 ft heal 3d8+WIS), Maelstrom

---

## Interactions Between Magic Types

### Can a Wizard Also Have a Wild Talent?
Yes. Wild talents are determined at character creation independently of class. A Defiler with a wild talent is using two completely separate power sources. The wild talent cannot be enhanced by defilement — the systems don't interact.

### Can a Cleric Also Use Arcane Magic?
Not without multi-classing. A single-class Cleric has no access to arcane spells.

### Anti-Magic Effects
- Dispel Magic works on arcane spells and elemental cleric spells
- Dispel Magic does NOT work on psionic powers
- The Var-Khet psionic suppression grid works ONLY on psionics — arcane and elemental magic function normally within it

### Defiler Ash and Elemental Clerics
An Earth or Water Cleric who witnesses defilement can identify the exact location and magnitude of the drain. This gives them a tracking ability against Defilers — a narrative tool for the Veiled Alliance questline.
