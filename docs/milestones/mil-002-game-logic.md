# MIL-002 Game logic

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001], [PP-001], [RC-005] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [ddfe96f] |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-005 | pending |

---

## Purpose

Decide whether the game's data and pure functions are correct and tested before the interactive loop is built on them.

## Deliverable

The assignment data set and art as modules, constants in `constants.py`, and the pure functions `get_random_account`, `pick_pair`, `format_data` and `check_answer`, all with Doxygen comments and pytest tests.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | Data module holds the 50 assignment entries with `name`, `follower_count`, `description`, `country` | 50 entries, all keys | Count or keys differ |
| 2 | `logo` and `vs` art are available unchanged | Present | Missing or altered |
| 3 | Magic strings and numbers live in `constants.py` | None left in logic modules | Any left |
| 4 | `pick_pair` never returns the same entry twice | Verified by test | Can repeat |
| 5 | `check_answer` returns correct result for A, B and equal counts | Verified by tests | Any wrong |
| 6 | `pytest` passes; every public function has a Doxygen comment | Exit code 0, comments present | Fails or missing |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | Needs the package layout, pytest and constants module |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O2, O3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-09 — second window of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add game data module | Store the assignment's list of 50 dictionaries (`name`, `follower_count`, `description`, `country`) verbatim in `src/higher_lower/game_data.py` as `data`. Order is kept as given; the game compares counts, not position. | No | |
| 2 | Add ASCII art module | Store `logo` and `vs` from the assignment in `src/higher_lower/art.py`, unchanged (raw strings so backslashes survive). | No | |
| 3 | Define constants | Put in `constants.py` the account dictionary keys, choice letters `"a"`/`"b"`, prompt and message texts, and the starting score, so the logic modules hold no magic values. | No | |
| 4 | Implement pair selection | `get_random_account()` returns a random entry; `pick_pair()` returns two distinct entries. Accept an injectable `random.Random` so tests are deterministic. | No | |
| 5 | Implement format_data and check_answer | `format_data(account)` returns "name, a description, from country"; `check_answer(guess, a_followers, b_followers)` returns whether the guess is right, using the assignment's names. Ties count as correct for either choice. | No | |
| 6 | Write unit tests for game logic | pytest tests for the data shape (50 entries, required keys), distinct pairs, `format_data` output and `check_answer` for A higher, B higher and equal. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-001]: ./mil-001-project-setup.md
[ddfe96f]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/ddfe96ffa459d5e4b2e30d71bd53878aba2cfc5d
[RC-005]: ../sqa/reviews/rc-005-mil-002.md
