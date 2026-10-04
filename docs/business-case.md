# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001], [PP-001], [RC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [ddfe96f] |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Added target-date constraint and cost-benefit justification<br>Accepted after review RC-001 | pending |

---

## Executive Summary

Build the "Higher Lower" console game from Udemy's 100 Days of Code (day 14) as a small, readable, dependency-free Python project. The player compares two Instagram accounts and guesses which has more followers; a correct guess adds a point and continues, a wrong guess ends the game. The repository is a learning artefact that other course participants and GitHub visitors can read, run and compare against.

## Methodological and Standards Foundation

Planning follows the project's SQA/QC framework (`framework/`): Business Case, Stakeholder Analysis, Project Plan, milestones synced as Gitea Milestones and Issues, then code. Product quality is described with ISO/IEC 25010:2023 characteristics.

## Problem Statement

The course assignment gives only a brief and a data set. Without a structured, tested and documented solution there is nothing to share, compare or reuse, and the practice value of the exercise is lost.

## Business Opportunity

A clean reference solution with the assignment's function names, tests and run instructions lets fellow participants compare approaches, and shows the author's practice of planning-first, tested development.

## Objectives

1. O1 — Deliver a playable console Higher Lower game using the assignment's data set, art and function names.
2. O2 — Keep the code readable: constants in `constants.py`, Doxygen comments in source, Python 3.13+.
3. O3 — Provide pytest tests for the game logic and the game loop.
4. O4 — Provide a README with venv, pip upgrade, run and test instructions, and a Doxyfile.
5. O5 — Publish the repository with a clear description and topics.

## Scope

### In Scope

- Console game: random pair selection, score tracking, one session that ends on a wrong guess.
- Assignment data set (50 entries), `logo` and `vs` ASCII art.
- `src/`, `tests/`, `docs/` layout, `pyproject.toml`, Python `.gitignore`, `Doxyfile`, `README.md`.
- Repository description and topics on the Gitea repository.

### Out of Scope

- Graphical or web user interface.
- Live data from Instagram or Google Trends.
- Persistent high scores.
- Runtime third-party dependencies.
- Committing or pushing (done by the author after review).

## Expected Benefits

### Tangible Benefits

- A runnable, tested repository other participants can clone.
- A reusable planning and documentation trail.

### Intangible Benefits

- Practice in decomposing a problem into small tasks and testing incrementally.
- Visibility of the author's work to GitHub viewers.

## Strategic Alignment

Supports the author's goal of completing the 100 Days of Code bootcamp with professional-quality practice (planning, tests, documentation).

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | Game is playable | A full game runs from `python -m higher_lower` | Manual run |
| 2 | Tests pass | All pytest tests pass | `pytest` exit code 0 |
| 3 | No runtime dependencies | `dependencies = []` in `pyproject.toml` | File inspection |
| 4 | Docs complete | README, Doxyfile and Doxygen comments present | Review record |
| 5 | Repository metadata set | Description and topics visible on the host | Host page |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Token from `.env` leaks into the project | Credential exposure | Keep `.env` gitignored; never import or test it; use only for host sync |
| Data set has entries out of order (e.g. Cardi B, David Beckham) | None for gameplay; may confuse readers | Keep data verbatim; the game compares counts, not list order |
| Same account drawn twice in a round | Meaningless round | Pair selection forces two distinct entries; tested |

## Assumptions

- The README template referenced in the brief will be supplied before the README task starts (see Project Plan open issues).
- Python 3.13 or newer is installed on the author's machine.

## Constraints

- Python 3.13+, `venv`, pytest, `pyproject.toml`, `constants.py`.
- No runtime dependencies unless needed.
- Do not commit, push or open a PR without the author's request.
- Product Owner language: English.
- Target completion 2026-10-14 (proposed by S01; no external deadline).

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| About one to two evenings of the author's time | A shareable, tested, documented reference solution |

The comparison is qualitative on purpose: this is a personal learning project with no revenue or budget, so a monetary ROI would be artificial. The cost is the author's time; the benefit is the shareable reference solution and practice gained.

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Product Owner, developer and reviewer; wants a correct, well-practised solution |
| S02 | Udemy coursists; want readable, runnable code with the assignment's function names |
| S03 | GitHub viewers; want a clear description, topics and README, and no dependencies |

## Recommendation

Proceed — the scope is small, the risks are low and the result serves all three stakeholders.

---

[SA-001]: ./stakeholder-analysis.md
[PP-001]: ./project-plan.md
[ddfe96f]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/ddfe96ffa459d5e4b2e30d71bd53878aba2cfc5d
[RC-001]: ./sqa/reviews/rc-001-business-case.md
