# Dark Sun: Shattered Lands — Remake GDD
## 03: Character Classes

**Version:** 0.2
**Last Updated:** 2026-04-20

---

## Overview

Eight classes are available, faithful to the original Shattered Lands. Each has a distinct mechanical identity. Multi-classing is available for specific race/class combinations following AD&D 2e Dark Sun rules.

All classes are measured across the same six attributes. Attack progression, saving throws, and proficiency growth follow a modernized version of the original THAC0 system (converted to d20 with equivalent probabilities).

---

## 1. Fighter

**Description:** The general-purpose warrior. Fighters are the most adaptable combat class — no special restrictions on weapons or armor, the broadest proficiency list, and the highest sustained damage output. On Athas, a good fighter is worth their weight in water.

**Hit Die:** d10
**Armor:** Any (bone, chitin, hide — no metal restriction applies to class, only to world)
**Weapons:** Any
**Saves:** Fortitude-focused

### Primary Attributes
- STR 9+ required
- CON 7+ required

### Proficiency Progression
| Level | Attack Bonus | Proficiency Slots | Special |
|---|---|---|---|
| 1 | +1 | 4 weapon, 3 non-weapon | — |
| 2 | +2 | — | Weapon Specialization available |
| 3 | +3 | +1 weapon | — |
| 4 | +4 | — | Second Attack (1/round → 3/2) |
| 5 | +5 | +1 weapon, +1 non-weapon | — |
| 6 | +6 | — | — |
| 7 | +7 | +1 weapon | Improved Critical (crit on 19-20) |
| 8 | +8 | — | Second Attack improves (3/2 → 2/round) |
| 9 | +9 | +1 weapon, +1 non-weapon | — |
| 10 | +10 | — | — |
| 11 | +11 | +1 weapon | Third Attack (2/round → 5/2) |
| 12 | +12 | — | — |
| 13 | +13 | +1 weapon, +1 non-weapon | Improved Critical (crit on 18-20) |
| 14 | +14 | — | — |
| 15 | +15 | +1 weapon | — |
| 16–20 | +1/level | +1 weapon/2 levels | — |

### Class Abilities
- **Weapon Specialization:** At level 2+, spend 2 proficiency slots on one weapon type to gain +1 attack/+2 damage with it
- **Multiple Attacks:** Gain additional attacks per round at levels 4, 8, 11
- **Combat Tactics:** At level 5, choose one Combat Style (Two-Weapon, Defensive, Mounted — kank-back is available)
- **Parry:** Once per round as a reaction, reduce one incoming melee attack by proficiency bonus

### Remake Additions (vs Original)
- Combat Styles system (was not in original)
- Parry reaction (new)
- Full 20-level table (original was effectively capped at ~15 in practice)

---

## 2. Gladiator

**Description:** The arena specialist. Gladiators are not simply fighters — they are performers, psychologists, and showmen who have spent their lives learning to kill entertainingly in front of a crowd. They combine combat effectiveness with unique morale and crowd-manipulation abilities. Every player character in this game starts as a gladiator slave; the class reflects that origin.

**Hit Die:** d10
**Armor:** Light to medium only (arena rules favor mobility and visibility)
**Weapons:** Any; gain bonus proficiency with exotic arena weapons
**Saves:** Fortitude/Will mixed

### Primary Attributes
- STR 9+ required
- CON 9+ required

### Proficiency Progression
| Level | Attack Bonus | Special |
|---|---|---|
| 1 | +1 | Arena Showmanship; Exotic Weapon Proficiency |
| 2 | +2 | Taunt |
| 3 | +3 | — |
| 4 | +4 | Second Attack |
| 5 | +5 | Combat Display |
| 6 | +6 | — |
| 7 | +7 | Crowd Favor |
| 8 | +8 | Second Attack improves |
| 9 | +9 | — |
| 10 | +10 | Master of the Sand |

