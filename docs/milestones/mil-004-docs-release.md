# MIL-004 Documentation and release

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [ddfe96f] |

---

## Purpose

Decide whether the repository is ready to be shared with S02 and S03: documented, reviewed and verifiable from a clean clone.

## Deliverable

`README.md` with venv, pip upgrade, run and test instructions, a Doxygen build that renders the source comments, review records for the project artifacts, and a verified clean-clone run.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | README follows the supplied template and states how to create `.venv`, run `python -m pip install --upgrade pip`, install, run and test | All present | Any missing |
| 2 | Following the README on a clean clone, the game starts and `pytest` passes | Yes | No |
| 3 | `doxygen Doxyfile` builds without warnings on public functions | No warnings | Warnings |
| 4 | Every reviewed artifact has an `RC-*` record in `docs/sqa/reviews/` | Present | Missing |
| 5 | `pyproject.toml` still lists no runtime dependencies | Empty | Any |
| 6 | No `.env` content or token appears in tracked files | Clean | Found |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | Needs the finished game to document and verify |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O2, O4, O5 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-14 — final window of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Write README.md | Follow the template S01 supplies (still outstanding): what the game is, how to create and activate a local `.venv`, `python -m pip install --upgrade pip`, install with `pip install -e ".[dev]"`, run with `python -m higher_lower`, test with `pytest`, and how to build Doxygen docs. Serves S02 and S03. | No | |
| 2 | Audit Doxygen comments | Check that every module, function and constant group in `src/` has a Doxygen comment (`@brief`, `@param`, `@return`) and that `doxygen Doxyfile` builds cleanly. | No | |
| 3 | Review artifacts and record reviews | Review BC, SA, PP and the milestones against their QC checklists and create `RC-*` records in `docs/sqa/reviews/`; update version history rows to Accepted on a Go. | No | |
| 4 | Verify from a clean clone | In a fresh clone follow the README exactly: create `.venv`, upgrade pip, install, run the game, run pytest. Fix any gap in the README. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-003]: ./mil-003-console-game.md
[ddfe96f]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/ddfe96ffa459d5e4b2e30d71bd53878aba2cfc5d
