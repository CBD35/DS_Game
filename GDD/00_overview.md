# Crimson Sands — Game Design Document
## File 00: High-Level Overview

**Version:** 0.1 (Concept Draft)
**Date:** 2026-04-19
**Studio:** [TBD]
**Target Release:** TBD

---

## 1. Elevator Pitch

> *Crimson Sands* is a turn-based tactical RPG set on a dying desert world where magic kills the land, psionic power is the currency of survival, and every drop of water has a price. You begin as a gladiatorial slave. You end as either the world's savior or its final executioner.

A spiritual successor to *Dark Sun: Shattered Lands* (SSI, 1993), built for modern audiences who want the depth of classic CRPGs without sacrificing brutal honesty about consequences. No chosen-one comfort. No forgiving respawn economy. Every resource, every ally, every moral compromise leaves a permanent mark on the world.

---

## 2. Core Vision Statement

*Crimson Sands* asks a single question: **What would people become in a world that is already ending?**

The answer is not heroic by default. The people of Kharak'thal are pragmatic, cruel, creative, and desperate. The player character is not exempt. The game does not reward virtue automatically — it rewards *competence*, and then asks what you did with it.

We commit to:

- **Systemic depth over scripted spectacle.** The world responds to player actions through interlocking systems, not authored cutscenes.
- **Meaningful scarcity.** Water, food, metal, trust — all limited, all consequential.
- **Moral weight without moral instruction.** The game presents dilemmas. It does not grade your answers.
- **Turn-based tactical combat** as the primary resolution layer — spatial, deliberate, and lethal.
- **Psionic and magical systems** that feel alien and costly, not like re-skinned fantasy fireballs.

---

## 3. Design Pillars

### Pillar 1 — Survive the World
The environment itself is a hostile entity. Heat, thirst, and distance are mechanical challenges equal to any enemy encounter. Expedition planning and resource management are not optional minigames — they are core gameplay loops.

### Pillar 2 — Every Action Has a Cost
Combat damages equipment. Magic depletes the landscape. Psionic use exhausts the mind. Moral choices close doors. The economy of cost and consequence pervades every system.

### Pillar 3 — Power Is Political
Strength matters in Kharak'thal, but it is always in service to someone's agenda. The factions — Sorcerer-Kings, Templars, Merchant Houses, the Veiled Alliance — are not backdrop. They are competing systems the player must navigate, exploit, or destroy.

### Pillar 4 — The Party Is a Lifeboat
Companions are not just combat assets. They carry skills, knowledge, and loyalty that can be lost permanently. Party cohesion under pressure — moral, physical, psychological — is a sustained design concern.

### Pillar 5 — The World Remembers
Player choices alter the game world in visible, persistent ways. Defiling magic leaves scorched earth. Freed slaves form communities — or criminal gangs. Sorcerer-Kings retaliate proportionally to provocation. No action is cosmetic.

---

## 4. Tone and Atmosphere

| Dimension | Target |
|-----------|--------|
| **Mood** | Grim, hot, oppressive — with pockets of desperate beauty |
| **Moral register** | Moral grey throughout; no faction is purely good |
| **Humor** | Dark, rare, character-specific — never undercuts tension |
| **Violence** | Consequential, not gratuitous; tactical, not spectacle |
| **Hope** | Present but fragile — the world *could* be saved, at enormous cost |
| **Aesthetic** | Bone, leather, obsidian, dried blood, crimson sky, amber sand |

**Reference tone works:**
- *Cormac McCarthy — Blood Meridian* (landscape as violence)
- *Gene Wolfe — Book of the New Sun* (dying sun, decadent civilization)
- *Ursula K. Le Guin — The Tombs of Atuan* (spiritual oppression, escape)
- *Frank Herbert — Dune* (ecology as politics, resource as power)

**Explicitly NOT:**
- Grimdark nihilism with no agency
- High fantasy power fantasy
- Post-apocalyptic comedy

---

## 5. Comparable Titles

