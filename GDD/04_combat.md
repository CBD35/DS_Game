# Dark Sun: Shattered Lands — Remake GDD
## 04: Combat System

**Version:** 0.2
**Last Updated:** 2026-04-20

---

## Table of Contents
1. [Combat Philosophy](#combat-philosophy)
2. [Turn Structure](#turn-structure)
3. [Action Economy](#action-economy)
4. [Attack Resolution](#attack-resolution)
5. [Damage and Death](#damage-and-death)
6. [Conditions](#conditions)
7. [Environmental Combat](#environmental-combat)
8. [Arena Rules](#arena-rules)
9. [Morale System](#morale-system)
10. [Fleeing Combat](#fleeing-combat)

---

## Combat Philosophy

Combat in the remake is turn-based, tactical, and unforgiving. The goal is to preserve the original game's lethality while adding the clarity and depth modern players expect.

Key principles:
- **Attrition matters.** Healing resources are limited. A costly victory is a real cost.
- **Positioning matters.** Flanking, elevation, and terrain interact with every attack.
- **Preparation matters.** Entering combat without water and in heat is a death sentence.
- **Every enemy is lethal.** No "trash mobs." Even the weakest opponents are dangerous in numbers.

---

## Turn Structure

### Initiative
At the start of each combat encounter:
1. Each combatant rolls d10 + DEX modifier
2. Highest initiative acts first, descending
3. Ties broken by DEX score; if still tied, simultaneous resolution
4. Initiative is rolled once per encounter (not re-rolled each round) — exceptions: Surprise Round and Panic events

### Round Duration
Each round represents approximately 1 minute of combat time. Actions within a round are not perfectly sequential — initiative represents who acts decisively first, not who literally moves before the other.

### Surprise
If one side is undetected at combat start:
- Surprised side loses their first full turn
- Surprising side gets a free standard action before initiative is rolled
- Thri-Kreen in the party add +3 to party's Surprise Detection check

---

## Action Economy

Each combatant receives per turn:
- **1 Standard Action** — attack, cast a spell, use a psionic power, use an item, Taunt, Aid Another, etc.
- **1 Move Action** — move up to full Speed, stand from Prone, draw/sheath a weapon, open a door
- **1 Reaction** (once per round, outside your turn) — opportunity attack, Parry (Fighter), Shield Block, dodge attempt

### Action Combinations
- Standard + Move: standard use
- Standard + Standard (Full Attack): sacrifice Move action to make all available attacks this round (applies multi-attack at appropriate levels)
- Move + Move (Full Move): double movement distance; cannot make a Standard Action

### Free Actions (no action cost)
- Speak up to one sentence
- Drop a held item
- Drop to Prone

---

## Attack Resolution

### The d20 System (Modernized THAC0)
All attacks use d20 + Attack Bonus vs target's Armor Class.
- Hit if: d20 + Attack Bonus ≥ target AC
- Target AC = 10 + DEX modifier + Armor bonus + Shield bonus + Magical bonuses
- Attack Bonus = Base Attack Bonus (BAB) + STR (melee) or DEX (ranged) modifier + proficiency bonus + weapon bonus

This preserves the original game's probability curves (derived from THAC0 tables) within a d20 interface.

### Critical Hits and Fumbles
- **Natural 20:** Critical hit — roll damage twice (or triple with a slashing weapon and Weapon Mastery)
- **Natural 1:** Fumble — roll on the Fumble Table

**Fumble Table (d6):**
| Roll | Result |
|---|---|
| 1 | No effect beyond miss |
| 2 | Off-balance: -2 AC until next turn |
| 3 | Weapon Fragility check (if applicable) |
| 4 | Drop weapon (free action to pick up) |
| 5 | Hit an adjacent ally (half damage, no crit) |
| 6 | Fall Prone |

### Weapon Proficiency
- **Proficient:** Full attack bonus
- **Non-proficient:** -2 attack penalty
- **Specialized (Fighter/Gladiator):** +1 attack, +2 damage with chosen weapon type

### Flanking
When two allies are on directly opposite sides of an enemy: both gain +2 to attack rolls against that enemy.

### Elevation
Higher ground grants +1 to ranged attack rolls; lower ground imposes -1 to ranged attacks against higher targets.

### Cover
| Cover Type | AC Bonus | Notes |
|---|---|---|
| Half (low wall, large rock) | +2 | — |
| Three-quarters (arrow slit, corner) | +5 | Ranged attacks only: -2 to attacker |
| Full (total) | Cannot be targeted | Must move to engage |

---

## Damage and Death

### Hit Points
HP represents combat viability — a combination of physical durability, skill at avoiding lethal blows, and fighting spirit. At 0 HP, the character is Incapacitated, not necessarily dead.

### The Death Threshold
At 0 HP, the character falls and must make a **Death Saving Throw** each round:
- Roll d20; 10+ = Stabilize for this round (still at 0 HP but not losing ground)
- Three successes before three failures: Stabilized at 0 HP (unconscious, not dying)
- Three failures before three successes: Dead
- A CON modifier applies to all Death Saving Throws
- Healing any amount of HP returns the character to consciousness at 1 HP minimum

### Permadeath Option
The remake includes a permadeath toggle (enabled in Hardcore mode). When enabled, a character who dies cannot be recovered and the party must continue without them — or recruit a replacement.

### Healing Resources
Healing on Athas is scarce:
- **Short Rest (1 hour):** Spend Hit Dice (d4–d10 by class) to recover HP. Each character has CON modifier + level/2 HD per day.
- **Long Rest (8 hours):** Recover all Hit Dice; regain full HP; requires water and food or no full recovery
- **Cleric Spells (Water domain primary):** The primary magical healing source
- **Psionic Healing (Psychometabolism):** Secondary healing source; costly in Power Points
- **Healing Kits:** Consumable; restore 1d6 HP per use; can stabilize a dying character

**No infinite healing.** Long rests in the wilderness require camp supplies. In the desert, a long rest can be interrupted by heat, predators, or weather.

---

## Conditions

| Condition | Effect | How to Remove |
|---|---|---|
| Prone | -4 to melee attacks; ranged attackers gain +2 vs you; move action to stand | Stand up (Move action) |
| Fatigued | -2 to STR and DEX-based checks | Short rest or Cleric/psionic restoration |
| Exhausted | -6 to STR and DEX; speed halved; cannot run | Long rest with food and water |
| Scorched | -2 to all attacks; -1 AC; max HP -10% | Shade + water for 1 hour |
| Frightened | Must move away from source; -2 to attacks while in line of sight | Break line of sight; Will save each round |
| Stunned | Lose Standard Action; -2 AC | Lasts 1d3 rounds |
| Blinded | -4 to attack; attackers gain +4 vs you | Condition ends or Cleric cure |
| Bleeding | Lose 1 HP per round | Healing Kit, any healing spell, or Bind Wounds action |
| Poisoned | Effect varies by poison type | Antidote, Cleric neutralize, or duration expires |
| Demoralized | -1 to all combat rolls; may flee on morale check | Morale recovery (see Morale System) |
| Psionic Daze | Cannot use psionic powers; -1 to Will saves | 1d3 rounds |

---

## Environmental Combat

The environment is an active participant in every fight.

### Sand and Loose Ground
- Running on sand: speed -5 ft
- Charging on sand: Dexterity check DC 10 or fall Prone at end of charge
- Burrowing creatures: gain Stealth (DC 18 to detect while burrowed)

### Heat During Combat
- Combat during Peak heat: each character makes a Constitution save at end of round 5 (DC 10 + 1 per additional round after 5); failure = 1 heat damage and Fatigued on next failure

### Fire
- Being struck by fire deals Burning condition: 1d4 fire damage at start of each turn until extinguished
- Extinguish: use Move action to stop-drop-roll (DC 10 DEX check) or have water poured on you
- Fire spreads to adjacent flammable objects each round

### Darkness and Low Light
- Torches illuminate 20-foot radius; dim light to 40 feet
- Attacks in dim light: -2 to attack rolls
- Attacks in full darkness: -4 to attack; requires Blindsense or Thri-Kreen thermal vision to negate
- Candles and small flames: 5-foot radius only

### Water Features
- Rare but present (oases, sewers, cisterns)
- Difficult terrain to move through
- Extinguishes fire conditions
- Electrical damage in water: area effect (all within water take damage)

---

## Arena Rules

The game begins in an arena. Gladiatorial combat returns in several story segments and optional side content. Arena rules differ from standard combat:

### Arena-Specific Rules
- **No Death Until the Crowd Decides:** In an arena fight, a character at 0 HP is Incapacitated but not automatically killed. The crowd (or the presiding noble/Templar) must call for death or mercy. This creates a window for dramatic reversals.
- **Crowd Reaction Meter:** Tracks audience approval (1–10). High-impact moves (critical hits, Devastating Blow, Gladiator Showmanship) increase the meter. Cowering, missing multiple times, or ignoring a prone enemy decreases it.
- **Arena Conditions:** Sand floor, sun overhead (apply heat rules), elevated spectator galleries (ranged attack angle issues), occasional arena hazards (gates that open releasing beasts, pit traps).
- **Weapons Check:** Standard arena bouts use designated weapons. Using psionic powers in a non-designated bout is grounds for disqualification — and a Templar response.
- **Betting Mechanic:** Party members not in the fight can wager gold on outcomes. Odds are calculated from party-level matchup. Winnings fund equipment.

### Championship Fights
Several story-critical arena events have special rules:
- Multi-stage bouts (survive Wave 1 before Wave 2 is released)
- Team vs team (player party vs another slave team)
- Beast round (one or more players vs a megafauna creature)
- Death match (no mercy; crowd cannot save you)

---

## Morale System

Non-player-controlled enemies have morale ratings that can break under pressure.

### Morale Rating
Enemies have a morale rating from 2 (cowardly) to 12 (fanatical). Templars and arena guards rate 8–10. Raider bands rate 5–7. Undead and Silt Horrors are immune to morale.

### Morale Check Triggers
A morale check (d12 roll vs morale rating) is triggered when:
- The group loses 25% of its members in a single fight
- The group loses 50% of its members total
- The group's leader is killed or incapacitated
- A party member uses a highly intimidating ability (Half-Giant's Intimidating Presence, Gladiator's Combat Display)
- The enemy takes an unexpected and catastrophic hit (50%+ HP in one strike)

### Morale Failure Results
| Check Result | Outcome |
|---|---|
| Failed by 1–2 | Demoralized: -1 to all combat rolls for 3 rounds |
| Failed by 3–4 | Withdraw: moves toward nearest exit; will not attack unless cornered |
| Failed by 5+ | Rout: drops weapons, flees; does not return |

### Player Party Morale
The player party does not have morale ratings but can suffer the **Shaken** condition from narrative events. Shaken imposes -1 to Will saves for 1 hour. Removed by rest or a Bard's Counter Fear ability.

---

## Fleeing Combat

Players can attempt to disengage and flee at any time.

### Disengagement
- **Defensive Withdrawal:** Move Action to step 5 feet back without triggering opportunity attacks. Does not allow full move.
- **Run:** Full Move (double speed) in any direction. Triggers opportunity attacks from adjacent enemies.
- **Full Retreat:** Use both Standard and Move as a sprint (triple speed). Every enemy adjacent to any fleeing party member gets a free attack. Party exits the map and the encounter ends.

### Consequences of Fleeing
- The encounter is logged as fled; may have narrative consequences (NPCs comment, reputation effects)
- Enemies may pursue on the world map (if they have fast movement or mounts)
- Loot and XP from fled encounters are lost
- Some encounters cannot be fled (arena fights, certain story beats)