### Class Abilities
- **Arena Showmanship:** In any combat with observers, Gladiator can perform a Showmanship action (costs their move action) to gain +2 AC and +1 attack until the start of their next turn. Crowd presence amplifies all combat abilities.
- **Taunt:** Action — target one enemy within 30 feet; Wisdom save DC 10 + Gladiator level or the enemy must target the Gladiator on their next action. Does not work on mindless creatures or psionics.
- **Combat Display:** At level 5 — once per short rest, perform a combat maneuver that imposes -2 on all enemy attack rolls for 2 rounds (Intimidation display).
- **Crowd Favor:** At level 7 — when fighting in any arena or public space with 20+ observers, Gladiator gains temporary HP equal to the crowd's reaction level (1–10, determined by prior performance).
- **Exotic Weapons:** Gladiators have proficiency in weapons not available to other classes: net, trikal, lotulis, alhulak, cahulak, and arrow-head.
- **Master of the Sand:** At level 10 — Gladiator can read combat terrain advantages. +2 to attack and AC when on sandy, uneven, or arena-specific terrain.

### Remake Additions (vs Original)
- Crowd mechanics fully implemented (original had no crowd interaction system)
- Taunt as a strategic combat ability (new)
- Exotic weapon list expanded and fully functional

### Narrative Note
All party members start as gladiators regardless of their eventual class — the opening act is set in an arena. Class selection determines what they become *after* escape.

---

## 3. Ranger

**Description:** The wilderness specialist. Rangers are survivalists, trackers, and ambush fighters who have made the Athasian wastes their home. They are the only class with meaningful survival skill integration. On a world where the wilderness kills most people who enter it unprepared, a ranger is invaluable.

**Hit Die:** d8
**Armor:** Light only (heavy armor impedes tracking and movement)
**Weapons:** Any; bonus with ranged weapons and two-weapon fighting
**Saves:** Fortitude/Reflex mixed

### Primary Attributes
- STR 8+ required
- DEX 9+ required
- CON 12+ required
- WIS 12+ required

### Class Abilities
- **Favored Enemy:** At levels 1, 5, 10, 15 — choose a creature type; +2 to attack and damage against that type, +4 to Tracking/Survival checks involving them. Original game favored enemies still available: humanoid, undead, animal, psionic beast.
- **Tracking:** Rangers can follow creature tracks at base Survival DC 10; modified by terrain, time elapsed, and creature size. Critical for several main-story segments.
- **Two-Weapon Fighting:** Rangers reduce two-weapon penalties by 2 each (normally -4/-4; Rangers use -2/-2)
- **Wilderness Survival:** Rangers never fail basic survival checks in terrain they have experience with. Auto-find water once per day on a successful Survival check DC varies by terrain.
- **Camouflage:** In natural terrain, Rangers can Hide without cover or concealment (Stealth check DC modified by terrain type)
- **Animal Empathy:** Rangers can attempt to calm or communicate basic intent to non-psionic animals (Wisdom check, DC by animal hostility)

### Levels 1–20
Attack progression identical to Fighter but one step slower. Gain Favored Enemy at 1, 5, 10, 15. Wilderness Stealth improves at 5, 10. Multi-attack at level 7 (3/2) and 14 (2/round).

### Remake Additions
- Tracking system is fully interactive (not just a passive check in original)
- Camouflage enables stealth sequences in wilderness encounters

---

## 4. Thief

**Description:** The rogue. On Athas, thieves operate in a world with no banks, no locks worth picking, and very few pockets worth cutting — but enormous amounts of valuable information, dangerous secrets, and unguarded backs. Athasian thieves are information brokers, poison specialists, and precision killers as much as pickpockets.

**Hit Die:** d6
**Armor:** Light only
**Weapons:** Light weapons, shortbows; penalty with heavy weapons
**Saves:** Reflex-focused

### Primary Attributes
- DEX 9+ required

