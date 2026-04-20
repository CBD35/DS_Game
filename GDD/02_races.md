# Dark Sun: Shattered Lands — Remake GDD
## 02: Races

**Version:** 0.2
**Last Updated:** 2026-04-20

---

## Overview

Seven races are playable — all canonical to the Dark Sun setting (AD&D 2e). Race affects base attributes, available classes, passive traits, and dialogue throughout the game. Some quests are accessible only to specific races; some NPC reactions are permanently set by race.

### Design Note: Faithfulness
All races match their canonical Dark Sun descriptions. Attribute modifiers follow the original AD&D 2e Dark Sun Player's Handbook with minor balance adjustments for the remake's d20-based system.

### Attribute Notation
- Base attributes rolled 3d6 (or point-buy option in remake)
- Racial modifiers apply after rolling
- Racial maximums listed where they differ from standard (18)

---

## 1. Human

**Lore:** Humans are the most common race in the Tablelands. They built most of the city-states, fill the Templar ranks, and dominate the arena circuits. Their lack of distinguishing physical traits is their strength — they fit anywhere, blend everywhere, and adapt to anything.

**Physical:** Enormous variation. Desert-adapted Athasians tend toward lean builds, darkened skin, and sun-weathered features. Average lifespan 70–80 years.

### Attribute Modifiers
No bonuses or penalties. Humans are the baseline.

### Racial Traits
- **Adaptable:** +1 to one attribute of player's choice at character creation
- **Bonus Proficiency:** One additional weapon or non-weapon proficiency at creation
- **Broadly Trusted:** +1 to initial Disposition with most NPCs (familiarity breeds tolerance)

### Class Access
All classes available. No restrictions.

### Wild Talent Chance
15%

---

## 2. Elf

**Lore:** Athasian elves are nothing like the forest-dwelling elves of other fantasy worlds. They are tall, lean, arrogant desert nomads who live in tribes, prize running above all other skills, and regard trust as something that must be earned over years — if at all. An elf who accepts you as kin will die for you. An elf who doesn't will rob you blind and feel no shame about it.

**Physical:** 6.5–7 feet tall, 150–175 lbs. Extremely lean. Bronze to dark brown skin. Angular features. Prominent ears. Lifespans of 110–120 years. Fastest runners on Athas — covering 80 miles per day is normal.

### Attribute Modifiers
| Attribute | Modifier | Racial Max |
|---|---|---|
| Strength | — | 17 |
| Dexterity | +2 | 20 |
| Constitution | -1 | 16 |
| Intelligence | +1 | 18 |
| Wisdom | — | 18 |
| Charisma | +1 | 18 |

### Racial Traits
- **Desert Run:** Movement 40 ft/round (vs 30 standard); wilderness travel time reduced 20%
- **Long-Sight:** Double normal visual range; no penalty on ranged attacks to normal range; half penalty at long range
- **Elven Distrust:** Elves begin with -2 Persuasion vs non-elves; non-elf party members suffer -1 Persuasion with elven NPCs unless vouched for
- **Tribal Memory:** Once per long rest, trance to recall geographical or historical knowledge (Wisdom check DC 10–18 by obscurity)
- **Heat Immunity:** Immune to Scorched condition; still requires normal water

