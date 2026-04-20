# Crimson Sands — Game Design Document
## 00: Overview & Vision

**Version:** 0.1 (Pre-Production)
**Last Updated:** 2026-04-19
**Document Owner:** Design Lead

---

## Table of Contents
1. [Elevator Pitch](#elevator-pitch)
2. [Design Pillars](#design-pillars)
3. [Tone & Aesthetic](#tone--aesthetic)
4. [Comparable Titles](#comparable-titles)
5. [Scope & Target Audience](#scope--target-audience)
6. [High-Level Feature List](#high-level-feature-list)
7. [Out of Scope](#out-of-scope)

---

## Elevator Pitch

**Crimson Sands** is a turn-based tactical RPG set in Kharak'thal — a dying desert world where the sun bleeds red, metal is rarer than water, and magic devours the earth itself. Players begin as gladiatorial slaves, escape into a brutal wilderness of psychic predators and scheming city-states, and uncover a conspiracy that could hasten the world's final death.

It is a spiritual successor to *Dark Sun: Shattered Lands* (SSI, 1993), rebuilt for a modern audience with the tactical depth of *Solasta*, the narrative ambition of *Baldur's Gate 3*, and the uncompromising survival pressure of *Darkest Dungeon*. Every decision costs something. The world remembers what you take from it.

**Tagline:** *"Everything here wants to kill you. The world is next."*

---

## Design Pillars

These five pillars govern all design decisions. When in conflict, earlier pillars take precedence.

### Pillar 1: Consequence is Physical
Every system must produce visible, tangible consequences in the world. A wizard who defiles leaves scorched earth. A party that drinks the last water at an oasis leaves nothing for the next traveler — and may meet that traveler later, dying. Resources are finite. Choices persist.

### Pillar 2: Brutality with Agency
Kharak'thal is merciless, but players are never helpless. Difficulty comes from hard choices, incomplete information, and resource scarcity — not arbitrary punishment. A fight you cannot win can still be survived, fled, or bypassed. Intelligence and preparation should always matter.

### Pillar 3: Tactical Depth Without Bloat
Combat must reward positioning, resource management, and ability synergy. Every class, race, and psionic discipline should offer distinct tactical options. But complexity must be legible: new players can function with basic tactics; veterans can squeeze every edge from the system.

### Pillar 4: World as Character
Kharak'thal is not a backdrop — it is a dying organism the player is embedded in. The survival layer, the ecology, the political factions, and the magic system are all expressions of the same core truth: this world is being consumed, and player choices either slow or accelerate that process.

### Pillar 5: Authentic Darkness
No redemption arcs handed out for free. The setting is post-apocalyptic fantasy at its most unromantic: slavery is the economic foundation, genocide is historical fact, and the most powerful beings in the world maintain that power through sustained atrocity. The game does not apologize for this, but it gives players the agency to push back — at real cost.

---

## Tone & Aesthetic

### Tone
- **Genre:** Grim dark / Sword & Sorcery / Post-Apocalyptic Fantasy
- **Emotional register:** Tense, oppressive, occasionally cathartic. Not nihilistic — there is meaning in resistance even when victory is uncertain.
- **Violence:** Present, impactful, never gratuitous. Death matters. Injury matters.
- **Humor:** Rare and dark. Gallows wit from characters who have survived too much to be shocked anymore.

### Visual Style
- Isometric perspective, hand-painted textures with a desaturated warm palette: ochres, siennas, bone whites, and the deep crimson of the dying sun.
- UI inspired by bone, obsidian, and stretched hide — no steel or chrome anywhere.
- Particle effects for psionic abilities: shimmer and heat-distortion rather than flashy lights.
- Defiling magic: visible ashen rings expanding from the caster, flora wilting in real time.

### Audio
- Percussion-heavy soundtrack with Middle Eastern, North African, and Central Asian instrumentation. No orchestral swell — intimate and harsh.
- Ambient sound design prioritizing wind, sand, insect clicks (Thri-Kreen), and distant roars.
- Voice acting for key NPCs only. Player party uses grunts, effort sounds, and short contextual barks.

### Reference Points (Aesthetic)
- Paintings: Frank Frazetta desert pieces, Brom original Dark Sun illustrations
- Films: Mad Max: Fury Road, Conan the Barbarian (1982), Lawrence of Arabia
- Games: Dark Sun: Shattered Lands, Planescape: Torment, Darkest Dungeon

---

## Comparable Titles

| Title | What We Share | What We Do Differently |
|---|---|---|
| Dark Sun: Shattered Lands (1993) | Setting tone, tactical combat, resource scarcity | Modern UI/UX, expanded psionic system, full survival layer |
| Baldur's Gate 3 | Party-based tactical RPG, D&D-derived rules, reactive world | Isometric only, harder survival, no gods or divine magic |
| Solasta: Crown of the Magister | Turn-based combat depth, environmental interaction | Far darker tone, survival mechanics, original rule system |
| Darkest Dungeon | Attrition-based resource management, morale system | Full tactical CRPG scope, open world, narrative complexity |
| Pathfinder: Wrath of the Righteous | Deep class/build system, long-form narrative | Single world, no mythic power, survival-first design |
| Divinity: Original Sin 2 | Environmental combat, origin characters | No elemental spell combos gimmick, grittier tone, scarcity-focused |

---

## Scope & Target Audience

### Target Audience
- **Primary:** CRPG enthusiasts aged 25–45 with nostalgia for or knowledge of late-era SSI titles, Planescape, and Baldur's Gate.
- **Secondary:** Tactical RPG players (XCOM, Into the Breach, Solasta) drawn to deeper narrative.
- **Tertiary:** Dark Sun tabletop players wanting a faithful video game adaptation of the setting.

### Platform Targets
- **PC (Windows/Linux/macOS):** Primary — all development, QA, and optimization targets.
- **Steam Deck:** Verified target. UI must support controller input at 1280x800 resolution.
- **Console (PS5/Xbox Series X):** Stretch goal, post-launch port.

### Team Size Assumption
Small-to-mid indie studio: 15–25 people. GDD is scoped for a 3–4 year production cycle.

### Scope Summary

| Category | Target |
|---|---|
| Campaign Length | 40–60 hours (main story + side content) |
| Playable Races | 7 (6 core + 1 original: the Ssurrai) |
| Character Classes | 8 |
| Unique Maps/Areas | 60–80 handcrafted |
| Major Factions | 5 (+ several minor) |
| Acts | 3 |
| Major Ending Variants | 4 with epilogue slides |
| Languages at Launch | English; French, German, Spanish planned |

---

## High-Level Feature List

### Core Features (Must Ship)
- Turn-based tactical combat on tile-based isometric maps
- Full party creation (up to 4 player-controlled characters)
- 8 character classes with distinct mechanical identities
- 7 playable races with meaningful stat and ability differences
- Psionic system (parallel to but distinct from arcane magic)
- Defiler/Preserver moral split in wizard magic with world-state consequences
- Survival layer: water, food, heat exposure, encumbrance
- 3-act narrative with branching faction allegiances
- Reactive world: resource depletion, political consequences, reputation tracking
- Arena/gladiatorial combat mode with unique rules
- 5 major factions with relationship meters and distinct quest lines

### Secondary Features (High Priority)
- Companion characters with full dialogue trees and personal quests
- Procedurally generated random encounters in wilderness travel
- Crafting system using bone, obsidian, and chitin — no metal
- New Game+ mode with escalating difficulty modifiers
- Bestiary that populates as enemies are encountered or studied

### Stretch Features (Post-Launch or If Schedule Allows)
- Modding SDK exposing Godot 4 project structure
- Additional playable origin stories (2–3 pre-written backstories)
- Multiplayer co-op for tactical combat (narrative remains single-player)

---

## Out of Scope

The following are explicitly excluded from Crimson Sands v1.0:

- **Real-time or real-time-with-pause combat.** This is a turn-based game, always.
- **3D world exploration.** Movement between areas is map-based with survival tracking. Only combat encounters and town scenes use isometric rendering.
- **Gods or divine magic.** Kharak'thal has no gods. Cleric magic is entirely elemental.
- **Metal equipment.** If a piece of content requires ferrous weapons or armor, it does not belong.
- **Multiplayer narrative modes.** Co-op, if implemented, is combat-only and post-launch.
- **Procedurally generated story content.** All narrative content is handcrafted.
- **Alignment system.** Replaced entirely by the Reputation/Infamy system (see 07_progression.md).
- **Open-world free roam.** World travel is node-based with survival resource tracking between nodes.

---

## Project Philosophy Note

Dark Sun: Shattered Lands succeeded because it committed to its setting without apology. It did not soften the slavery, explain away the ecological horror, or give players a chosen-one escape hatch from the misery. Crimson Sands must honor that commitment while adding the systemic depth, narrative craft, and interface legibility that modern players expect.

The goal is not nostalgia. The goal is to build the game that Dark Sun always deserved.