### Thief Skills
Thieves receive 60 skill points at level 1 + 30 per level, distributed among:
- **Pick Pockets** — lifting items from NPCs; also used to plant items
- **Open Locks** — bone and chitin locks are common; some crystal locks require higher skill
- **Find/Remove Traps** — detection and disarming
- **Move Silently** — base stealth movement
- **Hide in Shadows** — stationary concealment
- **Detect Noise** — passive listening
- **Climb Walls** — scaling surfaces
- **Read Languages** — deciphering ancient texts (important for lore content)
- **Backstab Multiplier** — not a skill but improves with level (see below)

### Backstab
When attacking an unaware or flanked target from behind: damage multiplier based on level.
| Level | Backstab Multiplier |
|---|---|
| 1–4 | ×2 |
| 5–8 | ×3 |
| 9–12 | ×4 |
| 13–16 | ×5 |
| 17–20 | ×6 |

### Class Abilities
- **Poison Use:** Thieves can apply poison to weapons without risk of self-poisoning (other classes risk 20% self-poisoning on application failure)
- **Evasion:** If a Reflex save would reduce damage to half, Thief takes 0 damage instead
- **Opportunist:** When any ally attacks an enemy, Thief may use a reaction to make one attack against that enemy at +2

### Remake Additions
- Read Languages implemented as a full document/codex mechanic (reveals lore inscriptions)
- Poison crafting system (new — requires materials found in the wild)
- Social thievery: Pick Pockets skill used to plant evidence, swap items in dialogue scenes

---

## 5. Bard

**Description:** Athasian bards are not singers — they are information merchants, poison sellers, smooth-talking fixers, and occasionally assassins. Their music is a cover for more profitable activities. They are the social engineering class: every faction wants something a bard can get, find, or sell.

**Hit Die:** d6
**Armor:** Light only
**Weapons:** Any one-handed; shortbows
**Saves:** Mixed (Reflex/Will)

### Primary Attributes
- DEX 9+ required
- INT 13+ required
- CHR 15+ required