### Class Access
All classes except Gladiator (cultural — elves do not perform for others' entertainment)

### Wild Talent Chance
20%

### Original Content Note
Elven tribe questlines were incomplete in the original game. The remake adds: **The Sandrunner Accord** — a full questline resolving the inter-tribal conflict only hinted at in Shattered Lands.

---

## 3. Dwarf

**Lore:** Athasian dwarves are defined not by their craft or their mountains but by their **Focus** — a single overriding life goal that gives them meaning. A dwarf without a Focus is considered broken. A dwarf who achieves their Focus immediately chooses a new one. They are not stubborn for stubbornness's sake; they are single-minded in a way that other races find baffling and, occasionally, terrifying.

**Physical:** 4.5–5 feet, 180–220 lbs. Completely hairless — no head hair, no beard, no body hair. This shocks non-athasians expecting traditional dwarves. Heavy builds. Tawny to dark brown skin. Lifespans of 250+ years.

### Attribute Modifiers
| Attribute | Modifier | Racial Max |
|---|---|---|
| Strength | +2 | 20 |
| Dexterity | -1 | 16 |
| Constitution | +2 | 20 |
| Intelligence | — | 18 |
| Wisdom | +1 | 18 |
| Charisma | -2 | 15 |

### Racial Traits
- **The Focus:** Player defines the Focus at character creation. While pursuing it: +2 to all relevant skill checks, +1 to attacks against targets directly impeding it. Achieving the Focus is a narrative event; player then chooses a new one.
- **Tunnel Vision:** -1 Persuasion on topics unrelated to the Focus
- **Death Before Failure:** If reduced to 0 HP while Focus incomplete: Constitution save DC 15 to remain at 1 HP (once per long rest)
- **Stonecunning:** Advantage on detecting hidden doors, structural weaknesses, underground navigation, mineral identification
- **Slow:** Base movement 25 ft/round

### Class Access
All classes except Bard and Psionicist (Dwarven biology resists psionic development)

### Wild Talent Chance
5% (lowest psionic affinity of any race)

---

## 4. Half-Elf

**Lore:** Half-elves exist in the worst of both worlds. Human society considers them outsiders; elven society considers them not-quite-kin, unable to keep pace in the desert run. They belong to no tribe, no community. Those who survive this social exile tend to be extraordinarily self-sufficient — and extraordinarily alone.

**Note on the original game:** Half-elves were listed in the original Shattered Lands but received minimal mechanical and narrative support. The remake fully realizes them.

**Physical:** 6–6.5 feet, lean. Features split between human and elven — angular but not extreme. Lifespans of 90–100 years.

### Attribute Modifiers
| Attribute | Modifier | Racial Max |
|---|---|---|
| Strength | — | 18 |
| Dexterity | +1 | 19 |
| Constitution | — | 17 |
| Intelligence | +1 | 18 |
| Wisdom | — | 18 |
| Charisma | — | 18 |

### Racial Traits
- **Outcast's Eye:** Half-elves have lived by reading people. +2 to Insight and Deception checks.
- **Between Worlds:** Neither fully trusted by elven NPCs nor fully comfortable in human society. Initial Disposition -1 with both elves and humans; however, this penalty can be overcome faster than other races (requires fewer positive interactions to reach Friendly)
- **Endurance:** Can march one additional hour per day before Fatigue sets in
- **Low-Light Vision:** Can see in dim light as if it were normal light

### Class Access
All classes available

### Wild Talent Chance
18%

### Original Content Note (Restored)
Half-elf companion **Raaen** — referenced in original design documents but cut before release — is fully implemented in the remake as an optional companion with a personal questline about identity and belonging.

---

## 5. Mul

**Lore:** Muls are the product of dwarf-human crossbreeding, engineered specifically for the gladiatorial arenas and heavy labor. They are the most valuable slaves on Athas — nearly tireless, enormously strong, and resistant to pain and heat. They are sterile. Most have known only the arena. Those who escape become some of the most dangerous individuals alive.

**Physical:** 6–6.5 feet, 180–220 lbs of muscle with minimal fat. Completely bald and hairless (like their dwarven parent). Skin tones grey-brown to dark bronze. Lifespans theoretically 100+ years, though arena mortality means few reach middle age.

### Attribute Modifiers
| Attribute | Modifier | Racial Max |
|---|---|---|
| Strength | +2 | 20 |
| Dexterity | — | 18 |
| Constitution | +2 | 20 |
| Intelligence | — | 16 |
| Wisdom | — | 16 |
| Charisma | -1 | 16 |

### Racial Traits
- **Tireless:** Immune to Fatigued condition from forced marching; Exhausted condition requires double the normal triggers
- **Pain Resistance:** Once per long rest — when reduced to 0 HP, Constitution save DC 12 + damage dealt to remain at 1 HP
- **Heat Adaptation:** Heat damage halved; no penalty during Midday heat stage
- **Arena-Bred:** Begin with proficiency in two weapons of choice regardless of class (reflects years of arena training)
- **Sterile:** No mechanical effect; significant narrative and dialogue weight throughout the game

### Class Access
Cannot be Wizard (Defiler or Preserver) or Psionicist. Optimal: Gladiator, Fighter, Ranger.

### Wild Talent Chance
5% (Mul hybrid biology suppresses psionic development)

---

## 6. Half-Giant

**Lore:** Half-Giants are not literally half giant — the term predates current knowledge of their origin. They are a distinct race, possibly the result of ancient magical experimentation, standing 10–12 feet tall. They are not stupid, though Athasian society treats them as if they are. They are deliberate, literal-minded, intensely loyal, and psychologically imitative — they naturally adopt the moral framework of whoever they spend most time with.

**Physical:** 10–12 feet tall, 900–1200 lbs. Proportioned like large humans. Skin in earth tones: clay, sandstone, grey-brown. Lifespans of 30–40 years (the body wears out).

### Attribute Modifiers
| Attribute | Modifier | Racial Max |
|---|---|---|
| Strength | +4 | 22 |
| Dexterity | -2 | 15 |
| Constitution | +2 | 20 |
| Intelligence | -2 | 14 |
| Wisdom | -1 | 15 |
| Charisma | — | 18 |

### Racial Traits
- **Massive:** Large creature; cannot enter Small spaces; requires double rations and water; standard mounts unusable
- **Devastating Blow:** Once per combat — single melee attack deals +2d10 damage; 50% chance to knock target Prone
- **Alignment Drift:** The Half-Giant absorbs the moral alignment of the party's dominant personality over time. This shifts their dialogue responses and some skill checks. Tracked on a separate UI indicator.
- **Intimidating Presence:** Enemies Medium or smaller must Wisdom save DC 13 or be Frightened for 1 round on first sight

### Class Access
Cannot be Thief, Bard, Wizard, or Psionicist. Optimal: Fighter, Gladiator.

### Wild Talent Chance
10%

---

## 7. Thri-Kreen

**Lore:** Insectoid desert hunters. Four arms, compound eyes, chitinous exoskeleton, and a biology so alien that most other races find them deeply unsettling. Thri-Kreen do not sleep. They communicate naturally through pheromone and gesture. They are profoundly loyal to those they accept as "clutch-kin" — and utterly indifferent to everyone else. Their culture centers on the hunt.

**Physical:** 6.5–7 feet, 200–250 lbs. Four arms (two primary, two secondary). Tan-yellow to grey-green chitin. Compound eyes. Mandibles. No external ears. 25–30 year lifespan.

### Attribute Modifiers
| Attribute | Modifier | Racial Max |
|---|---|---|
| Strength | +1 | 19 |
| Dexterity | +2 | 20 |
| Constitution | — | 18 |
| Intelligence | — | 18 |
| Wisdom | +1 | 18 |
| Charisma | -2 | 12 |

### Racial Traits
- **Four Arms:** Can wield up to 4 weapons; off-hand penalties reduced (-2 instead of -4); can hold shield in secondary hand while dual-wielding
- **Sleepless:** No sleep required; during camp, the Thri-Kreen watches, granting Advantage on ambush detection; recovers HP at short-rest rate rather than long-rest rate
- **Chitin Armor:** Natural AC 12 unarmored; armor only applies if it exceeds 12
- **Leaping Attack:** Once per combat — jump up to 15 feet as a free action before a melee attack; +2 to hit, +1d6 damage
- **Natural Telepathy:** Limited-range telepathy (30 ft) to communicate basic concepts with willing targets; cannot use spoken language effectively (clicks and chittering)
- **Pack Bond:** When an accepted party member drops to 0 HP: Rage-equivalent (+2 attacks, -2 AC) for 3 rounds

### Class Access
Cannot be Bard (cannot speak fluidly) or Wizard Defiler (cultural prohibition — defilement is anathema to Thri-Kreen). Optimal: Ranger, Fighter, Psionicist.

### Wild Talent Chance
30% (insectoid nervous system is naturally psionic-conductive)

---

## Race Comparison Table

| Race | STR | DEX | CON | INT | WIS | CHA | Psionic% | Restricted From |
|---|---|---|---|---|---|---|---|---|
| Human | — | — | — | — | — | — | 15% | Nothing |
| Elf | — | +2 | -1 | +1 | — | +1 | 20% | Gladiator |
| Dwarf | +2 | -1 | +2 | — | +1 | -2 | 5% | Bard, Psionicist |
| Half-Elf | — | +1 | — | +1 | — | — | 18% | Nothing |
| Mul | +2 | — | +2 | — | — | -1 | 5% | Wizard, Psionicist |
| Half-Giant | +4 | -2 | +2 | -2 | -1 | — | 10% | Thief, Bard, Wizard, Psionicist |
| Thri-Kreen | +1 | +2 | — | — | +1 | -2 | 30% | Bard, Wizard (Defiler) |

---

## Restored Content Note

The original Shattered Lands gave every race a functional but thin mechanical profile. The remake's additions:

- **Half-Elf** — fully realized with dedicated companion, questlines, and faction interactions (was nearly vestigial in original)
- **Thri-Kreen** — four-arm combat system fully implemented (original treated them as standard two-weapon fighters)
- **Half-Giant alignment drift** — implemented as a trackable character system (was described in flavor text only)
- All races receive race-specific dialogue throughout the full game (original had only a handful of race-specific lines)
