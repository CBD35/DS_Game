# Dark Sun: Shattered Lands — Remake GDD
## 07: Character Progression

**Version:** 0.2
**Last Updated:** 2026-04-20

---

## Table of Contents
1. [Experience Points](#experience-points)
2. [Leveling](#leveling)
3. [Attributes](#attributes)
4. [Skills and Proficiencies](#skills-and-proficiencies)
5. [Reputation and Infamy](#reputation-and-infamy)
6. [Party Dynamics](#party-dynamics)
7. [Companion Progression](#companion-progression)

---

## Experience Points

### Sources
| Source | XP Award | Notes |
|---|---|---|
| Defeating an enemy in combat | CR × 100 | Divided equally among party |
| Subduing without killing | CR × 150 | Bonus for non-lethal resolution |
| Completing a quest (major) | 500–2000 | Based on quest difficulty and impact |
| Completing a quest (minor) | 100–500 | |
| Discovering a location | 50–200 | First visit only |
| Successful skill application | 25–100 | For meaningful non-combat skill use |
| Dialogue resolution (avoided combat) | Same as combat XP | Reward for non-combat solutions |
| Faction milestone | 300–1000 | Each time a faction relationship advances a tier |

### XP and Multi-Classing
Multi-class characters split XP equally between their active classes. Dual-class humans accumulate XP only in the new class until it surpasses the old class level, at which point both classes share XP going forward.

### Level Cap
Level 20 in any single class. Multi-class characters can reach level 20 in any individual class but total level is effectively 20 (XP split slows progression).

---

## Leveling

### Level Thresholds
| Level | XP Required | Notable Milestone |
|---|---|---|
| 1 | 0 | Game start |
| 2 | 2,000 | — |
| 3 | 4,000 | — |
| 4 | 8,000 | Multi-class: gain third discipline (Psionicist) |
| 5 | 16,000 | Favored Enemy 2 (Ranger); Backstab ×3 (Thief) |
| 6 | 32,000 | — |
| 7 | 64,000 | Third Attack progression begins |
| 8 | 120,000 | — |
| 9 | 250,000 | All classes gain a "Master" ability (unique per class) |
| 10 | 500,000 | — |
| 15 | 1,500,000 | — |
| 20 | 3,000,000 | Pinnacle; post-game content unlocks |

### On Leveling Up
When a character levels up:
1. Roll new hit die (d4–d10 by class); add CON modifier; add to max HP
2. Apply any new class abilities granted at that level
3. Receive new proficiency slots (weapon and non-weapon)
4. If applicable: gain new spell slots, PP, or psionic powers

### No Level Loss on Death
The original game used level drain mechanics for some undead. The remake removes this — death costs time, resources, and morale, but not XP.

---

## Attributes

### The Six Core Attributes
| Attribute | Governs |
|---|---|
| Strength (STR) | Melee attack/damage, encumbrance, forced-open checks |
| Dexterity (DEX) | Ranged attack, AC, initiative, thief skills |
| Constitution (CON) | HP per level, Death Save bonus, heat/exposure resistance |
| Intelligence (INT) | Wizard spell access, skill points, knowledge checks |
| Wisdom (WIS) | Cleric/Psionicist power, Will saves, Perception |
| Charisma (CHR) | Persuasion, Intimidation, Bard abilities, initial NPC Disposition |

### Attribute Checks
When the game calls for a raw attribute check: roll d20, add the relevant attribute modifier (see below), compare to DC.

### Modifier Table
| Score | Modifier |
|---|---|
| 3 | -4 |
| 4–5 | -3 |
| 6–7 | -2 |
| 8–9 | -1 |
| 10–11 | +0 |
| 12–13 | +1 |
| 14–15 | +2 |
| 16–17 | +3 |
| 18 | +4 |
| 19 | +5 |
| 20 | +6 |
| 21–22 | +7 |

### Attribute Improvement
Characters gain one attribute point at levels 4, 8, 12, 16, and 20. This point can be applied to any attribute, up to the racial maximum. This replaces the original game's fixed stat gains with player choice.

---

## Skills and Proficiencies

### Weapon Proficiencies
Every class starts with a fixed number of weapon proficiency slots and gains more per level (see 03_classes.md). Using an unproficient weapon imposes -2 to attack.

**Weapon Specialization** (Fighter/Gladiator only): Spend 2 slots on one weapon type for +1 attack and +2 damage.

**Weapon Mastery** (level 9+ Fighter only): Spend 3 more slots on already-specialized weapon for expanded critical range and one free special maneuver per combat.

### Non-Weapon Proficiencies
Non-weapon proficiencies represent skills outside combat. Each has a governing attribute. Checks are: d20 + attribute modifier vs DC.

| Proficiency | Attribute | Representative Uses |
|---|---|---|
| Survival | WIS | Finding water, identifying safe camp sites, avoiding hazards |
| Tracking | WIS | Following creature trails |
| Healing | WIS | Stabilize dying; remove conditions with kit |
| Craft (specify) | INT | Repair weapons; make simple tools; bone/chitin/obsidian work |
| Persuasion | CHR | Social negotiation |
| Deception | CHR | Lying convincingly |
| Intimidation | STR or CHR | Threatening NPCs |
| Insight | WIS | Detecting lies; reading intentions |
| History | INT | Recall Athasian lore |
| Nature | WIS | Identify creatures, plants, terrain features |
| Stealth | DEX | Move silently |
| Perception | WIS | Notice hidden things |
| Athletics | STR | Climbing, swimming, jumping |
| Acrobatics | DEX | Balance, tumbling, dodging |
| Thieves' Tools | DEX | Pick locks, disarm traps (Thief class gets this free) |
| Psionic Lore | INT | Identify psionic effects and items |
| Arcane Lore | INT | Identify spells and magical items |
| Elemental Lore | WIS | Identify elemental nodes, effects, and cleric magic |

### Proficiency Slots
Each class receives proficiency slots at creation and gains additional slots per level (see 03_classes.md for class-specific tables). One slot = one weapon proficiency OR one non-weapon proficiency.

Exceptions:
- Thief skills are a separate pool (see 03_classes.md)
- Rangers receive Tracking and Survival for free at level 1
- Bards receive Persuasion and History for free at level 1

---

## Reputation and Infamy

The Reputation/Infamy system replaces the alignment system entirely. There is no "good/evil" axis — only how the world perceives your actions and what your actions have actually done.

### Reputation Tracks
Five faction-specific reputation tracks (see 09_narrative.md for factions):

| Faction | Friendly Threshold | Hostile Threshold |
|---|---|---|
| Veiled Alliance | 25 | -10 |
| Merchant Houses | 30 | -15 |
| Templars | 20 | -5 |
| Elemental Cults | 20 | -10 |
| Slave Population | 15 | -5 |

Each track runs from -50 (Kill on Sight) to +100 (Full Alliance). Starting values vary by race and class.

### Actions That Modify Reputation
| Action | Veiled Alliance | Templars | Slaves |
|---|---|---|---|
| Free a slave group | +10 | -8 | +15 |
| Perform a public defilement | -15 | +5 | -5 |
| Assist a Templar patrol | -10 | +12 | -8 |
| Complete an Alliance mission | +20 | -5 | +5 |
| Turn in a Defiler to Templars | -20 | +15 | 0 |
| Kill a Merchant House agent | -15 (House) | 0 | +3 |
| Destroy an elemental node | -10 (Cults) | 0 | 0 |
| Restore an elemental node | +15 (Cults) | -5 | 0 |

### Infamy
A separate global track measuring how feared or notorious the party has become. Infamy is not inherently bad — it opens some doors (powerful individuals treat you seriously) while closing others (merchants may refuse service; some quests unavailable).

| Infamy Level | Label | Effects |
|---|---|---|
| 0–20 | Unknown | No effect |
| 21–40 | Noticed | Some NPCs recognize the party; guards watch more closely |
| 41–60 | Feared | Weaker enemies may flee; some merchants charge 20% premium |
| 61–80 | Dreaded | Templar patrols actively hunt the party in cities; rare NPCs seek you out for dangerous work |
| 81–100 | Legend | Major faction leaders seek direct contact; Sorcerer-Kings are aware of you |

---

## Party Dynamics

### Party Composition
The player controls 1–4 characters. Characters can be created at the start or (for the remake) recruited as named companions found in the world.

### Morale and Bond
Over time, party members develop relationships with each other. These are tracked silently and expressed through:
- **Combat Assist:** Party members with a high bond will spend their reaction to shield each other without being commanded
- **Dialogue:** Characters comment on each other's decisions; approve/disapprove of major choices
- **Bond Abilities:** At high bond levels, paired characters unlock a once-per-long-rest combined ability (e.g., Fighter + Gladiator: coordinated strike with combined attack bonus)

### Party Communication
Party members can be individually commanded or set to one of three AI stances:
- **Aggressive:** Uses all available offensive actions; no retreat
- **Defensive:** Prioritizes survival; retreats when below 30% HP
- **Support:** Prioritizes healing and buffing allies over dealing damage

---

## Companion Progression

### Named Companions (Remake Addition)
The remake introduces 6 named companions found during the story. Each has:
- A fixed class (cannot be changed)
- A fixed race
- A personal questline that spans 2+ acts
- Unique dialogue throughout the game
- A personal arc that concludes differently based on player choices

### Companion XP
Companions level up at the same pace as the player party regardless of whether they are currently active. Companions not in the active party do not fall behind.

### Companion Loyalty
Each companion has a Loyalty track (0–100). Low Loyalty causes them to refuse certain orders, voice strong objection to decisions, or — at Loyalty below 10 — leave the party permanently. High Loyalty unlocks personal quests, deeper dialogue, and Bond Abilities.

Actions that affect Loyalty are specific to each companion's values — documented in the companion profiles (see 09_narrative.md).
