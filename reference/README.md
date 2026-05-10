# Reference Spreadsheets

Source-of-truth tables for *Dark Sun: Shattered Lands Reborn*. These are skeletons — they're seeded with examples drawn from the v1.0 Master Project File, but must be filled in by reading the cluebook (`Game Design/DS/ds_shatterland_cluebook_pdf.PDF`) and manual (`ds_shatterland_manual_pdf.pdf`) end-to-end.

## How to use

- All files are CSV. Open in Google Sheets, Excel, or LibreOffice Calc.
- A copy of each is uploaded to Google Drive at `Game Design/DS/` and auto-converted to Google Sheets.
- The `id` column in each table is a stable string key. Other tables reference these IDs.
- The `source_page` column points back to the page number in the manual or cluebook. Always cite a source.
- Empty rows with just an `id` placeholder are intentional — they're slots to fill in.

## Files

| File | What it tracks | Cross-refs |
|---|---|---|
| `locations.csv` | Every region/area in the game | `npcs.id`, `encounters.id`, `flags.id` |
| `npcs.csv` | Every named character | `locations.id`, `factions.id`, `items.id` |
| `items.csv` | Weapons, armor, magical items, quest items | `locations.id`, `npcs.id` |
| `encounters.csv` | Combat encounters by location | `locations.id`, `bestiary.id` |
| `bestiary.csv` | Monster stat blocks from manual | — |
| `spells_preserver.csv` | Preserver spell list (1–5) | — |
| `spells_cleric.csv` | Cleric spell list (1–5) | — |
| `psionics.csv` | All psionic powers (sciences + devotions) | — |
| `flags.csv` | Story flags to track in GameState | `locations.id` |
| `companions.csv` | Playable companion characters | `locations.id`, `npcs.id` |
| `factions.csv` | Faction reputation tracking | `npcs.id` |

## Conventions

- IDs are `snake_case`, ASCII only.
- Multi-value cells use `;` (semicolon) as separator: `gareth;saria;tarim`
- Layer tags use `O` (Original), `E` (Expanded), `N` (New) per the three-layer system.
- Page numbers are `M-pp` for manual, `C-pp` for cluebook (e.g. `M-19`, `C-15`).
- Missing data: leave the cell empty. Don't write `N/A` or `?` — empty means "needs research."

## Phase 0 task

Before Phase 1 implementation: every NPC named in the cluebook should have a row in `npcs.csv` with location, role, and page number. Every named item should have a row in `items.csv`. Every monster from the manual's bestiary should have a stat block in `bestiary.csv`.
