# Dark Sun: Shattered Lands — Remake GDD
## 08: Survival Mechanics

**Version:** 0.2
**Last Updated:** 2026-04-20


> ⚠️ **DRAFT — Pending rewrite.** This file contains errors (game is set in **Draj under Tectuktitlay**, not Urik/Hamanu). Content not verified against source PDFs. See `GDD/MASTER_PROJECT_FILE.md` for the authoritative reference.
---

## Table of Contents
1. [Philosophy](#philosophy)
2. [Water](#water)
3. [Food](#food)
4. [Heat and Exposure](#heat-and-exposure)
5. [Encumbrance](#encumbrance)
6. [Wilderness Travel](#wilderness-travel)
7. [The Camp System](#the-camp-system)
8. [Environmental Hazards](#environmental-hazards)

---

## Philosophy

Survival on Athas is not a minigame — it is the texture of every decision. The original Shattered Lands had basic rations and water mechanics; the remake deepens these into a system where preparation and resource management determine whether the party reaches the next city-state or dies in the wastes between them.

Survival is never punitive for its own sake. Every resource constraint creates a decision. Every decision has a cost and an alternative. The player is never helpless — only planning matters.

---

## Water

Water is the most important resource on Athas. It is tracked per party member, not as a collective pool.

### Water Units
- 1 **Water Unit (WU)** = approximately 1 pint; enough for one character for one day of moderate activity
- Water is stored in waterskins, ceramic jugs, or kank nectary flasks
- Maximum carrying capacity: 10 WU per character (standard waterskin × 10)
- Kanks carry up to 30 WU in saddle bags

### Daily Water Consumption
| Condition | WU per Day |
|---|---|
| Rest / minimal activity | 1 |
| Normal wilderness travel | 2 |
| Heavy combat | +0.5 |
| Midday heat without shade | +1 |
| Peak heat without shade | +2 |
| Using Psychometabolism heavily | +0.5 |

### Water Deprivation
| Days Without Water | Effect |
|---|---|
| 0.5 (missed one day's full ration) | Thirsty: -1 to all Dex and Int checks |
| 1 | Dehydrated: -2 to all checks; speed -5 ft |
| 2 | Severely Dehydrated: -4 to all checks; speed halved; max HP -20% |
| 3 | Critical: Constitution save DC 15 each hour or take 1d6 damage |
| 4 | Death |

### Finding Water
| Method | Skill / Check | Water Gained |
|---|---|---|
| Oasis (discovered on map) | Automatic | 10–50 WU; refillable over time |
| Wyrmroot extraction | Survival DC 14 | 2d4 WU per plant |
| Kank nectary tap (owned kank) | Automatic | 1 WU per kank per day |
| Rainwater collection (rare event) | Automatic if prepared | 1d10 WU per hour |
| Dew collection (desert morning) | Survival DC 16 | 1d3 WU |
| Purify contaminated water | Cleric spell / Preserver ritual | Converts 1 gallon |
| City purchase | Gold | Market rate varies by scarcity |

### Water Economy in Cities
Water prices reflect the scarcity of each region:
| Location | Price per WU |
|---|---|
| Tyr (iron wealth, modest water) | 2 cp |
| Desh-Arak (near Deepwell) | 1 cp |
| Deep Wastes outpost | 10–25 cp |
| After a drought event | 3× normal |

---

## Food

Food is secondary to water but still tracked. Starvation is slower than dehydration but ultimately equally lethal.

### Food Units
- 1 **Food Unit (FU)** = one day's adequate nutrition
- Stored as dried meat (erdlu jerky), travel bread, or foraged plants
- Maximum carrying capacity: 15 FU per character
- Kanks carry up to 50 FU

### Daily Food Consumption
1 FU per character per day under normal conditions. Heavy combat burns +0.5 FU (exertion). Half-Giants require 3 FU per day.

### Food Deprivation
| Days Without Food | Effect |
|---|---|
| 1 | Hungry: -1 to STR and CON checks |
| 3 | Starving: -2 to all checks; Fatigued at end of each day |
| 6 | Wasting: -4 to all checks; speed -10 ft; max HP -10% per additional day |
| 10 | Death |

### Finding Food
| Method | Check | Food Gained |
|---|---|---|
| Hunt (appropriate terrain) | Survival DC 12–18 | 2d6 FU; takes 2 hours |
| Forage plants | Survival DC 14 | 1d4 FU |
| Erdlu herd encounter | No check; requires kill | 4d6 FU per erdlu |
| City purchase | Gold | 5 cp per FU standard |

---

## Heat and Exposure

### Heat Stages
See 01_setting.md for the full heat stage table. Summary:
- **Safe periods:** Dawn, Morning, Evening, Night
- **Dangerous:** Midday (+1 WU consumption; possible Scorched condition)
- **Lethal:** Peak hours (additional WU; Constitution saves vs heat damage)

### Mitigating Heat
| Method | Effect |
|---|---|
| Full shade (caves, buildings) | Negates all heat effects |
| Partial shade (large rocks, cloth canopy) | Reduces heat stage by 1 step |
| Wet cloth on skin | -1 heat damage; costs 0.5 extra WU |
| Elf or Mul (racial adaptation) | Immune to Scorched condition |
| Cleric of Water spell | Protect from Elements; negates heat for duration |
| Travel at night | No heat exposure; Cold Exposure risk in deep wastes instead |

### Cold Exposure (Night)
The deep wastes drop sharply at night. Characters without shelter or cold-weather gear:
- After 4 hours: Chilled (-1 to all DEX checks)
- After 8 hours: Hypothermic (-2 STR, -2 DEX; speed -5 ft)
- Fires negate cold exposure but attract predators and are visible for miles

### Desert Storms
Sandstorms are weather events that occur randomly on the wilderness map (or are scripted for dramatic effect).

| Storm Severity | Visibility | Combat Effect | Duration |
|---|---|---|---|
| Light dust | 60 ft | -1 to ranged attacks | 1d4 hours |
| Moderate | 20 ft | -3 to ranged; -1 melee; risk of separation | 2d6 hours |
| Heavy | 5 ft | Ranged impossible; -3 melee; Constitution save DC 12/hour or 1d4 damage | 1d3 days |

During a heavy storm: the party must shelter or take constant damage. Finding shelter requires Survival DC 15. Failure means the storm catches the party in the open.

---

## Encumbrance

Encumbrance limits how much each character can carry before movement and combat performance degrade.

### Carrying Capacity
- **Light Load:** ≤ STR × 10 lbs — no penalty
- **Medium Load:** ≤ STR × 20 lbs — speed -5 ft; -1 to DEX checks
- **Heavy Load:** ≤ STR × 30 lbs — speed -10 ft; -2 to DEX and STR checks; cannot run
- **Overloaded:** > STR × 30 lbs — speed 5 ft only; -4 to all checks; Fatigued after 1 hour

Half-Giants use STR × 50 lbs for carrying capacity (proportional to their size).

### Item Weights (Selected)
| Item | Weight |
|---|---|
| Waterskin (full, 10 WU) | 10 lbs |
| 5 days rations | 5 lbs |
| Obsidian short sword | 2 lbs |
| Bone spear | 5 lbs |
| Chitin breastplate | 20 lbs |
| Leather armor | 10 lbs |
| Standard pack (tent, bedroll, rope) | 15 lbs |
| Kank saddle bag | Kank carries; doesn't count against character |

### Encumbrance and Combat
Heavy encumbrance in combat:
- Cannot use Full Move or Charge
- Initiative penalty: -2
- Acrobatics checks at disadvantage

---

## Wilderness Travel

### The World Map
The map is node-based — locations are points connected by routes. Travel consumes time, water, and food based on the route's distance, terrain type, and the party's pace.

### Travel Rates
| Pace | Miles/Day | WU Cost Modifier | Notes |
|---|---|---|---|
| Slow | 15 | ×0.75 | Reduced exposure; +2 Survival checks |
| Normal | 24 | ×1 | Standard |
| Fast | 36 | ×1.5 | Fatigued after 3 days; no Survival bonus |
| Forced | 48 | ×2 | Exhausted after 1 day; serious injury risk |

Elves at any pace move 20% faster. Dwarves at any pace move 20% slower.

### Terrain Modifiers
| Terrain | Travel Time Multiplier | Survival DC |
|---|---|---|
| Road (maintained) | ×0.8 | 8 |
| Scrubland | ×1 | 10 |
| Badlands | ×1.3 | 12 |
| Sand desert | ×1.5 | 14 |
| Salt flat | ×1.7 | 16 |
| Mountains | ×2 | 15 |
| Silt margin | ×2 | 18 |

### Mounts
**Kanks:** Standard mount; speed bonus ×1.3; carry 30 WU + 50 FU extra; cannot navigate silt margin.
**Crodlu:** Fast riding mount; speed ×1.6; less carrying capacity; harder to manage (Handle Animal DC 14).
**Mekillot-drawn wagon:** Very slow (×0.7) but massive cargo capacity; requires 2 handlers; impassable in badlands.

### Random Encounters
Each travel segment has a chance of a random encounter based on terrain danger:
- Safe road: 5% per segment
- Scrubland: 15%
- Badlands: 25%
- Deep wastes: 40%

Encounters are drawn from regional tables (hostile / environmental / opportunity / lore). See 04_combat.md for combat that results.

---

## The Camp System

Whenever the party stops to rest, they enter the Camp interface.

### Camp Actions
Each party member can perform one Camp Action per rest period:
- **Sleep** (required for long rest HP recovery; also costs WU 0.5 extra vs staying awake)
- **Watch** (reduces ambush chance; Thri-Kreen can do this without sleeping)
- **Tend Wounds** (Healing check DC 12; target recovers +1 HP per die rolled if successful)
- **Cook** (converts raw food to rations; requires fire; improves food quality)
- **Repair Gear** (Craft check to remove one Crack from a weapon or patch armor)
- **Forage** (Survival check during rest; gain 1d4 FU or 1d2 WU)
- **Study** (Wizard: memorize an additional spell slot worth of spells; Psionicist: recover 5 extra PP)
- **Bond** (spend time with a specific companion; +5 to their Loyalty)

### Ambush During Camp
Each rest has an ambush chance based on:
- Terrain danger level (5–30%)
- Whether a watcher is posted (-10% per alert watcher)
- Whether a fire is lit (+10%)
- Whether the party took obvious action before camping (+5%)
- Thri-Kreen automatic watch: -15%

Ambush triggers an encounter at the start of the rest, with most party members starting in reduced-readiness state (some abilities on cooldown, armor may not be equipped).

### Camp Supplies
A **Camp Kit** allows a safe campsite to be established. Cost: 10 gp. Provides: basic shelter, fire setup, cooking equipment. Without a Camp Kit:
- Long rest in wilderness recovers only 50% max HP
- No Cook action available
- Ambush chance +10%

---

## Environmental Hazards

### Quicksilt
Found at the Silt Sea margins. Functions like quicksand but with silt — moving into it requires a Strength check DC 14 each round to avoid sinking deeper. Fully submerged characters take suffocation damage (1d6/round). Rope extraction requires Strength DC 16.

### Volcanic Vents (Iron Finger region)
Ground suddenly hot; 2d6 fire damage on contact with active vents. Identifiable with Survival DC 12.

### Toxic Plants
Several plant species are toxic. Identify with Nature DC 14. Eating unknowingly: Constitution save DC 12 or Poisoned for 1 hour.

### Flash Floods (Extremely Rare)
In ancient riverbeds after a distant rainfall (the player has no warning). 4d8 bludgeoning damage; Strength save DC 16 or knocked off feet and dragged 30 ft. Survival DC 18 to predict; Nature DC 15 to recognize signs in advance.

### Psionic Dead Zones
Areas where past traumatic events have left residual psychic impressions. Within a dead zone:
- Wild talents and Psionicist powers cost double PP
- All Will saves at -2
- Perception checks to notice unusual things are at advantage (the past "speaks")
- Sleeping in a dead zone triggers vivid nightmares; long rest recovers half HP

### The Obsidian Plains
The Obsidian Shelf (a natural glass plain) in the central wastes reflects the sun's heat. Any character spending time on the Shelf without foot protection takes 1d4 fire damage per hour from heat conducted through the ground. Vision is impaired by reflection (ranged attacks at -2 in direct sunlight hours). However, it is one of the few flat, clear surfaces on Athas — perfect for ambushes set by others.