| Title | What We Learn From It |
|-------|-----------------------|
| *Dark Sun: Shattered Lands* (1993) | Core inspiration — tactical party combat, brutal world, gladiatorial hook |
| *Planescape: Torment* (1999) | Narrative depth, character interiority, willingness to be strange |
| *Baldur's Gate II* (2000) | Party chemistry, faction politics, quest density |
| *Wasteland 3* (2020) | Party tactics, moral faction choices, survival tension |
| *Solasta: Crown of the Magister* (2021) | Modern TB tactical implementation, rules transparency |
| *Tyranny* (2016) | Playing inside an evil empire, faction reputation, moral consequence |
| *XCOM: Enemy Unknown* (2012) | Tension economy, resource scarcity, permadeath stakes |
| *Divinity: Original Sin 2* (2017) | Environmental interaction in tactical combat, origin characters |

**Differentiator:** No competitor combines all four of: psionic overlay on tactical combat, defiler/preserver magical consequence, full survival layer, and faction political economy in a single coherent system.

---

## 6. Scope

### Target Scope (v1.0 Release)
- **Playtime:** 40–60 hours main path; 70–100 hours completionist
- **Map areas:** ~35–40 distinct regions (city-states, dungeon complexes, wasteland stretches, arena venues)
- **Party size:** Up to 4 player-controlled characters (1 protagonist + 3 companions)
- **Companions:** 8 recruitable companions (max 3 active)
- **Quests:** ~80 quests (15 main, 40 side, 25 faction)
- **Enemy types:** ~60 distinct creature types
- **Playable races:** 7
- **Classes:** 8 base classes, multi-class combinations

### Out of Scope (v1.0)
- Multiplayer of any kind
- Procedurally generated dungeons (all content hand-authored)
- Real-time combat mode
- Voice acting (text + ambient audio only for v1.0)

### Platform Targets
| Platform | Priority |
|----------|----------|
| PC (Windows) | Primary |
| PC (Linux) | Day-1 |
| PC (macOS) | Day-1 |
| Steam Deck | Stretch goal post-launch |
| Consoles | Post-launch consideration |

---

## 7. Team Requirements (Estimated)

| Role | Count |
|------|-------|
| Lead Designer / Writer | 1 |
| Systems Designer | 1 |
| Level Designer | 2 |
| Writer | 1 |
| Programmer (Godot) | 2 |
| Technical Artist | 1 |
| 2D Artist (sprites, UI) | 2 |
| Composer / Sound Designer | 1 |
| QA | 2 |

**Total:** ~13 people. Feasible for a well-capitalized indie studio or a mid-size crowdfunded project.

---

## 8. Key Risks

| Risk | Mitigation |
|------|------------|
| Scope creep on systems | Lock core mechanics at prototype stage; defer features to DLC |
| Survival mechanics feel punishing not fun | Extensive playtesting; difficulty modes that tune (not remove) survival |
| Dark Sun IP is Wizards of the Coast property | Setting is *inspired by*, not derived from — original names, original lore, no copyrighted material |
| Turn-based market saturation | Differentiate on setting uniqueness and systemic depth, not genre novelty |
| Narrative tonal inconsistency | Single narrative lead with veto power; style guide enforced |

---

## 9. Document Index

| File | Contents |
|------|----------|
| `01_setting.md` | World of Kharak'thal — history, geography, ecology |
| `02_races.md` | Playable and NPC races |
| `03_classes.md` | Character classes and progression |
| `04_combat.md` | Turn-based tactical combat system |
| `05_psionics.md` | Psionic disciplines and combat overlay |
| `06_magic.md` | Defiler/Preserver system and elemental magic |
| `07_progression.md` | XP, leveling, skills, reputation |
| `08_survival.md` | Water, food, heat, travel, camping |
| `09_narrative.md` | Story structure, NPCs, factions |
| `10_ui_ux.md` | Interface and UX design |
| `11_technical.md` | Engine, rendering, save system, moddability |
