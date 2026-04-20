# Crimson Sands — Game Design Document
## 02: Races

**Version:** 0.1 (Pre-Production)
**Last Updated:** 2026-04-20

---

## Overview

Seven races are playable in Crimson Sands. All begin the game as gladiatorial slaves in Var-Khet. Race selection affects base attributes, available classes, passive traits, and dialogue options throughout the game.

Race is not cosmetic. A Half-Giant draws different reactions than an Elf from every major faction. Some quests are only accessible to specific races. Some dialogue options are permanently locked or unlocked based on race.

### Attribute Notation
- Attributes range 3–18 at character creation (before racial modifiers)
- Racial modifiers are listed as bonuses/penalties to the standard 3d6 spread
- Maximum racial cap overrides class cap where applicable

---

## 1. Human

**Lore:** The most numerous and politically dominant race. Humans built the city-states, humans run the Templar networks, and humans fill the arenas. Their adaptability is their greatest strength — and their capacity for cruelty is their greatest flaw.

**Physical:** Range widely. Desert-adapted humans trend toward lean builds, darker skin, and sun-weathered features. Average lifespan 60–70 years.

### Attribute Modifiers
| Attribute | Modifier |
|---|---|
| Strength | — |
| Dexterity | — |
| Constitution | — |
| Intelligence | — |
| Wisdom | — |
| Charisma | +1 |

