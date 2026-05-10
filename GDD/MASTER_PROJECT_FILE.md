# DARK SUN: SHATTERED LANDS REBORN
## Master Project File — Complete Edition
### For Claude Code | Engine: Godot 4 | Version 1.0

---

> *"The same sun. The same chains. One chance to break them."*

---

## CRITICAL PRODUCTION NOTE

This document is grounded in the **actual 1993 SSI game manuals and cluebook**. Previous GDD versions (v0.1, v0.2) contained a significant error — the game is set in **DRAJ** under the Sorcerer-King **TECTUKTITLAY**, not Urik/Hamanu. Every production decision must reflect this.

**Source documents used to build this file:**
- `ds_shatterland_manual_pdf.pdf` — 1993 SSI rule book (49 pages, Acrobat Distiller 1995)
- `ds_shatterland_cluebook_pdf.PDF` — Official SSI cluebook (65 pages, 1996)

**The source documents live in Google Drive at `Game Design/DS/`.** All developers should read them before working on any chapter.

**Status of older GDD files in this folder (`00_overview.md` through `11_technical.md`):**
Those v0.2 documents contain the Hamanu/Urik error and other inconsistencies. They are **superseded by this Master Project File**. Treat them as historical reference only until they are rewritten in Phase 1.

---

## TABLE OF CONTENTS