### Class Abilities
- **Bard Music:** Not performance — embedded signals. Bard music can: Inspire allies (+1 to attacks for 3 rounds), Counter Fear (suppress Frightened condition), Distract enemies (-1 to saves vs the Bard's abilities for 2 rounds). Usable 3 + CHR modifier times per long rest.
- **Lore:** Bards have extensive knowledge of Athasian history, factions, and personalities. +4 to all History and Faction Knowledge checks; often provides unique dialogue options that reveal secret information.
- **Poisons:** Bards begin with proficiency in 3 poison types and can identify and apply them without risk. Higher levels add more complex poisons.
- **Thief Skills (Limited):** Bards receive 40 points at level 1 + 20/level in: Pick Pockets, Open Locks, Move Silently, Hide in Shadows, Detect Noise, Read Languages.
- **Influence:** Once per short rest, the Bard can attempt to shift an NPC's Disposition by 1 step (Hostile→Unfriendly, Unfriendly→Neutral, etc.) without a skill check. This is narrative persuasion, not magic.
- **City Contacts:** In each city-state, Bards can establish a contact network. After one in-game day in a city, they can access a contact for information (costs gold or a favor).

### Progression Note
Bards advance more slowly in combat than Fighters but have the broadest non-combat skill set of any class.

### Remake Additions
- Contact network system (new — replaces the original's generic "Gather Information")
- Poison specialization tree (new)
- Full faction knowledge integration with dialogue system

---

## 6. Cleric

**Description:** On Athas, there are no gods. There is only the land, the sky, the fire, and the water — and each of those elements has priests who draw power directly from them. Elemental clerics are not chosen by a deity; they forge a pact with an elemental force. Their magic is real, potent, and deeply tied to the health of Athas itself.

**Hit Die:** d8
**Armor:** Any
**Weapons:** Restricted by element (see below)
**Saves:** Will-focused

### Primary Attributes
- WIS 9+ required

### Element Selection
At character creation, the Cleric chooses one of four elemental allegiances. This is permanent.

| Element | Thematic Focus | Weapon Restriction | Bonus Domain |
|---|---|---|---|
| Earth | Endurance, stone, protection | Blunt weapons only | Fortification, tremorsense |
| Air | Speed, breath, freedom | Light weapons only | Movement, weather |
| Fire | Destruction, passion, purification | Any; bonus with fire | Burning, intimidation |
| Water | Healing, purity, life | Any; bonus with fluid weapons | Restoration, divination |

### Spell Progression
Clerics cast spells per day by level. No memorization slots are lost permanently (rest restores all). Spells are drawn from the elemental domain list (see 06_magic.md).

| Level | 1st | 2nd | 3rd | 4th | 5th |
|---|---|---|---|---|---|
| 1 | 1 | — | — | — | — |
| 2 | 2 | — | — | — | — |
| 3 | 2 | 1 | — | — | — |
| 4 | 3 | 2 | — | — | — |
| 5 | 3 | 3 | 1 | — | — |
| 6 | 3 | 3 | 2 | — | — |
| 7 | 3 | 3 | 2 | 1 | — |
| 8 | 3 | 3 | 3 | 2 | — |
| 9 | 4 | 4 | 3 | 2 | 1 |
| 10 | 4 | 4 | 3 | 3 | 2 |

### Class Abilities
- **Turn Undead:** Clerics can Rebuke or Turn undead; Water and Earth clerics gain bonus vs undead; Fire clerics have the most powerful turn effect
- **Elemental Attunement:** Once per long rest, a Cleric can sense their element's presence within 60 feet (water sources, fire, moving air, stone thickness)
- **Elemental Resistance:** At level 5, permanent resistance to their element's damage type
- **Elemental Avatar:** At level 10 — once per long rest, briefly channel their element's avatar form for 3 rounds (+2 to all stats related to element)

### Remake Additions (vs Original)
- Elemental quest lines for each domain (4 new quest chains — original had no element-specific content)
- Elemental node system: certain locations on the map are strong nodes; casting near them costs no spell slots
- Water clerics have expanded healing options (Water was underpowered in original)

---

## 7. Wizard

**Description:** Arcane magic on Athas comes at a cost. Every arcane spell draws energy from living matter. A Preserver takes only the minimum required, carefully preserving the rest. A Defiler takes everything they can reach, burning the earth for power. This is not a cosmetic choice — it is the most morally consequential decision in character creation.

**Hit Die:** d4
**Armor:** None (arcane magic requires freedom of movement)
**Weapons:** Daggers, staves, darts
**Saves:** Will-focused

### Primary Attributes
- INT 9+ required

### Defiler vs Preserver
At character creation, the player chooses. This cannot be changed without a major narrative event.

**Defiler:**
- Spells are 1 die step more powerful (1d6 becomes 1d8, etc.)
- Casting creates a visible ash ring (radius = spell level × 5 feet) that kills all plants in range
- NPCs who witness defilement react with fear, hostility, or both
- Templars will report a Defiler cast in a city
- Accelerates world defilement counter (see 06_magic.md)
- Gains Templar tolerance (Templars are less hostile to known Defilers — power is respected)

**Preserver:**
- Standard spell power
- No environmental damage
- Veiled Alliance starts with +2 Disposition toward Preservers
- Access to Preserver-only ritual spells (slower, powerful, no defilement)
- Can cast in cities without triggering hostile responses

### Spell Progression
| Level | Cantrips | 1st | 2nd | 3rd | 4th | 5th |
|---|---|---|---|---|---|---|
| 1 | 2 | 1 | — | — | — | — |
| 2 | 2 | 2 | — | — | — | — |
| 3 | 2 | 2 | 1 | — | — | — |
| 4 | 3 | 3 | 2 | — | — | — |
| 5 | 3 | 3 | 2 | 1 | — | — |
| 6 | 3 | 3 | 3 | 2 | — | — |
| 7 | 3 | 4 | 3 | 2 | 1 | — |
| 8 | 3 | 4 | 3 | 3 | 2 | — |
| 9 | 3 | 4 | 4 | 3 | 2 | 1 |
| 10 | 4 | 4 | 4 | 3 | 3 | 2 |

### Cantrip Examples
Dancing Lights, Mending (bone and chitin repair), Prestidigitation, Light, Chill Touch

### Remake Additions (vs Original)
- World defilement counter — Defilers affect a persistent world state (new)
- Preserver ritual spells — slow-cast powerful spells unavailable to Defilers (new)
- Defiler/Preserver switching — now possible via narrative event (was locked in original)

---

## 8. Psionicist

**Description:** The Psionicist is the master of mind-over-matter — the only class built entirely around psionic ability rather than physical combat or arcane magic. On Athas, where psionics are universal (every being has a chance at a wild talent), the Psionicist is a professional: trained, disciplined, and devastating.

**Hit Die:** d6
**Armor:** None or light only (psionic disciplines require concentration)
**Weapons:** Any one-handed
**Saves:** Will-focused (highest Will saves of any class)

### Primary Attributes
- INT 12+ required
- WIS 15+ required

### Psionic Power Points
The Psionicist's core resource. See 05_psionics.md for full system.

| Level | Power Points | Disciplines Known | Powers Known |
|---|---|---|---|
| 1 | 15 | 2 | 5 |
| 2 | 20 | 2 | 7 |
| 3 | 25 | 2 | 9 |
| 4 | 30 | 3 | 11 |
| 5 | 40 | 3 | 13 |
| 6 | 50 | 3 | 15 |
| 7 | 60 | 4 | 17 |
| 8 | 70 | 4 | 19 |
| 9 | 85 | 4 | 21 |
| 10 | 100 | 5 | 23 |

### Disciplines Available
- Telepathy, Psychokinesis, Psychometabolism, Clairsentience, Psychoportation (see 05_psionics.md)
- At level 1, choose 2 disciplines; gain 1 additional discipline at levels 4, 7, 10, 13

### Class Abilities
- **Psionic Combat Modes:** Psionicists gain access to all 5 mental attack modes and all 5 mental defense modes (see 05_psionics.md). Others have at most 1–2 wild modes.
- **Power Surge:** Once per long rest — spend 1d10 additional power points beyond a power's cost to maximize its effect (damage maximized, duration maximized, DC +3)
- **Mental Fortress:** Psionicist is immune to psionic fear effects and has Advantage on all Will saves vs psionic powers
- **Psychic Sense:** Always knows if another sapient creature is within 30 feet, even through walls or in darkness (no details, just presence)

### Remake Additions (vs Original)
- Full 5-discipline tree system (original had a limited selection)
- Psionic combat overlay as a parallel to physical combat (new)
- Mental Fortress as a high-level class ability (new)

---

## Multi-Classing

Available to non-human races as per AD&D 2e Dark Sun rules. Humans may dual-class (abandon one class entirely, restart at level 1 in a new class, eventually surpass the original).

### Common Multi-Class Combinations
| Race | Multi-Class | Notes |
|---|---|---|
| Elf | Fighter/Thief | Classic Athasian scout |
| Elf | Ranger/Wizard (Preserver) | Veiled Alliance operative |
| Half-Elf | Fighter/Thief, Fighter/Cleric | Balanced hybrid |
| Dwarf | Fighter/Cleric | Earth domain is thematically perfect |
| Thri-Kreen | Fighter/Psionicist | The most dangerous combination in the game |
| Mul | Fighter/Gladiator | Redundant but maximizes arena-origin concept |

### Multi-Class Rules
- XP split evenly between classes
- Use the better attack bonus of either class
- Use the higher saving throw value for each save category
- HP: average the two hit dice types
- Skill points: average of the two class grants

### Human Dual-Classing
- Abandon Class A (abilities freeze)
- Level in Class B from scratch
- When Class B level exceeds Class A level: all Class A abilities become available again
- Cannot wear armor that Class A restricted while leveling Class B