### Racial Traits
- **Adaptable:** At character creation, gain +1 to any one attribute of player's choice.
- **Widely Trusted:** +2 to all Persuasion checks with non-hostile NPCs (they've seen humans before).
- **No Special Resistances:** Humans have no innate elemental or psionic resistances.
- **Bonus Proficiency:** Humans begin with one additional weapon or skill proficiency.

### Class Restrictions
None. Humans can access all 8 classes and all multi-class combinations.

### Starting Wild Talent Chance
15% (see 05_psionics.md)

### Faction Notes
- Templars are predominantly human; human players receive less initial suspicion from Templar encounters
- Veiled Alliance treats humans as the primary oppressor class; rapport must be earned
- Merchant Houses favor human negotiators; +1 to all trade interactions

---

## 2. Mul

**Lore:** The offspring of human and dwarf parents, Muls are sterile hybrids bred specifically for the gladiatorial arena and heavy labor. They are the most prized slaves on Kharak'thal — virtually tireless, enormously strong, and resistant to both heat and pain. Most Muls have never known freedom. Those who escape tend to become the most dangerous individuals alive.

**Physical:** 6–6.5 feet tall, barrel-chested, almost entirely hairless, skin ranging from grey-brown to dark bronze. No body hair. Typically 150–200 lbs of muscle with almost no fat. Lifespan 40–50 years (arena mortality is the primary cause; healthy Muls can reach 80).

### Attribute Modifiers
| Attribute | Modifier |
|---|---|
| Strength | +2 (max 20) |
| Dexterity | — |
| Constitution | +2 (max 20) |
| Intelligence | — |
| Wisdom | — |
| Charisma | -1 |

### Racial Traits
- **Tireless:** Muls do not suffer the Fatigued condition from forced marching. Exhausted condition requires double the normal trigger conditions.
- **Pain Resistance:** When reduced to 0 HP, Mul may make a Constitution save (DC 12 + damage dealt in the blow) to remain at 1 HP instead. Usable once per long rest.
- **Heat Adaptation:** Heat exposure deals half damage. No penalty during Midday heat stage.
- **Bred for the Arena:** Muls begin with proficiency in two weapons of choice (reflecting arena training) regardless of class.
- **Sterile:** No mechanical effect; significant narrative and dialogue weight.

### Class Restrictions
- **Cannot be:** Wizard (Defiler or Preserver), Psionicist
- **Optimal Classes:** Gladiator, Fighter, Ranger

### Starting Wild Talent Chance
5% (Mul biology suppresses psionic development)

### Faction Notes
- Arena crowd loves Mul fighters; reputation gains doubled in arena contexts
- Templars view escaped Muls as high-priority recapture targets (+2 to Templar hostility)
- Other slaves relate strongly to Muls; automatic positive disposition with slave NPCs

---

## 3. Half-Giant

**Lore:** Half-Giants are not literally half giant — the name is ancient and inaccurate. They are a distinct race, product of magical experimentation in the early Crimson Age, standing 10–12 feet tall and weighing half a ton. They are not stupid, though the world treats them that way. They are deliberate, literal-minded, and loyal to a fault. Their size makes them invaluable as soldiers and laborers; their psychology makes them susceptible to following whoever seems most confident.

**Physical:** 10–12 feet, 900–1200 lbs. Proportioned like a large human, not grotesquely exaggerated. Skin tones in earth tones: clay brown, sandstone, grey. Lifespans of 30–40 years (body wears out fast).

### Attribute Modifiers
| Attribute | Modifier |
|---|---|
| Strength | +4 (max 22) |
| Dexterity | -2 |
| Constitution | +2 (max 20) |
| Intelligence | -2 |
| Wisdom | -1 |
| Charisma | — |

### Racial Traits
- **Massive:** Half-Giants are Large creatures. They cannot enter Small spaces, cannot use standard mounts, and require double rations and water.
- **Devastating Blow:** Once per combat, may make a single melee attack that deals an additional 2d10 damage and has a 50% chance to knock the target Prone.
- **Copycat Psychology:** If a Half-Giant observes another party member perform a specific action type (e.g., attacking with a sword, using a psionic power, casting a spell) three times in a row, they gain the ability to attempt that action at -4 proficiency for the remainder of the encounter. Represents their imitative learning.
- **Intimidating Presence:** Enemies of Medium size or smaller must succeed on a Wisdom save (DC 13) or be Frightened for 1 round upon first seeing the Half-Giant in combat.

### Class Restrictions
- **Cannot be:** Thief, Bard, Wizard (either), Psionicist
- **Optimal Classes:** Fighter, Gladiator, Ranger (wilderness variant)

### Starting Wild Talent Chance
10%

### Special Mechanics
- Half-Giant characters have a unique UI panel showing their **Alignment Drift** — they naturally absorb the alignment/moral stance of whoever they spend most time with. This is tracked over time and can shift their personality responses in dialogue.

---

## 4. Thri-Kreen

**Lore:** Insectoid humanoids native to the deep wastes. Four arms, compound eyes, chitinous exoskeleton, and a biology so alien that most other races find them unsettling. Thri-Kreen do not sleep. They hunt. They think in terms of pack hierarchy and prey/not-prey. They can join civilized society — some have lived in cities for decades — but the instinct never fully leaves. They are profoundly loyal to those they accept as "pack."

**Physical:** 6.5–7 feet, 200–250 lbs. Tan-yellow to grey-green chitin. Four arms (two primary, two secondary). Mandibles. Compound eyes (180-degree vision arc). No hair. Lifespan 25–30 years.

### Attribute Modifiers
| Attribute | Modifier |
|---|---|
| Strength | +1 |
| Dexterity | +2 (max 20) |
| Constitution | — |
| Intelligence | — |
| Wisdom | +1 |
| Charisma | -2 |

### Racial Traits
- **Four Arms:** Can wield up to 4 weapons simultaneously (two primary, two off-hand). Off-hand attacks at -2 rather than standard -4. Can also hold a shield in one secondary hand while wielding two weapons.
- **Sleepless:** Thri-Kreen do not require sleep. During camp phases, they remain on watch, granting the party Advantage on ambush detection rolls. They do not benefit from long rest HP recovery (instead recover HP at the rate of a short rest; their biology repairs differently).
- **Chitin Armor:** Natural AC 12 when unarmored. Wearing armor over chitin is mechanically awkward; armor AC only applies if it exceeds 12.
- **Leaping Attack:** Once per combat encounter, may make a jump attack (up to 15 feet) as a free action before a melee attack, gaining +2 to hit and +1d6 damage.
- **Telepathic Mute:** Thri-Kreen communicate naturally through pheromone and gesture. They can learn spoken languages but their voices are unpleasant (chittering, clicks). They have natural limited-range telepathy (30 feet) usable to communicate basic concepts with willing targets.
- **Pack Bond:** When an accepted pack member drops to 0 HP, Thri-Kreen enters a Rage-equivalent state (+2 to all attacks, -2 AC) for 3 rounds.

### Class Restrictions
- **Cannot be:** Bard, Wizard (Defiler) — Thri-Kreen have deep psionic culture; defiling is anathema
- **Optimal Classes:** Ranger, Fighter, Psionicist

### Starting Wild Talent Chance
30% (insectoid nervous system is naturally psionic-conductive)

---

## 5. Elf

**Lore:** Kharak'thal's Elves bear no resemblance to the forest-dwelling, immortal elves of other fantasy settings. They are desert nomads: tall, lean, arrogant, and fast. They live in tribes that war with each other as readily as with outsiders. They prize speed and endurance — the ability to run 80 miles in a day is the core of their culture. They distrust non-elves on principle and each other on experience. They are not evil; they are alien to the concepts of trust and community that other races take for granted.

**Physical:** 6.5–7 feet, lean (140–180 lbs). Bronze to dark brown skin. Angular features. Prominent ears. Extraordinary long-distance vision. Lifespan 100–120 years.

### Attribute Modifiers
| Attribute | Modifier |
|---|---|
| Strength | — |
| Dexterity | +2 (max 20) |
| Constitution | -1 |
| Intelligence | +1 |
| Wisdom | — |
| Charisma | +1 |

### Racial Traits
- **Desert Run:** Elves move at 40 feet per round (vs 30 standard). On wilderness travel, they reduce travel time by 20% when the party can match their pace.
- **Long-Sight:** Elves can identify targets and read text at twice the normal distance. No penalty on ranged attacks beyond normal range; reduced penalty at extreme range.
- **Elven Distrust:** Elves take a -2 penalty on initial Persuasion checks with non-elves. Non-elf party members suffer -1 to Persuasion with elven NPCs unless an elf vouches for them.
- **Tribe Memory:** Elves have a racial memory system. Once per long rest, may enter a trance and attempt to recall a piece of historical or geographical information (Wisdom check DC 10–18 depending on obscurity). Represents oral tradition passed down through generations.
- **Heat Immune:** Desert-adapted; immune to Scorched condition. Still requires normal water.

### Class Restrictions
- **Cannot be:** Gladiator (cultural; elves do not perform for others)
- **Optimal Classes:** Ranger, Thief, Bard, Wizard (Preserver preferred — defilement violates their connection to the land)

### Starting Wild Talent Chance
20%

### Faction Notes
- Elven clan affiliation persists through the game; different clans have different reputations with city-states
- Veiled Alliance has significant elven membership; elf players start with +2 initial reputation with the Alliance

---

## 6. Dwarf

**Lore:** Kharak'thal's Dwarves are shorter and stockier than their traditional fantasy counterparts, but the most defining trait is psychological: Dwarves choose a single **Focus** — a life goal — and dedicate themselves to it utterly. A Dwarf without a Focus is considered broken, pitiful, barely alive. A Dwarf who achieves their Focus immediately chooses a new one. They are not stubborn; they are single-minded in a way that other races find baffling and occasionally terrifying.

**Physical:** 4.5–5 feet, 180–220 lbs. Heavily built. Bald (all Dwarves are hairless). Sun-weathered skin. Lifespan 200+ years.

### Attribute Modifiers
| Attribute | Modifier |
|---|---|
| Strength | +1 |
| Dexterity | -1 |
| Constitution | +2 (max 20) |
| Intelligence | +1 |
| Wisdom | +1 |
| Charisma | -1 |

### Racial Traits
- **The Focus:** At character creation, player defines their Dwarf's current Focus (a specific achievable goal; examples: "Free the slaves of Var-Khet," "Kill the Templar who murdered my clan," "Acquire enough water rights to sustain my people"). While actively pursuing the Focus, the character gains +2 to all relevant skill checks and +1 to attack rolls against targets directly impeding the Focus. When the Focus is achieved, the player chooses a new one.
- **Tunnel Vision:** While the Focus is active, the Dwarf takes -1 to Persuasion checks on topics unrelated to the Focus (they don't hide their disinterest).
- **Death Before Failure:** If a Dwarf character would die while their Focus is incomplete, they may make a Constitution save (DC 15) to survive at 1 HP. If they succeed, they gain the Determined condition (+2 to all saves) for 24 in-game hours.
- **Stonecunning:** Advantage on checks to detect hidden doors, structural weaknesses, underground navigation, and mineral identification.
- **Slow:** Base movement 25 feet (vs 30 standard).

### Class Restrictions
- **Cannot be:** Bard, Psionicist (Dwarf biology is notoriously psionic-resistant)
- **Optimal Classes:** Fighter, Cleric (Earth), Thief (rare; the occasional Dwarf with Focus on "perfect theft")

### Starting Wild Talent Chance
5% (lowest of any race)

---

## 7. Ssurrai (Original Race)

**Lore:** The Ssurrai appeared in the deep wastes roughly 300 years ago — no records exist of them before that date. They are humanoid but clearly not mammalian: scales over pale skin, vertically-slit pupils, and a low-level psionic field that makes them subtly unpleasant to be near. Where they came from is unknown. Theories range from magical experimentation to extraplanar origin to simple evolution in isolation. The Ssurrai do not discuss it. What is known: they survive where nothing else does, they have perfect memory, and they are deeply curious about the world's death — as though they have seen it before.

**Physical:** 5.5–6 feet, 140–170 lbs. Humanoid posture and limb arrangement. Scales range from pale grey to deep green-black; color changes slightly with emotional state. Vertical pupils, flickering forked tongue, no external ears. Lifespan unknown — oldest confirmed Ssurrai is 400 years old and shows no aging.

### Attribute Modifiers
| Attribute | Modifier |
|---|---|
| Strength | -1 |
| Dexterity | +1 |
| Constitution | +1 |
| Intelligence | +2 (max 20) |
| Wisdom | +1 |
| Charisma | -2 |

### Racial Traits
- **Perfect Memory:** Ssurrai remember everything they have directly witnessed. Mechanically: automatic success on all Recall checks; gain an additional entry in the Codex for any area or NPC they interact with directly.
- **Psionic Field:** The Ssurrai's passive psionic field unsettles others. All non-allied NPCs begin with -1 to initial Disposition. However, this field also makes the Ssurrai a natural psionic amplifier: when adjacent to an ally using a psionic power, that ally gains +1 to the psionic attack/save DC.
- **Thermal Sense:** Ssurrai detect heat signatures up to 60 feet in darkness or obscurement. Invisible creatures with body heat are visible as dim outlines.
- **Scale Resistance:** Natural resistance to fire and heat damage (reduce by 3 points per instance). No benefit vs cold.
- **Ageless:** Ssurrai do not age mechanically. They are immune to magical aging effects.
- **Uncanny:** Animals and less-intelligent creatures react with fear to Ssurrai. Hostile animals must make a Wisdom save (DC 12) or hesitate before attacking a Ssurrai. Domestic animals refuse to approach.

### Class Restrictions
- **Cannot be:** Gladiator (too visually alien; crowd hostility makes it unviable as a career), Cleric (Ssurrai have no elemental affinity and cannot access elemental power)
- **Optimal Classes:** Psionicist, Wizard (Preserver), Thief, Ranger

### Starting Wild Talent Chance
40% (highest of any race; psionic field suggests deep psionic biology)

### Narrative Weight
The Ssurrai's origin is a major late-game revelation. Playing as a Ssurrai unlocks a personal quest line in Act 3 that reveals the true nature of their appearance 300 years ago — and their connection to the event that is now accelerating the world's death.

---

## Race Comparison Table

| Race | STR | DEX | CON | INT | WIS | CHA | Psionic% | Best Classes |
|---|---|---|---|---|---|---|---|---|
| Human | +0 | +0 | +0 | +0 | +0 | +1 | 15% | Any |
| Mul | +2 | +0 | +2 | +0 | +0 | -1 | 5% | Fighter, Gladiator |
| Half-Giant | +4 | -2 | +2 | -2 | -1 | +0 | 10% | Fighter, Gladiator |
| Thri-Kreen | +1 | +2 | +0 | +0 | +1 | -2 | 30% | Ranger, Psionicist |
| Elf | +0 | +2 | -1 | +1 | +0 | +1 | 20% | Ranger, Thief, Bard |
| Dwarf | +1 | -1 | +2 | +1 | +1 | -1 | 5% | Fighter, Cleric |
| Ssurrai | -1 | +1 | +1 | +2 | +1 | -2 | 40% | Psionicist, Wizard |
