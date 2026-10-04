# MIL-003 Console game

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Decide whether the game can be played from start to finish in the console, with score tracking and robust input handling.

## Deliverable

An interactive console game started with `python -m higher_lower`, built on the [MIL-002] functions, with automated tests of the game loop.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `python -m higher_lower` shows logo, Compare A, `vs` art, Against B and a prompt | All shown | Any missing |
| 2 | A correct guess increases the score by one and B becomes the next A | Verified by test | Not so |
| 3 | A wrong guess ends the game and shows the final score | Verified by test | Not so |
| 4 | Invalid input is rejected and re-asked, never crashes | Verified by test | Crash or accepted |
| 5 | Game ends gracefully if the data runs out | Verified by test | Error |
| 6 | `pytest` passes; no runtime dependencies added | Exit code 0 | Fails |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | Uses the data, art, constants and logic functions |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| O1, O3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 |

## Target Date

2026-10-12 — third window of [PP-001].

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Implement display and input helpers | A function that prints the logo, "Compare A: ...", the `vs` art and "Against B: ..." using `format_data`, and one that asks for "A" or "B" and re-asks until valid (case-insensitive). Input and output go through injectable callables so tests need no real console. | No | |
| 2 | Implement the game loop | `play_game()` keeps the score, starts with a random pair, compares guesses with `check_answer`, moves B to A after a correct guess and picks a new B that differs from A. Prints the score after each round and "Sorry, that's wrong. Final score" at the end. | Yes | UC-001 Play a game (to be created with the SSD before this task starts) |
| 3 | Handle exhausted data | If every account has been used, end the game with a win message instead of failing to find a new B. | No | |
| 4 | Add entry point | `python -m higher_lower` runs `main()`, which calls `play_game()`; no side effects on import. | No | |
| 5 | Write game loop tests | pytest tests with scripted input and a seeded random generator: correct streak, wrong first guess, invalid input then valid, data exhausted, and the score printed. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[MIL-002]: ./mil-002-game-logic.md