1. Vision & Philosophy
2. The FFVII Remake Model Applied
3. The Original Game — Verified Story Bible
4. Original Game — All Locations (from Cluebook)
5. Original Game — Character Roster (from Manual & Jareth's Journal)
6. Original Game — Races & Classes (from Manual)
7. Original Game — Combat & Mechanics (from Manual)
8. Original Game — Spells & Psionics (from Manual)
9. Original Game — Bestiary (from Manual & Cluebook)
10. Remake Story — The Three-Layer System
11. Remake Chapters — Original Story Rebuilt
12. Remake Chapters — New Story (Chapters 6–8)
13. Character Roster — Original + New
14. Companion System
15. Faction System
16. Combat System (Modernized)
17. Psionic System (Expanded)
18. World & Exploration
19. Resource Systems
20. Art Direction
21. Audio Direction
22. Technical Specification — Godot 4
23. Development Roadmap
24. Key Story Questions
25. First Steps for Claude Code

---

# SECTION 1: VISION & PHILOSOPHY

## What This Game Is

A faithful fan rebuild of the 1993 SSI RPG *Dark Sun: Shattered Lands*, in Godot 4. Every major original story beat is preserved. Everything is expanded. New content is woven in organically. Three new chapters extend the story beyond the original ending.

## The Three-Layer System

Every piece of content is tagged:
- **[ORIGINAL]** — From the 1993 game. Preserve faithfully.
- **[EXPANDED]** — Original content deepened. Same destination, more road.
- **[NEW]** — New content alongside, never replacing.

## The FFVII Remake Contract

- Every original story beat plays out as remembered
- Every original character appears and functions as in the source
- New characters and threads emerge from the existing world, not a parallel one
- Players who know the original recognize it immediately
- The new story (Chapters 6–8) begins exactly where the original ends

## Core Design Pillars

1. **Faithful to the original** — Draj, Tectuktitlay, the Arena, Semyon, Scar. These are sacred.
2. **Every choice has weight** — Story flags echo across chapters.
3. **Athas is hostile** — Water, heat, weapon degradation, scarcity. The world kills.
4. **Tactical depth without bloat** — Meaningful combat, not endless systems.
5. **The original team's vision, completed** — What the 1993 game was trying to be.

---

# SECTION 2: THE ORIGINAL GAME — VERIFIED STORY BIBLE

*This section is extracted directly from the 1993 manual and cluebook. It supersedes all earlier GDD story assumptions.*

## Setting

**City-state: DRAJ**
**Sorcerer-King: TECTUKTITLAY** (not Hamanu/Urik — previous GDD error corrected)
**Geography: The Tablelands east of Draj, extending to the Silt Sea**

From the manual: *"SHATTERED LANDS takes place in and around the city-state of Draj, ruled by the sorcerer-king Tectuktitlay."*

From the manual's world description: *"Athas, the world of Dark Sun, was once as pleasant as any other. But, after many thousands of years, powerful mages found ways to gain power through draining the planet's vitality. At their zenith, these wizards caused the sun to transform from a pleasant yellow glow to a raging crimson fireball on the horizon. The seas evaporated and were replaced by huge basins of silt. Mines played out, rendering metal extremely rare and valuable."*

## Jareth's Journal — Character Backstories (from Manual, pp. 3–4)

Jareth is a bard condemned to the arena who observes the other slaves. His journal is the player's introduction to the party:

**GARETH (SELUCUS)** — Half-giant gladiator, favorite of Tectuktitlay. Won many matches for the noble house of Tehuactl. Had a misguided loyalty to his master. When a templar suggested he lose a match, Gareth broke the templar's neck. His master declared this an escape attempt and condemned him to die in the royal slave pens. He is still not bitter and seeks wisdom and freedom.

**SARIA (SADIRA)** — Offspring of a foolish human slave girl and a roguish elven caravan master. Her father left before she was born. She spent her youth stealing to survive. Before this life could wear her down, she was caught picking a preserver's pocket. He took her east, near the volcano, trained her in elemental spirits (cleric spells), and in the preserver's dangerous art. A slaver band captured her and killed her benefactor. At the auction block, she used her spells to slay a templar. Now she lives in the pens.

**TARIM** — Thri-kreen female, a bizarre prisoner. She had been hunting city troops on the salt flats west of Draj when she was trapped by a powerful templar. Rather than kill her outright, the templar sent her to the arena so her death could entertain the masses. While she doesn't mind the fight, she misses the hunt and the freedom of the wasteland.

*Note: Manual names and Jareth's observations may differ from in-game names. Verify against actual game before locking character names in production.*

## Overview Story Arc

The party begins as gladiators in **King Tectuktitlay's Arena** in **Draj**. They must:

1. **Arena** — Survive gladiatorial fights, find allies, escape
2. **Slave Pens** — Navigate the pens, form escape alliances with Scar or Merzol
3. **Sewers** — Navigate beneath Draj, deal with the Tari and disgraced templar Mikquetzl
4. **Dagolar's Tunnels** — Confront the evil psionicist Dagolar
5. **Fields & Wasteland** — Escape into the open desert around Draj
6. **Free Villages** — Reach and ally with Teaquetzl, Cedrilte, and Gedron villages
7. **Palace Ruins (Korbnor)** — Retrieve the Genie Bottle from the buried city
8. **Final Battle** — Face Kraxis, the Drajian commander, and Draj's army
9. **Epilogue** — Victory or defeat in the war against Draj's oppression

---

# SECTION 3: ORIGINAL GAME — ALL LOCATIONS (Cluebook)

*Complete location list from the official cluebook, in story order. Maps exist in the original game. All locations must be recreated for the remake.*

## Underground / City Regions (Early Game)

### ARENA
Draj's gladiatorial arena. Red brick walls, sand floor, surrounded by crowds. Party battles various monsters per the sorcerer-king's entertainment. Key NPCs: **Announcer** (controls fights, heckles gladiators), **Semyon** (former gladiator staked out, needs water), **Venyz** (second staked slave, beyond help).

Combat monsters include: bulettes, daggorans, defilers, dune reapers, fire eels, thri-kreen, mastyrials, mountain stalkers, otyughs, renegade halflings, sand howlers, screamer beetles, silt runners, red slaad, half-giants, sligs, strines, tohr-kreen, wild muls, xorns, and rampagers.

**Key mechanic:** Party must fight in the Arena a minimum number of times (5 for Scar's alliance, 3 for Merzol's) before escape is possible. A corner at location 1 is safe for vulnerable characters during large monster fights.

**Escape path:** West exit from the Arena leads to the tunnel escape route once Scar has agreed to flee.

### SLAVE PENS
Maze of brown brick rooms. Big fountain to the south. Gladiator pens to east, monster pens to west. Kitchen in northwest. Templar Pehtucl's room in southwest. Key NPCs:

- **Scar** — "King of the Pens." Captured to please Tectuktitlay. Will escape after 5 Arena visits. His plan: escape through the Arena's west exit.
- **Merzol** — Would-be king, less organized. Escapes after 3 Arena visits. More risky plan.
- **Trustee** — Old gladiator who can't fight, does odd jobs. Former wilderness guide. Lets party see Dinos.
- **Dinos** — Slave cook. Was arrested for accidentally feeding bad food to a templar. Can heal Gilal.
- **Mirlon** — Vain gladiator, bribed by Templar Pehtucl to betray escapees. Claims rich family.
- **Gilal** — Gladiator who tried to escape, paid with her memory. Can't think of escape without head pain. Dinos can heal her; she'll then explain how she escaped.
- **Templar Pehtucl** — In charge of the pens. Offers fake escape, leads to ambush. Has sword Bloodwrath (+1) on his body.
- **Kurzak** — Main guard. Takes bribes but gives nothing. Lets Mirlon through.
- **Bonecrusher** — Half-giant monster trainer. Sent to retrieve party if they delay too long.

**Key items:** Water pot (location 6, fill at Dinos' sink), Bloodwrath sword on Pehtucl's body, arrows+3/gem/scale armor in secret room (location 4), steel axe in armory (location 17), polearms in armory.

**Escape routes:** Through Arena with Scar or Merzol (location 1/20), sewer grate at location 12 (thief can pick lock, others can hack/rip open).

### SEWERS
Maze of tunnels beneath Draj. Northern flushing tunnels empty into fields. Southern tunnels have flood-control gates. Inhabited by Tari (rat-people). Tyrian slimes and sligs common. Key NPCs:

- **Low Warren Thugs** — Churrr's henchmen. Easily intimidated. Know about the high warren chief's daughter.
- **Churrr** — Beady-eyed controller of low warrens. Jealous, weak. Kidnapped chief's daughter for Mikquetzl. Buys bags of grain, trades leather armor.
- **High Warren Guards** — Tari warriors. Distrustful. Will lead party to chief if trust is earned.
- **High Warren Chief** — Bold and intelligent (for a ratman). Devastated by kidnapped daughter. Has Helm of Contemplation to give as reward.
- **Skull Guardians** — Tari transformed by Dagolar. Protect the Elders. Can give party bone crank.
- **Elders** — Animated skulls of past tari leaders. Haughty. Grant permission to take Staff of Parting. Tell party how to reach Dagolar's Tunnels.
- **Mikquetzl** — Disgraced templar of Tectuktitlay. Insane. Rules tari worshippers. Plans to build fanatical army to regain Tectuktitlay's favor. Had the chief's daughter kidnapped for sacrifice. Has Chameleon Gloves.
- **High Warren Chief's Daughter** — Kidnapped, plucky. Rushes into battle even when weakened.

**Key items:** Staff of Parting (drain collection pond to reveal Dagolar's Tunnels entrance), Helm of Contemplation (from chief), Chameleon Gloves (on Mikquetzl), steel sword/gem/Mikquetzl's notes (in chest at location 20), steel axe+1 (in sewer hole), scroll of enlarge, scroll of color spray.

**Escape to fields:** Secret exit (Elders explain how). Collection pond drained with Staff of Parting reveals Dagolar's Tunnels entrance.

### DAGOLAR'S TUNNELS
Experiments performed in hidden tunnels. Dagolar is a **20th-level human psionicist** who has been twisting creatures and people. Key NPCs:

- **Dagolar** — Evil psionicist, creator of the Dagolar slimes. His experiments are the source of the twisted creatures found throughout the game. Location varies.
- **Keldar** — Dagolar's servant, warped by proximity to twisted creations. Keeps a book of names of all people Dagolar has killed. If killed in one shot, doesn't teleport to next location.
- **Goburnix** — Dagolar's brother, turned into a zombie. Originally led a different life from his cruel brother. Follows party if freed. Can expose Jake or Mow as Dagolar if one is waiting outside.

## Wasteland Regions (Mid-Game)

### FIELDS
Sandy wastes between Draj and the free villages. Drajian patrols. Old One-eye (NPC in region).

### WHITE SANDS
Sandy waste between Fields and Teaquetzl. Where the party fights Drajian army waves:
- Final Battle #1 and #2 — Drajian troops
- Final Battle #3 — Kraxis the Drajian commander and elite forces

NPCs: **Egrus** — stays near camp unless party reads scroll on nearby body.

### TEAQUETZL VILLAGE
Free village in the middle of sandy wastes. Founded by escaped slaves. A **visionary's prophecy** of destruction is the central rallying point for the alliance. Key NPCs:

- **Chahl** — Leader of Teaquetzl. Has adopted daughter Katura.
- **Katura** — Chahl's adopted daughter. Fascinated by magical items. Visits the Elven Caravan.
- **Visionary** — Halfling found half-dead in the desert. His prophecy of the slave villages' destruction drives the alliance-building arc.
- **Father Garyn** — Cleric of water. Tends villagers' spiritual needs. Was injured escaping slavery.
- **Village Council** — Provides latest news on Drajian army. Asks party to gather allies after defeating the army.
- **Weapon merchant** — Sells melee weapons if party agrees to seek allies.

**Key mechanic: Alliance building.** Teaquetzl needs Cedrilte and Gedron to ally before the final battle is survivable. The visionary's prophecy provides the reason, but the party must do the diplomatic legwork.

**Key items/events:** Obelisk (teleport device — place correct gem to activate), Father Garyn needs bag of pith from Notaku at Red Sands Plateau, meteorite metal at location 20 can be made into metal axe+1. A sandstorm event caused by the Genie reveals the Palace Ruins.

### NAZCA LINES
Sandy wasteland. Toonuu sells salt here (needed to buy mastyrial Alita from Demothi at Red Sands Plateau).

### CEDRILTE VILLAGE
Free village. Strangers are mistrusted. Won't join alliance against Draj unless all threats to the village are resolved. Has NPCs Krikor and Chaya (speak to Chaya first before being led to key location).

### UNDERMOUNTAIN
Subterranean region. Can be reached by climbing wells in Cedrilte, Gedron, or Teaquetzl, or using rope on bridge in Wagon Train region. Home of the Undermountain Folk (Mindhome) — small telepathically-linked humanoids.

### LOWER CASTLE
Castle region. Wyvern riders operate from here, raiding the Elven Caravan.

### UPPER CASTLE
Upper levels of the castle.

### SALT OASIS
Salt flats with springs. A templar is mining for copper with slave labor. Key NPCs: Kasha (escaped slave, warning), Uzoma (Drajian guard patrol leader who mistakes party for guards). Using the Wand of Metal Detection (from sage at Red Sands Plateau) on the templar convinces him to leave.

### HOT SPRINGS
Salt flat springs being mined for copper by a Drajian templar. Teaquetzl patrols the area. Can follow Drajian patrol to encounter Teaquetzl patrol.

### GEDRON VILLAGE
Taken over by evil defiler **Wyrmias** who controls villagers' minds. Wyrmias needs two statue pieces (head and rattle for a serpentine statue). Key NPCs:

- **Wyrmias** — Defiler controlling the village. Man of his word — if given both statue pieces, releases the village and challenges party to a duel. Teleports villagers into silt if party attacks or insults him after warning.
- **Linara** — 6th-level human preserver, unaffected by Wyrmias. Waiting to hear from her sister.
- **Gedron Mayor** — Wyrmias' puppet. Agrees to alliance after village is freed.
- **Melkor** — Travelling merchant stuck in the village.

**Key items:** Hidden safe under rug in Wyrmias' room (requires high INT or thief to find) contains: 2,000 ceramic pieces, sword El's Drinker, psionic bracelet of life draining, obelisk gem. Jasmine's spellbook gives information about Wyrmias' room.

## Far Wasteland Regions

### SILT SEA SSURRANS
Isthmus into the Silt Sea. Ssurran slave traders have one of the two statue pieces Wyrmias needs. Can buy (expensive) or take by force.

### SILT SEA SUMMONING
**Jasmine** — 9th-level human preserver. Came to retrieve a statue piece for Wyrmias. Dakaren and magera were an obstacle. Her spellbook (findable here or in Gedron) contains information about Wyrmias' room.

Also: **Arant** holds captured gladiators from Gedron and Cedrilte. Has the second statue piece (Wyrmias needs). The ssurran merchants are waiting to buy the captured gladiators from Arant.

### CAPTURED GLADIATORS
Gladiators from Gedron and Cedrilte have been captured by Arant and his men. Freeing them (and killing Arant) is required for the villages to reach full alliance strength. The ssurrans at Silt Sea Ssurrans are waiting to buy these gladiators.

### PALACE RUINS (KORBNOR)
**The most critical mid-late game location.** Korbnor was once a beautiful city buried in a sandstorm after an advisor named Cragg (a greater shadow) wished the Genie to contain the evil of the court. The psurlons who were summoned to give knowledge demanded the Genie and were buried with the city.

Key NPCs:
- **Cragg** — Greater shadow and former advisor. Killed the king. Mortally wounded, wished the evil contained. Has been buried ever since. Has the Genie bottle. Can be given his body back to rest in peace.
- **King Dwyer** — Spirit of the former king. On the dais. Stepping on the dais angers him.
- **Genie** — Grants three wishes. If you wish for help defeating Draj (and didn't kill Cragg), wish is granted + Quicksilver Glove. Can teleport party out of ruins. Can heal and resurrect party members. Prevents Drajian forces from summoning aid in final battles. Calls shadow army from the ruins.
- **City Dwellers** — Greater shadows who don't know the city is destroyed. Give information about what happened.
- **Psurlons** — Guard the ruins. Evil, 30% magic resistant, require +1 weapons to hit.

**The Genie's wishes can provide:** Wealth (1,000,000 ceramic pieces), item duplication (El's Drinker or Terror Blade recommended), help vs. Draj (shadow army + Quicksilver Glove), healing/resurrection.

**How to reach:** The sandstorm event (triggered by the Genie earlier) reveals Palace Ruins. Can reach through Teaquetzl after helping all three villages ally.

### LAVA RIFT
Rift to elemental plane of fire. Hermit defiler found it, began summoning fire elementals. Ranger and band drove him off; only ranger survived. Hermit schemes to return. Lesser fire elementals require +1 weapons.

### GEMFIELDS
Lava flows. Geysers. Lava domes contain gems (use pick). Thri-kreen hunters. Plugging geysers with rocks shoots out meteor metal (usable for metal axe+1 at Teaquetzl).

### WAGON TRAIN
Small plateaus and sinkholes. Magera attacked wagon train to get slaves. Prisoners must be rescued before magera kill them. Bridge over chasm — use rope to climb down to Subterranean Temple. **Kalinin** (warrior leader of prisoners) gives sword Hornblade and allies with Teaquetzl for final battle if rescued.

**Key item:** Plants here are naturally fibrous — can make rope, needed for bridge descent to Subterranean Temple.

### RED SANDS PLATEAU
Large central mesa. Common wandering monsters: tohr-kreen, strines, sand howlers, dune reapers, otyughs, rampagers, lesser earth elementals. Key NPCs:

- **Notaku** — Elven merchant dealing in magical herbs and spell components. Sends party on quests: deliver pith to Father Garyn in Teaquetzl, collect terror bloom (reward: Derth's Wand), get mastyrial stinger (reward: El's Shield). Buys sand howler eyes, fire eel tongues, screamer beetle wings.
- **Sage/Wise Hermit** — Wanders looking for Veiled Alliance. Identifies magical items. Gives magic wand and obelisk gem.
- **Demothi** — Trains mastyrials to sell as pack animals. Selling mastyrial Alita requires bag of salt from Toonuu at Nazca Lines.
- **Rift Ranger** — Only survivor of band that drove off the lava hermit.

### SAND OASIS
Sand druid watches over the oasis. Ensures it is not defiled. Gives butterfly wings.

### ELVEN SLAVERS
Templar and slavers operate here. Templar has a whistle that summons troops. Party may find themselves here if they fail the poison save at the Elven Caravan.

### MESSENGER ROUTE
White sand deserts. Party may fight slavers, the messenger, and blue slaad. Key NPCs: Messenger (carries notes between templar and noble, can summon up to 4 blue slaad), Hototo's Band and Dagger's Band (slave transfer, can be manipulated with deception), Nirveli (noble slave, gives thanks when freed).

### ELVEN CARAVAN
Sits in sandy wastes. Bone fence. Burrowing fire eels and bulettes attack. Wyvern riders from castle raid it. Key NPCs:

- **Drisana** — Caravan master. Wants raids stopped. Acts as judge in Tobrian dispute.
- **Larissa** — Seer of minor abilities. Tells fortunes for ceramic pieces.
- **Kel** — "Mage" merchant who sells goods, many non-magical. Real magic items: arrows+1, Soulcrusher, talisman of venom, gem for obelisk, mage scrolls.
- **Jark** — Honest merchant. Armor, weapons, rumors.
- **Tobrian** — Wine merchant and ex-slave merchant. Tries to poison party and sell them into slavery. Talisman of venom prevents his poison.
- **Katura** — Chahl's adopted daughter. Gives party information about Larissa and the visionary.
- **Tidzio** — Halfling wanderer. Gives information about Gemfields and surroundings.
- **Ylakez and Ketzia** — Refugees whose village was burned by Drajian troops. Give information about Tectuktitlay and templars for money.
- **Hesutu** — Dwarf who lost his focus when Drajian troops destroyed his tribe. Can be given new purpose.

**Talisman of venom:** Prevents weak poisons (Tobrian's wine). Must be worn when first visiting Tobrian.

### SSURRAN RUINS
Ssurran tribe worshipping old ruins and spirits. Shaman is 3rd-level. Various encounters here.

### WYRM BELLY / WYRM SCHOOL / WYRM TEMPLE
Three connected regions inside a massive wyrm (creature or structure). The Wyrm is home to magera raiders who attack the Elven Caravan. Key NPC: **Balkazar** at Wyrm School receives terror extract from Notaku. These regions must be cleared to stop the caravan raids.

### SUBTERRANEAN TEMPLE
Reached via rope on the Wagon Train bridge, or by climbing down wells in Cedrilte/Gedron/Teaquetzl. Underground temple region.

---

# SECTION 4: ORIGINAL GAME — CHARACTER ROSTER (Verified)

## Playable Party (Custom + Canonical)

The original game allows players to **create a custom party of 1–4 characters** or use the pregenerated party. The remake follows the FFVII Remake model: player creates their own character who exists alongside canonical party members encountered through the story.

### From Jareth's Journal (Manual pp. 3–4)

**GARETH / SELUCUS** — Half-giant gladiator. Favorite of Tectuktitlay's court, won matches for house of Tehuactl. Loyal to a fault until a templar asked him to throw a fight and he broke the templar's neck instead. Condemned to slave pens. Not bitter. Seeks wisdom.

**SARIA (SADIRA equivalent)** — Half-elf thief/preserver. Human slave mother, elven caravan master father who left. Raised on the streets stealing. Caught picking a preserver's pocket — the preserver trained her in elemental arts and preserved magic near the volcano. Slaver band captured her. Killed a templar at her auction with spells. Now in the pens.

**TARIM** — Thri-kreen female hunter. Trapped by a templar while hunting city troops on the salt flats west of Draj. Sent to arena rather than killed outright. Doesn't mind fighting, misses the hunt and the wasteland.

## Key NPCs (from Cluebook)

**SCAR** — Gladiator, "King of the Pens." Captured to entertain Tectuktitlay. Escape plan: through Arena west exit after 5 visits.

**MERZOL** — Would-be King of the Pens. Less organized than Scar. Escape after 3 Arena visits. More straightforward and risky plan.

**TRUSTEE** — Old gladiator who can no longer fight. Former wilderness guide. Knows Dinos.

**DINOS** — Slave cook. Was imprisoned for accidentally poisoning a templar with bad food. Heals Gilal.

**GILAL** — Gladiator with memory damage from failed escape attempt. Dinos can heal her.

**MIRLON** — Vain gladiator, secretly working for Templar Pehtucl.

**KURZAK** — Main guard. Takes bribes but gives nothing.

**BONECRUSHER** — Half-giant monster trainer. Retrieved laggard slaves.

**TEMPLAR PEHTUCL** — In charge of Slave Pens. Corrupt, leads party to ambush. Carries sword Bloodwrath+1.

**MIKQUETZL** — Disgraced templar. Rules tari worshippers in sewers. Has Chameleon Gloves. Insane.

**HIGH WARREN CHIEF** — Tari leader. Has Helm of Contemplation.

**DAGOLAR** — 20th-level psionicist. The deep-game villain of the underground section.

**WYRMIAS** — Defiler controlling Gedron Village. Man of his word, dangerous.

**LINARA** — 6th-level preserver, unaffected by Wyrmias. Critical NPC.

**JASMINE** — 9th-level preserver. At Silt Sea Summoning.

**CHAHL** — Leader of Teaquetzl Village.

**THE VISIONARY** — Halfling prophet. His prophecy drives the alliance arc.

**FATHER GARYN** — Cleric of water. Village healer of Teaquetzl.

**CRAGG** — Greater shadow. Former advisor who saved Korbnor's knowledge. Has the Genie bottle.

**THE GENIE** — Grants three wishes. Critical late-game asset.

**KRAXIS** — Drajian commander. Final battle antagonist.

**NOTAKU** — Elven spell component merchant. Sends party on quests.

**DRISANA** — Elven caravan master.

**TOBRIAN** — Corrupt wine merchant. Enemy NPC.

**SEMYON** — Former gladiator tied up as punishment in Arena. Join Veiled Alliance (one reference in cluebook) before joining party for one Arena fight.

---

# SECTION 5: ORIGINAL GAME — RACES & CLASSES (from Manual)

## Races (8 in Original)

| Race | Ability Adjustments | Special | Notes |
|------|-------------------|---------|-------|
| Dwarf | +2 CON, +1 STR, -1 DEX, -2 CHA | Non-magical (no wizard spells, clerics OK) | Up to 250 years old, ~200 lbs |
| Elf | +2 DEX, +1 INT, -1 WIS, -2 CON | Can run 50+ miles/day, dishonored by riding animals | Long-limbed sprinters |
| Half-Elf | +1 DEX, -1 CON | Self-reliant from intolerance | 6–6.5 feet tall |
| Half-Giant | +4 STR, +2 CON, -2 INT, -2 WIS, -2 CHA | Mood shift mechanic | 10–12 feet tall, 1,600 lbs |
| Halfling | +2 DEX, +2 WIS, -1 CON, -1 CHA, -2 STR | Always peak physical condition | 3.5 feet tall, 50–60 lbs |
| Human | (balanced) | Can be dual-class | Can be any class |
| Mul | +2 STR, +1 CON, -1 INT, -2 CHA | Always male. Bred for slavery/combat | 6–6.5 feet, 240–300 lbs |
| Thri-Kreen | +2 DEX, +1 WIS, -1 INT, -2 CHA | Always female. Chatkcha weapon (crystalline, returns on miss, 3–9 dmg, 90 yards). Cannot use armor, cloaks, belts, boots, or rings | 6-limbed insectoid, 7 feet at shoulder |

**NOTE from manual:** Mul is always male. Thri-kreen is always female in the original game. The remake should decide whether to preserve this or update it.

## Classes (8 in Original)

**FIGHTER** — STR 9 min, Prime STR. All races. All armor/weapons. No magic. Gains extra attacks at high levels.

**GLADIATOR** — DEX 12, STR 13, CON 15 min. Prime STR. All races. No spells. Gains -1 AC bonus when wearing armor at level 5. Extra attacks at high levels.

**RANGER** — STR 13, DEX 13, WIS 14, CON 14 min. Prime STR+DEX+WIS. Elf, Half-elf, Halfling, Human, Thri-kreen only. Can use two one-handed weapons with no penalty. Gains cleric spells from chosen elemental sphere at level 8.

**PRESERVER** — INT 9 min. Prime INT. Elf, Half-elf, Human only. No armor. Limited weapons. Casts spells in harmony with nature. Does not destroy land.

**CLERIC** — WIS 9 min. Prime WIS. All races. All armor. Weapons restricted by chosen element (fire = flaming weapons + obsidian, earth = stone/metal/wood, air = missile weapons only, water = bone/wood). Can turn undead. Extra spells at WIS 15+.

**DRUID** — WIS 12, CHA 15 min. Prime WIS+CHA. Half-elf, Halfling, Human, Mul, Thri-kreen only. No armor (can use magical protection items). No restrictions on weapons. Cannot turn undead. Extra spells at WIS 15+. Guards a section of land.

**THIEF** — DEX 9 min. Prime DEX. All races. Leather armor only. All weapons. Backstab (attack from exact opposite direction). Scales vertical surfaces.

**PSIONICIST** — CON 11, INT 12, WIS 15 min. Prime CON+WIS. All races. Leather armor only. Small weapons only. Three disciplines: psychokinesis, psychometabolism, telepathy. All characters in SHATTERED LANDS begin as first-level psionicists.

**Multi-class** is possible for non-humans (split XP evenly). Dual-class is humans only (can do it twice for 3 total classes, must reach level 3 in first class before switching).

## Level Advancement Tables (from Manual Appendix)

**Fighter/Gladiator/Ranger:** 1d10 HP/level. XP: 0, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000 (Fighter) | 0, 2250, 4500, 9000, 18000, 36000, 75000, 150000, 300000 (Gladiator/Ranger)

**Preserver:** 1d4 HP/level. XP: 0, 2500, 5000, 10000, 20000, 40000, 60000, 90000, 135000

**Cleric/Druid:** 1d8 HP/level. XP: 0, 1500, 3000, 6000, 13000, 27500, 55000, 110000, 225000

**Thief/Psionicist:** 1d6 HP/level. XP: Thief: 0, 1250, 2500, 5000, 10000, 20000, 40000, 70000, 110000 | Psionicist: 0, 2200, 4400, 8800, 16500, 30000, 55000, 100000, 200000

---

# SECTION 6: ORIGINAL GAME — COMBAT & MECHANICS (from Manual)

## Core Combat System (AD&D 2nd Edition)

**THACØ** = To Hit Armor Class Zero. Attacker's number must be rolled equal to or greater than (THACØ - target's AC) to hit. Lower THACØ = better. Modified by range, attacking from rear, magic weapons, spells.

**d20 roll formula:**

```
Need to roll: THACØ - Target_AC or higher
Example: Fighter THACØ 5 vs. Monster AC 3 → need 2+
Example: Fighter THACØ 5 vs. Monster AC -2 → need 7+
```

**Hit Points:** At 0 HP = unconscious. At -10 HP = dead. Constitution affects HP per level.

**Ability Scores range:** 9 (low) to 24 (high). Generated randomly, modified by race and class.

**Saving Throws:** Used for spells, poison, magical effects. Modified by level and relevant stats.

## Gameplay Actions (Mouse/Keyboard)

**Three mouse modes:** Walk, Attack, Look (right-click to cycle)

**Attack modes:** Hand-to-Hand (adjacent) and Ranged (at distance with readied missile weapon)

**Look mode:** Examine objects. If one option available, happens automatically. Talk button for NPCs. Use button for objects.

**Combat end:** NPC enemies may flee, fight back, or summon reinforcements. Indiscriminate killing removes potential quest NPCs.

**Camping:** Rest at fire ring icons. Restores HP (if cure spells auto-cast) and all PSI points. Every rest = 8 hours. If Kurzak calls and party delays too long = alarm.

**Training:** Level-up is automatic when XP threshold reached. Spell/psionic training box appears.

## Stores
Ceramic pieces (CP) is currency. Shopkeepers have 6 item slots + MORE button. Yellow outline = can afford. Solid highlight = cannot afford. Sell button for items you own.

---

# SECTION 7: ORIGINAL GAME — SPELLS & PSIONICS (from Manual)

## Spell System

Spells have: RANGE, DURATION, AREA OF EFFECT, SAVING THROW.
- Range: 0 (self only), Touch (physical contact), yards
- Duration: Combat (one combat), Instantaneous, Special
- Saving throws: Neg (no effect if saved), 1/2 (half damage if saved), None, Special

**Max spells before rest:** Determined by level. See Spell Progression Tables.

**Cleric elemental spheres:** Air, Earth, Fire, Water. Clerics have Major access to own sphere + Minor access to Sphere of Cosmos (3rd level or less). Cannot cast other spheres.

**Cleric WIS 15+ bonus spells:** WIS 15: +2/1st, +1/2nd | WIS 16: +2/1st, +2/2nd | WIS 17–18: additional higher-level slots | WIS 19–22 add further bonuses.

### Preserver Spell List (Levels 1–5)

**Level 1:** Armor, Burning Hands, Charm Person, Chill Touch, Color Spray, Enlarge, Gaze Reflection, Grease, Magic Missile, Shield, Shocking Grasp, Wall of Fog

**Level 2:** Blur, Detect Invisibility, Flaming Sphere, Fog Cloud, Glitterdust, Invisibility, Melf's Acid Arrow, Mirror Image, Protection from Paralysis, Scare, Stinking Cloud, Strength, Web

**Level 3:** Blink, Dispel Magic, Fireball, Flame Arrow, Haste, Hold Person, Hold Undead, Lightning Bolt, Melf's Minute Meteors, Minor Malison, Monster Summoning I, Protection from Normal Missiles, Slow, Spirit Armor, Vampiric Touch

**Level 4:** Charm Monster, Confusion, Evard's Black Tentacles, Fear, Fire Shield, Ice Storm, Improved Invisibility, Minor Globe of Invulnerability, Minor Spell Turning, Monster Summoning II, Rainbow Pattern, Solid Fog, Stoneskin, Turn Pebble to Boulder, Wall of Fire, Wall of Ice

**Level 5:** Chaos, Cloudkill, Cone of Cold, Conjure Elemental, Dismissal, Domination, Feeblemind, Hold Monster, Lower Resistance, Monster Summoning III, Summon Shadow, Wall of Force, Wall of Stone

### Cleric Spell List (Levels 1–5)

**Level 1:** Bless, Cause Fear, Cause Light Wounds, Cure Light Wounds, Curse, Entangle, Invisibility to Undead, Magical Stone, Protection From Evil, Remove Fear, Shillelagh

**Level 2:** Aid, Barkskin, Charm Person or Mammal, Dust Devil, Find Traps, Flame Blade, Hold Person, Resist Cold, Resist Fire, Spiritual Hammer

**Level 3:** Bestow Curse, Cause Blindness or Deafness, Cause Disease, Conjure Lesser Elemental, Cure Blindness or Deafness, Cure Disease, Dispel Magic, Magical Vestment, Negative Plane Protection, Prayer, Protection from Fire, Remove Curse, Remove Paralysis, Summon Insects

**Level 4:** Abjure, Blood Flow, Cause Serious Wounds, Cloak of Bravery, Cloak of Fear, Condense, Cure Serious Wounds, Dehydrate, Dust Cloud, Focus Heat, Free Action, Neutralize Poison, Poison, Produce Fire, Protection from Evil 10' Radius, Protection from Lightning

**Level 5:** Cause Critical Wounds, Conjure Elemental, Cure Critical Wounds, Deflection, Dispel Evil, Flame Strike, Insect Plague, Ironskin, Quicksand, Raise Dead (cannot raise Elves), Slay Living, Wall of Fire

## Psionic System

**PSP (Psionic Strength Points):** Regenerate at 3 per hour of walking. Fully restored by rest.

**Power Score:** Character's relevant attribute ± modifier = % chance to activate. A character ALWAYS makes a power check when activating. Power score 20 can still fail occasionally.

**Initial Cost:** PSPs spent on activation. Failing power check costs half. **Maintenance Cost:** PSPs per round to keep power active. If no maintenance listed, cannot be maintained.

**All characters begin as 1st-level psionicists in Shattered Lands.**

### Psychokinesis Sciences
- **Detonate** — CON-3, 18 PSP. Explode latent energy in objects for 1-10 dmg in 10' radius. May disintegrate items.
- **Disintegrate** — WIS-4, 40 PSP. Reduces creature to ash on failed save vs death magic.
- **Project Force** — CON-2, 10 PSP. Psychokinetic "punch" at 200 yards. 1-6 dmg + target's AC.

### Psychokinesis Devotions
- **Ballistic Attack** — CON-2, 5 PSP. Throw small object at deadly speed. 1-6 dmg.
- **Control Body** — CON-2, 8 PSP, 8/round. Control another's body (marionette). -6 to attack rolls. Not outside combat.
- **Inertial Barrier** — CON-3, 7 PSP, 5/round. Halves damage from breath weapons, missiles, gas, acid, ice storms.

### Psychometabolism Sciences
- **Animal Affinity** — CON-4, 15 PSP, 4/round. Grow claws, 1-10 dmg.
- **Energy Containment** — CON-2, 10 PSP. No effect from electricity, cold, fire, heat, sound energy attacks.
- **Life Draining** — CON-3, 11 PSP. Drain up to 6 HP from another. Added to psionicist's total temporarily (1 hour).

### Psychometabolism Devotions
- **Absorb Disease** — CON-3, 12 PSP. Transfer disease to self, then cure it. Cannot absorb curses.
- **Adrenalin Control** — CON-3, 8 PSP, 4/round. +1 to +6 STR temporarily.
- **Biofeedback** — CON-2, 6 PSP, 3/round. Reduce incoming damage by 2. Improve AC by 1.
- **Body Weaponry** — CON-3, 9 PSP, 4/round. Use one arm as a weapon (as strong as wood or steel).
- **Cell Adjustment** — CON-3, 5 PSP. Heal wounds and cure diseases. Cannot remove curses.
- **Displacement** — CON-3, 6 PSP, 3/round. Project image 3 feet away. AC improved by 2.
- **Enhanced Strength** — WIS-3, varies. Raise STR to 24. 2x PSP cost per point added; same per round maintenance.
- **Flesh Armor** — CON-3, 8 PSP, 4/round. Temporary armor based on level. No penalties for use.
- **Graft Weapon** — CON-5, 10 PSP, 1/round. Weapon becomes part of body. +1 to hit. Cannot switch.
- **Lend Health** — CON-1, 4 PSP. Transfer HP to another. Cannot exceed target's max or drop self below minimum.
- **Share Strength** — CON-4, 6 PSP, 2/round. Transfer STR to another (2 lost for every 1 received).

### Telepathy Sciences
*(Note: Game automatically activates defenses. Mind blank and tower of iron will controlled by game.)*
- **Domination** — WIS-4, varies. Control another's mind. PSP cost depends on subject. Not outside combat.
- **Mass Domination** — WIS-6, varies. Up to 5 creatures at once. Not outside combat.
- **Psychic Crush** — WIS-4, 7 PSP. Attack on psionicist's mind. Up to 6 HP damage.
- **Superior Invisibility** — INT-5, varies, 5/round. Cannot be seen, heard, or smelled. Dispelled if user attacks. Not outside combat.
- **Tower of Iron Will** — WIS-2, 6 PSP. Defense vs. psionic contact. Can initiate one other power while warded.

### Telepathy Devotions
- **Ego Whip** — WIS-3, 4 PSP. Stun target 1-4 rounds.
- **Id Insinuation** — WIS-4, 5 PSP. Paralyze target 1-4 rounds. Not outside combat.
- **Intellect Fortress** — WIS-3, 4 PSP. Telepathic defense for all minds within 3 yards.
- **Mental Barrier** — WIS-2, 3 PSP. Personal defense only. Can use other powers while protected.
- **Mind Bar** — INT-2, 6 PSP, 4/round. 75% magic resistance to mind-affecting spells.
- **Mind Blank** — WIS-7, 0 PSP, 0/round. Always "on." Defense vs. psionic attacks. Free.
- **Psionic Blast** — WIS-5, 10 PSP. Tricks opponent into believing it lost 80% HP. When at 20% HP, falls unconscious.
- **Synaptic Static** — INT-4, 15 PSP, 10/round. Prevents ALL psionics (including the user) in area.
- **Thought Shield** — WIS-3, 1 PSP. Protect mind from psionic attacks. Can initiate another power simultaneously.

---

# SECTION 8: ORIGINAL GAME — BESTIARY (from Manual & Cluebook)

*Key creatures for the remake, with combat stats from the manual's Detailed Descriptions section.*

## Featured Creatures

**DAGGORAN** — AC 7, HD 4, THACØ 17, 2-12 bite dmg + Psionics (Detonate, Ballistic Attack, Control Body, Inertial Barrier). Pack hunters, 2-8 appearing. Track psionic signatures. Used as Drajian guard trackers. Leap up to movement distance.

**DAGOLAR SLIME** — AC 2, HD 7, THACØ 13, 2-12 acid dmg. Immune to crushing/thrusting weapons. Launches sticky web (save vs. breath or immobile) and corrosive acid (destroys armor). Eats brains. Solitary. Created by Dagolar from tyrian slimes.

**DARK SPIDER** — AC 2, HD 6, THACØ 15. 3 attacks: 1-10/1-10 (forelegs) + 1-6 bite + type F poison (deadly if save fails). Some cast defiler spells to 6th level. Queen spiders are psionicist/defilers. Form tribes with warrior/mage/queen types. 2-20 appearing.

**DUNE REAPER** — AC 2, HD 8, THACØ 13. 3 attacks: scythe claws 3-18 each (+7 exceptional strength) + 2-12 bite. 10% magic resistance. Fearless morale. Pack hunters. Common near Draj. Prized for the arena. 5-30 appearing.

**FIRE EEL** — AC 4, HD 6, THACØ 15, 3-24 bite + fire breath (6d6 in 10'). Burrows in sand. Attacks from underground. 1-3 appearing.

**GREATER SHADOW** — AC 4, HD 6, THACØ 15. 2 attacks: 2-12 touch + 1 STR drain. Immune to sleep/charm/hold/cold. Requires +1 weapon to hit. Can be turned. Once powerful humanoids (possibly muls) exposed to Negative Material Plane. STR loss persists until rest.

**MAGERA** — AC 6, HD 6, THACØ 15. 2 attacks: 1-8 fist (+8 dmg). 10% psionic chance. Some master defiler magic to 5th level. Tribal. Raid caravans. 5-30 appearing.

**MASTYRIAL** — AC 0, HD 12, THACØ 9. 4 attacks: 1-10/1-10 (pincers) + 2-12 (bite) + 1-6 (stinger, poison = 30 dmg, 15 if saved). Regenerates 3 HP/round. Immune to blunt weapons. Lies buried in sand waiting for prey.

**MOUNTAIN STALKER** — AC 4, HD 10, THACØ 11. 4 attacks: 3-18 each (tentacles, +7 dmg). Skilled climbers. Populate mountains west of Draj. Pack of 5-10.

**PSURLON** — AC 0 (natural), HD 10 (Adept 18), THACØ 11. 3 attacks: 3-12/3-12 (claws) + 2-16 (bite). 45% magic resistance. Requires +1 weapon to hit. Immune to sleep/charm/hold. Massive psionic power (10 levels, 4 disciplines, 200+ PSPs). Trapped in Astral Plane. Evil, genius-level intelligence. Want to return to Athas. 5000-year lifespan.

**SAND HOWLER** — AC 5, HD 4+2, THACØ 17. 3 attacks: 1-3/1-3/1-6. Paralyzing gaze attack. Pack of 2-16. Nearly hunted to extinction in the tablelands.

**SCREAMER BEETLE** — AC 2, HD 3, THACØ 17. 1-8 (mandibles) + Psionic Blast (from abdomen). Forms small packs. Multicolored chitinous shells prized by collectors.

**SSURRAN** — AC 4, HD 6, THACØ 15. 1-8 claws (+4). Half damage from fire. Nomadic reptilian tribe. Shamans can reach 6th level cleric. Skin can be worked as scale armor (AC 6, fire resistant).

**STYR** — AC 0, HD 14, THACØ 7. 4 attacks: 2-20 each (fist) + fire breath (3-18). 30% magic resistance. Requires +1 weapon to hit. Summoned earth elemental plane creature. Guards treasure. Neither eats nor sleeps.

**TANAR'RI GREATER (BABAU)** — 50% magic resist, +1 weapons to hit. Gaze attack (ray of enfeeblement). Corrodes weapons and armor. Deadly poison. Extremely dangerous.

**TANAR'RI TRUE (VROCK)** — 70% magic resistant, +2 weapons to hit. 5 attacks/round (claws + beak). Look like vulture-human hybrids.

**THRI-KREEN** — 4 claws + paralyzing bite (victims take double damage afterward). Extremely agile, dodge missile attacks. Often better attacked with magic.

**TYRIAN SLIME** — AC 2, HD 5, THACØ 15, 2-12 acid. Immune to crushing/thrusting weapons, fire, and acid. Sticky web attack (save vs. breath). Corrosive acid. Can ooze through cracks.

**UNDERMOUNTAIN FOLK (MINDHOME)** — AC 6, HD 2+1, THACØ 19. Use psionics defensively. Telepathically linked community. Immune to enchantment/charm. Harmless unless attacked. Go catatonic if separated from their Mindhome.

**ZOMBIE** — Standard undead. Turned by clerics. Mindless, walk straight toward opponents.

---

# SECTION 9: REMAKE STORY — THE THREE-LAYER SYSTEM

## Content Tagging

All story content is tagged:

**[ORIGINAL]** — From the verified 1993 source documents. Must appear in the remake. Cannot be removed or fundamentally altered.

**[EXPANDED]** — Enrichment of original content. The scene still ends the same way. The original NPC is still present and serves their original function. But now there is more texture, more depth, more humanity.

**[NEW]** — Content that does not exist in the original. Added to serve the larger story. Must be organically consistent with the setting. Must not replace or contradict original content.

---

# SECTION 10: REMAKE CHAPTERS — ORIGINAL STORY REBUILT

## Chapter One: King Tectuktitlay's Arena

### [ORIGINAL] Beats
- Party begins as gladiators in Draj's Arena
- Tutorial combat — survive first fight
- The Announcer runs fights, heckles, controls monsters
- Semyon staked out in the arena — needs water from the Slave Pens to revive
- Five Arena visits (or three for Merzol) required before escape contacts open
- Scar offers escape through the Arena's west exit after five visits
- Merzol offers a more dangerous escape after three visits

### [EXPANDED]
- **The crowd is alive.** Draj's arena culture is visible — nobles in boxes, slaves in standing areas, templars ensuring order. The crowd cheers for brutality and boos mercy.
- **The Announcer's commentary** is expanded into full voiced-style text that reveals Drajian society. He is simultaneously entertaining and monstrous.
- **Semyon's rescue** — extended scene. His gratitude, his story of how he ended up staked, his decision to find the Veiled Alliance (referenced in the original cluebook).
- **Scar and Merzol** get full personalities. The choice between them (more cautious/more risky) feels genuinely weighted.

### [NEW]
- **The Watcher in the Crowd** — A figure in the nobles' box watches the party with unusual attention. Not Tectuktitlay. Not a templar. They leave before the party can identify them. This figure reappears in Chapter Six.
- **Pre-fight Ritual** — Before each fight, characters can speak to each other. Brief dialogue reveals character through small observations, not exposition.
- **First Psionic Resonance** — After a significant victory, a brief unasked-for psionic flash — not words, just an impression of watching, of being recognized. The Voice first contact (ties to Chapter Six).

### Key Story Questions — Chapter One
- Why did the Watcher in the crowd show particular interest in the party?
- Will the party choose Scar's caution or Merzol's recklessness?
- What did Semyon see in the arena that he will carry to the Veiled Alliance?

---

## Chapter Two: The Slave Pens

### [ORIGINAL] Beats
- The Slave Pens: templars, half-giants, Drajian guards, mountain stalkers
- Scar in location 1 (King of the Pens)
- Trustee walks the pens — can be pickpocketed for key to Dinos' room (thief leader)
- Dinos the cook — heals Gilal, gives information
- Gilal — memory-damaged, can be healed by Dinos to reveal escape information
- Mirlon — traitor. Works for Templar Pehtucl. If given gems, leads party into ambush
- Kurzak — main guard. Takes bribes, gives nothing
- Bonecrusher — half-giant. If party delays too long, Bonecrusher comes to retrieve them
- Templar Pehtucl — fake escape offer, real ambush. Bloodwrath sword+1 on his body
- Armory (location 17): polearms and steel axe
- Secret room (location 4): arrows+3, gem, scale armor (push button on north wall after killing mountain stalker in adjacent pen)
- Sewer grate escape (location 12): thief picks lock, or hack/rip open

### [EXPANDED]
- **The Pens as a society.** The slave population has a functioning social order — the King of the Pens, the gang structure, the guards' corruption, the cook as an unlikely hub of information. This is expanded into a living ecosystem.
- **Gilal's memory sequence.** When Dinos heals her, the moment is more than a mechanic — it's an emotional scene. What she remembers of her escape attempt, and what it cost her, reveals what the pens do to people over time.
- **Mirlon's betrayal** can be seen coming if players pay attention — he is too eager to help, his information too convenient. The choice to trust or not trust him has consequences.
- **Kurzak's bribery** system is expanded — he can be pushed further than the original suggests, revealing information about the pens' deeper workings if the approach is right.

### [NEW]
- **The Ledger Room** — Adjacent to Pehtucl's quarters, the party can find a partial ledger of slave origins. Certain entries are relevant to companion backstories.
- **The Murmur Below** — From beneath the sewer grate, the party can hear distant strange sounds before they descend. Not human sounds. Not Tari sounds. Something else.

### Key Story Questions — Chapter Two
- Did the party trust Mirlon — and what does that choice say about them?
- What is in the ledger, and who does it connect to?
- What is making the sounds beneath the grate?

---

## Chapter Three: The Sewers

### [ORIGINAL] Beats
- Tari communities: low warrens (Churrr's thugs), high warrens (the Chief)
- Churrr kidnapped the chief's daughter for Mikquetzl
- Skull Temple and the Elders (animated tari skulls)
- Mikquetzl — insane disgraced templar building fanatical army
- Rescuing the chief's daughter — she rushes into battle, must be protected
- Staff of Parting — needed to drain collection pond and open Dagolar's Tunnels entrance
- Elders explain secret exit and path to Dagolar's Tunnels
- Bone crank needed for broken wheels

### [EXPANDED]
- **The Tari as a civilization** — Their reverence for the Elders, their skull temple, their community structure: this is an alien but coherent society. Expanded from the original's glimpse into a fully realized world.
- **Mikquetzl's madness** — He was once a real person. His descent is documented in scraps of writing around his temple. The party can piece together who he was before the disgrace.
- **The Elders' knowledge** is expanded — they know things about Draj's history that the surface world has forgotten. Pressing them for information beyond their immediate guidance reveals fragments of the city's deeper past.

### [NEW]
- **Dagolar's Victims** — In the depths near the tunnel entrance, the party finds evidence that Dagolar has been collecting specific types of individuals — not at random. There is a pattern to his experiments.

### Key Story Questions — Chapter Three
- What was Mikquetzl's life like before his disgrace? Does it matter?
- What pattern exists in Dagolar's victims?
- What do the Elders know about Draj that they are not eager to share?

---

## Chapter Four: Dagolar's Tunnels

### [ORIGINAL] Beats
- Dagolar is a 20th-level human psionicist conducting experiments
- Keldar is his warped servant who tracks names of Dagolar's victims
- Goburnix is Dagolar's zombie brother
- Killing Keldar in one shot prevents his teleportation
- Goburnix follows the party if freed and can expose Dagolar disguised as Jake or Mow

### [EXPANDED]
- **Dagolar's research** — What exactly is he studying? The remake makes his obsession specific and frightening: he has been attempting to map and manipulate the psionic resonance of Athas itself. His experiments are not random sadism — they are terrible science.
- **Keldar's book** — The list of names Keldar keeps is expanded into a recurring element. Recognizable names from earlier chapters may appear. The book itself becomes a document of what this region of Athas has suffered.

### [NEW]
- **Dagolar's Discovery** — In his deepest notes, a reference to something he found in the psionic substrate of Athas — an old signal, regular, patient. He does not know what it is. The party recognizes the psionic signature from their own experience.

---

## Chapter Five: The Fields & Free Villages

### [ORIGINAL] Beats
- Escape from Draj's underground into open desert
- Three free villages to find and ally: Teaquetzl, Cedrilte, Gedron
- The Visionary's prophecy is the rallying point
- Father Garyn needs pith from Notaku
- Wyrmias has taken over Gedron — must be resolved (two statue pieces)
- Elven Caravan: Notaku, Drisana, Tobrian (attempted poisoning), Larissa
- Palace Ruins (Korbnor): Genie Bottle via Cragg's story
- Captured gladiators must be freed from Arant
- Final battle approaching: Teaquetzl, Cedrilte, Gedron + Kalinin (wagon train) + Genie = viable army

### [EXPANDED]
- **The Visionary's prophecy** — In the original, it's a plot driver. In the remake, it's examined: who is this halfling? Where did the vision come from? What exactly does it say? The ambiguity of prophecy becomes thematic.
- **The three villages as distinct cultures** — Each village has its own identity, history, and reason to fear Draj. Building the alliance is genuinely diplomatic work, not just quest-completion.
- **Cragg's tragedy** — The Palace Ruins section is expanded. Cragg was a good man who made the only choice available to him and was buried with the results for thousands of years. His story, told through the shadows and the environment, is one of the remake's most haunting sequences.
- **Kraxis** — The Drajian commander is given a full personality, a reason for his loyalty to Tectuktitlay, a speech before the final battle.

### [NEW]
- **The Alliance's Fragility** — Even after all three villages agree to fight, they distrust each other. The night before the final battle, the party can overhear arguments between village leaders. This shapes the epilogue.
- **The Genie's Warning** — When granting the wish for aid against Draj, the Genie gives a brief, cryptic observation: the party carries something it does not know it carries. It cannot say more. It vanishes.

### Key Story Questions — Chapter Five
- Who sent the Visionary his prophecy? Was it a vision, or instruction?
- What does Cragg's sacrifice mean for the question of how to fight evil?
- What does the Genie mean — what does the party carry without knowing it?
- Does the alliance survive the final battle as a united force, or fracture immediately after?

---

# SECTION 11: REMAKE CHAPTERS — NEW STORY (6–8)

*These chapters are entirely new. They pick up directly after the original game's ending and carry the story into territory the 1993 game could only hint at.*

**Central question of the new story: What does it actually take to break a Sorcerer-King?**

The original game's answer was: survive, escape, be free, and fight back. The new chapters answer: that was only the beginning. Tectuktitlay still exists. Five other Sorcerer-Kings still exist. Athas is still dying. The war for the three free villages was one battle. The war for Athas is something else entirely.

---

## New Chapter Six: The Genie's Warning

*Immediately following the original game's ending. The party has won — Draj's army is broken, the three villages are free, the Genie has vanished. But the Genie said something. And the party needs to understand what they are carrying.*

**New Location: The Freelands**
The desert beyond Draj's reach. Not empty — inhabited by nomads, escaped slaves, and those who refuse to live under any Sorcerer-King. And something else: evidence that someone or something has been watching the party from before they were in the arena.

**New Character: KORVAL DUST**
Ancient preserver. Former advisor to a Sorcerer-King (not Tectuktitlay — an older one). Turned against them all a century ago. Has been at the Shattered Spire — a ruined tower in the deep Freelands — for decades. He knows what the party carries. He sent the psionic flash in the arena. He was the Watcher in the crowd.

**New Character: SELA**
A former defiler who is attempting to become a preserver. Theoretically impossible — the transformation of the land once defiled cannot be reversed. She is attempting it anyway, slowly, at enormous personal cost. She is at the Spire because Korval is the only person who believes she can succeed.

**New Location: The Shattered Spire**
A ruined pre-cataclysm tower, six levels deep. Each level is a stratum of Athas's history — the world that was, the world during the cataclysm, the world after. The Voice that first contacted the party in the Arena lives in the deepest level.

**What the party carries (revealed here):** A psionic resonance, accumulated through the specific sequence of experiences in the original game — the Arena fights, Dagolar's experiments, the Genie's wish. This resonance is a key. It can open something in the Spire. Korval has been waiting for someone who had these exact experiences to arrive. He arranged the party's original circumstances. Partially.

### Key Story Questions — Chapter Six
- Did Korval arrange the party's slavery and escape? What does that make him?
- Is Sela's transformation possible — and does the party help or hinder it?
- What does the psionic key open in the Spire?
- What is the Voice, and why has it been waiting?

---

## New Chapter Seven: The Voice's Name

*The key has opened the deepest level. The Voice has a name. And the name changes everything about what the party thought they knew about Athas.*

**What the Voice Is:**
Not a person. Not a creature. A recording — the last transmission of the people who built the Spire, preserved in Athas's psionic substrate for ten thousand years. The people who built the Spire were the civilization that existed before the Sorcerer-Kings. They destroyed themselves trying to prevent the cataclysm. They failed. But before they died, they compressed everything they knew — how to restore Athas, how to stop a Sorcerer-King's transformation, how to turn defilers back to preservers — into a psionic broadcast that has been playing on a frequency no one could hear.

Until now. Until the party's accumulated resonance became a receiver.

**The Revelation:**
The Sorcerer-Kings know the recording exists. They do not know anyone can hear it. The transformation that makes them into Dragons — the terrible thing happening in Kalak's ziggurat in Tyr — can be stopped. But only if the recording is used before the transformation is complete.

**New Character: THE ARCHIVIST (part of the Voice)**
Not alive. Not dead. The last personality of the Spire's builders, preserved as psionic data. Knows everything the pre-cataclysm civilization discovered. Has been waiting ten thousand years to hand that knowledge to someone. Has opinions about how it should be used.

**New Complication: The Veiled Alliance**
The Alliance has learned about the Spire. They are divided. Some want the knowledge used immediately — defilement, transformation, sacrifice, whatever it costs, stop the Dragon in Tyr. Others believe the knowledge can only be used if used correctly, or it becomes the same destruction it's meant to prevent.

**Elder Pirdan** has arrived at the Spire with a faction ready to use the knowledge wrong.

### Key Story Questions — Chapter Seven
- What does it mean that Athas could be restored? Is that even possible now?
- Can the Voice's knowledge stop Kalak's transformation?
- Is the party willing to use the knowledge imperfectly to stop an immediate catastrophe?
- Where does Sela stand when defiling magic becomes the fastest path to victory?

---

## New Chapter Eight: The Last Green Thing

*The Dragon in Tyr is almost complete. The Alliance is fracturing. The Archivist's knowledge can stop it — but only if the party makes a choice that cannot be undone.*

**The Choice:**
The pre-cataclysm knowledge includes a ritual that can force a Sorcerer-King back from the Dragon transformation — permanently stunting their power. But the ritual requires defiling an area the size of a city block. Destroying it. Killing everything living in it. Permanently.

Using defiling magic to stop a Sorcerer-King from becoming a Dragon means becoming, for one moment, exactly the thing you are fighting against.

The party must decide.

**Alternative:**
The knowledge also contains a slower method — something that could work without defiling, but requires years and perfect conditions and the cooperation of the Veiled Alliance. And Kalak's transformation will be complete in days.

**What Sela's Arc Resolves:**
If Sela has succeeded — even partially — in her conversion from defiler to preserver, she becomes the key to the slower method. If she has failed, the party has only the fast method available.

**What the Genie's Warning Meant:**
The party carries the resonance. The resonance is not just a key. It is a seed. If the slow method is used correctly, the party's accumulated psionic resonance can be the foundation of a restoration — not of Athas instantly, but of one small part of it. One valley. One water source. One place where something green grows again.

Not a victory over the Sorcerer-Kings. Not the salvation of Athas. A beginning.

### Key Story Questions — Chapter Eight
- Will the party use the fast method (defilement) or the slow method (years, uncertainty)?
- If Sela succeeded: does her conversion change the calculus?
- What is the party willing to sacrifice, and what are they not?
- What does Athas look like in the epilogue, and is that enough?

**The Ending:**
There is no total victory. Tectuktitlay still rules Draj — though shaken. Kalak's transformation is stopped or completed depending on the choice. Five other Sorcerer-Kings remain. But somewhere in the Freelands, near the ruins of the Shattered Spire, something is growing.

---

# SECTION 12: CHARACTER ROSTER — FULL

## [ORIGINAL] Core Party (Verified)

**GARETH (SELUCUS)** — Half-giant gladiator. Tectuktitlay's favorite. Broke a templar's neck rather than throw a fight. Condemned for it. Not bitter. Seeks wisdom. *Remake arc: What does a man built by a system designed to use and discard people do with freedom?*

**SARIA** — Half-elf thief/preserver. Raised on the street, trained by a preserver, enslaved after killing a templar with magic. *Remake arc: Magic is what saved her and what destroyed her life. What is her relationship with power?*

**TARIM** — Thri-kreen female. Hunter who was captured and sent to the arena. Doesn't mind fighting. Misses the wasteland. *Remake arc: The wasteland she wants to return to is dying. What happens when the home you're fighting toward no longer exists as you remember it?*

**[NEW] Player Character** — Custom-created. Fifth party member. Race and class shape dialogue options and how events are perceived. Background options affect opening circumstances.

## Key NPCs

*(See Section 4 for full original roster)*

**SCAR** — Pragmatic escape planner. More caution, more preparation.
**MERZOL** — Bold escape planner. Faster, riskier.
**SEMYON** — Joins Veiled Alliance after rescue. One fight in Arena. Key thread.
**GILAL** — Memory of escape. Critical information for the party.
**TEMPLAR PEHTUCL** — The pens' villain. Carries Bloodwrath+1.
**MIKQUETZL** — Sewers' villain. Insane disgraced templar.
**DAGOLAR** — Underground villain. 20th-level psionicist.
**WYRMIAS** — Villages villain. Defiler with integrity.
**CRAGG** — The ghost who did the right thing and paid for it forever.
**THE GENIE** — Late-game asset, early-game MacGuffin.
**KRAXIS** — Final battle antagonist. The human face of Draj's military.

## [NEW] Characters

**KORVAL DUST** — Ancient preserver. Arranged (partially) the original events. Has been waiting. Not entirely trustworthy even when everything he says is true.

**SELA** — Former defiler attempting the impossible conversion. Her arc is the test case for the new story's central question.

**THE ARCHIVIST** — Psionic recording of the last pre-cataclysm civilization. Not alive. Has opinions. Cannot be fully trusted because it has been alone for ten thousand years.

**ELDER PIRDAN** — Alliance defiler faction leader. Genuinely grieving for Athas. Done waiting. Wrong about the method. Not wrong about the urgency.

---

# SECTION 13: GAME SYSTEMS

## Combat System

**Based on original AD&D 2nd Edition THACØ system, modernized for grid-based Godot 4:**

```
Attack Roll: d20
Hit if: roll >= (Attacker THACØ - Target AC)
Critical Hit: Natural 20 = double damage dice
Fumble: Natural 1 = miss + weapon condition check
```

**Grid:** Tile-based isometric. Each character occupies one tile.
**Flanking:** Attack from two opposite sides = +2 to hit
**High Ground:** +2 to hit, +1 damage for ranged attacks
**Cover:** Partial = -2 to hit against; Full = cannot target

**Action Economy (per turn):**
- 1 Move Action (up to Speed tiles)
- 1 Standard Action (attack, spell, psionic, item use)
- 1 Free Action (drop item, minor dialogue)
- 1 Reaction (opportunity attack on adjacent enemy movement)

**Formation System (new):**
- Vanguard / Encircle / Ambush (DEX check for hidden start) / Defensive

**Morale:** Enemies can break and flee. Templars never flee. Slave catchers do.

**Weapon Condition (from original):** All weapons degrade. Materials:
- Bone: 5 uses before break risk
- Obsidian: 8 uses, shatters on fumble
- Chitin: 10 uses, no fumble-break
- Metal: Never degrades. Extremely rare.

## Psionic System

Full PSP system as per original manual (Section 7 of this document). All characters are 1st-level psionicists at game start (as per original).

Psychokinesis, Psychometabolism, and Telepathy disciplines. Psionicists specialize in all three; other classes choose one at character creation.

PSP regeneration: 3 per hour walking, full restore on rest.

## Resource Systems

**Water (critical):** Measured in flasks. Consumed by travel, combat, some abilities, heat exposure. At zero: death within 48 hours with escalating CON damage.

**Food:** Measured in rations. Starvation progression: -1 STR/day → -1 CON/day → incapacitation.

**Ceramic Pieces (CP):** Primary currency. Metal items worth vastly more.

**Heat/Fatigue:** Extended day travel builds Fatigue bar. At high Fatigue: slower movement, weaker attacks. Clears with rest and water.

## Flag System

All story choices tracked as flags:
- **Boolean flags:** Did event happen?
- **Integer flags:** Reputation scores, visit counts
- **String flags:** Specific choices made

Flags must be queryable by: story scenes, dialogue options, enemy behavior, faction reactions, epilogue text.

---

# SECTION 14: ART DIRECTION

## Visual Philosophy

The original SSI game's pixel art constrained by 1993 hardware is the reference. The remake should look like what the original was *trying* to be — the same aesthetic language, the hardware limitations removed.

**Perspective:** Isometric, approximately 2:1 pixel ratio. Same camera angle as original.
**Style:** Hand-crafted pixel art. No procedural generation. No smooth 3D. Every tile has history.

## Color Palette of Athas

- **Sky:** Deep crimson to burnt orange. Never blue. Never.
- **Sand:** Ochre, burnt sienna, rust red. Not clean beige.
- **Shadows:** Deep purple-brown (not grey-black).
- **Stone:** Bleached bone-white to dark obsidian.
- **Living things (rare):** Dusty olive, faded sage. Green is the rarest color on Athas.
- **Water:** Precious, shown as deep blue-green. Draws the eye immediately.
- **Fire/Torches:** The primary indoor light source. Warm amber.
- **Psionic effects:** Cold blue-white, interior, resonant.
- **Defiling magic:** Ash-grey radiating outward, leaving dead ground.

## Character Design Rules

- Every character's appearance reflects their history
- No pristine equipment on anyone (except templars in the templar district)
- Half-giants are genuinely enormous relative to humans on screen
- Thri-kreen are alien — six-limbed, compound eyes, they do not stand or move the way mammals do
- Muls look exactly like what they are: bred for labor, usually bald, scarred

## UI Design

- Minimal HUD during exploration
- Inventory screen styled like a scavenged journal
- Combat UI: full isometric grid, initiative order track, action button row
- Fonts: classical serif (Cinzel or similar) for headers, rough hand-cut style for titles
- Text color: amber/gold on near-black
- Scene panels: full-width illustrated panels for key story moments, evoking TSR Dark Sun cover art

---

# SECTION 15: AUDIO DIRECTION

## Music

The original MIDI soundtrack drew on Middle Eastern and North African tonality — sparse, percussive, modal. The remake preserves this DNA with higher quality instruments and more dynamic range.

**Key principle:** This is not European fantasy music. No orchestral swells, no soaring strings. Bone instruments, skin drums, wind instruments that sound like they were carved from desert plants.

**Track contexts:**
- Arena (ambient dread, crowd murmur underneath everything)
- Slave Pens (near-silence broken by dripping, distant screaming, chain sounds)
- City/Draj (layered noise, crowds, oppressive order)
- Sewers (wet echoes, tari sounds, something moving in the dark)
- Desert (wind, insects, the vast emptiness that is almost beautiful)
- Combat (urgent, irregular percussion — not a march, a scramble)
- Rest (single instrument, melancholy, very quiet)
- Caravan (bustle, commerce, a fragile normalcy)
- Palace Ruins/Korbnor (alien resonance, the echo of ten thousand years)
- Spire (the Voice's acoustic fingerprint — repeating mathematical pattern that feels almost like language)

**Silence is a tool.** Some locations have no music. The Blasted Zone has no ambient sound either — complete sensory death. This must be deliberately designed, not a missing asset.

---

# SECTION 16: TECHNICAL SPECIFICATION — GODOT 4

## Project Structure

```
res://
├── scenes/
│   ├── ui/              # HUD, menus, inventory, dialogue
│   ├── world/           # World map, region maps, interiors
│   ├── combat/          # Combat grid, turn manager, ability UI
│   ├── characters/      # Player, companions, enemies
│   └── systems/         # Game state, save/load, flags
├── scripts/
│   ├── core/
│   │   ├── GameState.gd         # Central singleton — all state
│   │   ├── EventBus.gd          # Decoupled signal hub
│   │   └── ResourceManager.gd   # Asset loading/caching
│   ├── combat/
│   │   ├── CombatManager.gd     # Turn queue, grid, resolution
│   │   ├── TurnQueue.gd         # Initiative order
│   │   └── AbilitySystem.gd     # Spells, psionics, abilities
│   ├── story/
│   │   ├── StoryManager.gd      # Drives scene data → UI
│   │   ├── FlagTracker.gd       # All story flags
│   │   └── DialogueSystem.gd    # NPC conversations
│   ├── characters/
│   │   ├── CharacterStats.gd    # AD&D stats, THACØ, AC
│   │   ├── InventorySystem.gd   # Items, weight, equip
│   │   └── PsionicSystem.gd     # PSP pool, power resolution
│   └── world/
│       ├── MapManager.gd        # Map transitions, state
│       ├── EncounterSystem.gd   # Random + triggered encounters
│       └── WeatherSystem.gd     # Heat, sandstorms
├── assets/
│   ├── sprites/         # Isometric tiles, characters, UI
│   ├── audio/           # Music, SFX
│   ├── fonts/
│   └── data/            # Source data files
└── data/
    ├── story/           # JSON/tres scene and dialogue data
    ├── enemies/         # Enemy stat blocks
    ├── items/           # Item definitions
    ├── abilities/       # Spell and psionic definitions
    └── maps/            # Map layout data
```

## Key Architecture Decisions

**Data-Driven:** All story content (scenes, dialogue, flags, choices) lives in external data files, not in code. Writers can edit story without touching GDScript.

**Story Engine:** JSON-driven (or Godot Resources). Scene nodes have: text, choices (with flag requirements and consequences), art reference, combat trigger (optional), NPC triggers (optional).

**Save System:** Full serialization of GameState at any safe rest point. No autosave during combat. Save file captures: all flags (boolean/integer/string), all character stats, all inventory, all companion states, faction reputation, current location.

**Flag System Example:**

```gdscript
# Setting a flag
GameState.set_flag("rescued_chief_daughter", true)
GameState.set_flag("arena_visits", GameState.get_flag("arena_visits", 0) + 1)

# Checking a flag in story data
{
  "id": "scar_offer",
  "requires": {"arena_visits": {"min": 5}},
  "text": "Scar approaches you after the fight..."
}
```

## Isometric Tilemap

Use Godot 4's built-in TileMapLayer with isometric preset. Each region map is a separate scene with its own tilemap. Characters and objects are on separate layers above the tilemap.

## Recommended Plugins/Libraries

- Dialogic or custom dialogue system for NPC conversations
- Consider custom implementation for full control over story flag integration

---

# SECTION 17: DEVELOPMENT ROADMAP

## Phase 0 — Foundation
**Goal:** Walking skeleton.

- [ ] Read source PDFs end to end (manual + cluebook from Google Drive `Game Design/DS/`)
- [ ] Annotate any discrepancies between this Master Project File and the actual source
- [ ] Fill in the `reference/` spreadsheet skeletons (locations, NPCs, items, encounters, flags, spells, psionics, bestiary, companions, factions)
- [ ] Assemble asset reference library (screenshots, cover art, sprite sheets)
- [ ] Godot 4 project created, directory structure scaffolded
- [ ] GameState singleton implemented and tested
- [ ] EventBus implemented
- [ ] Basic Story Engine: JSON scene → text display → flag setting → choice resolution
- [ ] Basic combat: grid, one enemy type (Drajian Guard), THACØ resolution, win/lose
- [ ] One complete scene with combat

**Exit Criteria:** Player can make a character, read story text, make a choice that sets a flag, enter combat with a Drajian Guard, win or lose, see the result.

---

## Phase 1 — Chapters 1 & 2 (Arena + Slave Pens)
**Goal:** The opening fully playable.

- [ ] Full character creation (all 8 races, all 8 classes, all stat modifiers per manual)
- [ ] Arena: all fights, Announcer, Semyon rescue, Scar/Merzol encounter requirements
- [ ] Slave Pens: all NPCs, all escape routes, armory, secret room, sewer grate
- [ ] Companion system: Gareth/Selucus, Saria, Tarim can join
- [ ] Faction reputation: Drajian Templars, Free Slaves
- [ ] Basic water management
- [ ] Placeholder art

**Exit Criteria:** Chapters 1 and 2 completable on all major paths.

---

## Phase 2 — Chapters 3–5 (Underground + Wasteland + Villages)
**Goal:** Full original game completable.

- [ ] Sewers: Tari society, Mikquetzl, Staff of Parting, Elders
- [ ] Dagolar's Tunnels
- [ ] All 7+ wasteland region maps
- [ ] All three free villages: Teaquetzl, Cedrilte, Gedron
- [ ] Alliance-building quest chain
- [ ] Palace Ruins (Korbnor): Genie, Cragg, psurlons
- [ ] Final battle: Kraxis, waves, Genie wish resolution
- [ ] All NPC quest chains functional
- [ ] Full flag system tracking story decisions

**Exit Criteria:** Original game story completable start to finish on all major paths.

---

## Phase 3 — Polish & Beta
**Goal:** Polished, releasable, feedback-ready.

- [ ] Final pixel art (all tiles, characters, UI, scene panels)
- [ ] Full audio implementation
- [ ] Save/Load system
- [ ] UI polish
- [ ] Combat balance pass (original AD&D math verified against source tables)
- [ ] Bug fix and QA
- [ ] Public beta release

**Exit Criteria:** Polished release of original-game scope.

---

## Phase 4 — New Chapters 6–8
**Goal:** Complete game including new story.

- [ ] Chapter 6: Freelands, Korval Dust, Shattered Spire
- [ ] Chapter 7: The Voice, the Archivist, Veiled Alliance fracture
- [ ] Chapter 8: Endgame choice, Dragon in Tyr, epilogue variants
- [ ] Full psionic discipline trees (expanded from original)
- [ ] All new characters fully implemented
- [ ] Faction system across all chapters

---

# SECTION 18: KEY STORY QUESTIONS

*Every design decision should serve at least one of these. Every scene should advance at least one.*

## About Athas
1. What killed Athas — and is the death still ongoing, or has it reached equilibrium?
2. Are the Sorcerer-Kings the cause of the world's death, or its last maintainers?
3. If a Sorcerer-King falls, does anything actually improve — or does the vacuum kill more people?
4. What was the pre-cataclysm civilization? What did they know that was lost?

## About the Original Party
5. Who is Gareth/Selucus when he is not being used by something larger than himself?
6. What is Saria's relationship with the magic that saved and destroyed her?
7. What is Tarim hunting for, now that hunting to survive has become something else?
8. Does the party's freedom mean anything if three free villages are all that exists of it?

## About the Original NPCs
9. Did Scar's caution or Merzol's boldness serve the escape better — and does it matter?
10. What did Semyon see in the arena? What does he bring to the Veiled Alliance?
11. Was Cragg right to contain the evil of Korbnor rather than destroy it? What did that cost?
12. What does the Genie know that it cannot say?

## About the New Story
13. Korval arranged (partially) the party's original circumstances. Does that make what they built real or manufactured?
14. Can Sela convert from defiler to preserver — and does it change what the word "preserver" means?
15. The pre-cataclysm civilization tried to stop the Sorcerer-Kings and failed. What does the party know that they didn't?
16. Is it possible to use defiling magic to stop defiling magic — and remain yourself afterward?
17. What does Athas look like in the epilogue — and is one green valley enough?

---

# SECTION 19: FIRST STEPS FOR CLAUDE CODE

When this project resumes, here is the exact order of operations:

## Step 1: Verify the Source Documents
The PDFs in Google Drive at `Game Design/DS/` (`ds_shatterland_manual_pdf.pdf` and `ds_shatterland_cluebook_pdf.PDF`) are the ground truth. **Before writing any code or story content, read them.** The cluebook especially — it contains every map, every NPC, every item, every quest. This GDD is a synthesis; the source documents are authoritative.

**Required documentation task before Phase 1:** Fill in the reference spreadsheets at `reference/*.csv` (locations, NPCs, items, encounters, flags, spells, psionics, bestiary, companions, factions). Every named character, every named item, every stated mechanic. This is the foundation.

## Step 2: Scaffold Godot 4
Create the project. Build the directory structure from Section 16. Implement GameState as a singleton first — everything else depends on it.

## Step 3: Story Engine First
Before any art, before any combat, before anything visual: get a text-only story engine running. JSON-driven scenes. Flag tracking. Choice resolution. If Chapter 1 Scene 1 (Party arrives in the Arena, Announcer speaks) is playable as text with working flag setting, the foundation is solid.

## Step 4: Combat Second
The combat grid. Turn queue. THACØ resolution as per the AD&D math in Section 6. One enemy type (Drajian Guard). Win/lose state. This is the walking skeleton.

## Step 5: Everything Else
Art, audio, companions, factions — all build on working story and combat.

## Critical Context for Claude Code Sessions

- **The game is set in DRAJ under TECTUKTITLAY.** Earlier GDD versions (v0.1, v0.2) were wrong about this. This file is the corrected, authoritative version.
- **The three-layer tagging system** ([ORIGINAL]/[EXPANDED]/[NEW]) must be respected in all story development.
- **The source PDFs live in Google Drive at `Game Design/DS/`** and should be consulted directly when any story question arises.
- **The project owner knows the original game intimately.** When in doubt about a story beat, ask.
- **This is a non-commercial fan project.** Dark Sun IP belongs to Wizards of the Coast / Hasbro.

---

*Master Project File — Complete Edition v1.0*
*Compiled from: ds_shatterland_manual_pdf.pdf (SSI, 1993) + ds_shatterland_cluebook_pdf.PDF (SSI, 1996)*
*Original Dark Sun setting: Troy Denning & Timothy Brown for TSR, Inc.*
*Original game: Strategic Simulations Inc. (SSI), 1993*
*Dark Sun IP belongs to Wizards of the Coast / Hasbro | Non-commercial fan project*
