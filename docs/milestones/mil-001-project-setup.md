# MIL-001 Project setup

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [ddfe96f] |

---

## Purpose

Decide whether the project foundation (configuration, layout, tooling files and repository metadata) is ready for code to be written on top of it.

## Deliverable

`pyproject.toml`, Python `.gitignore`, `Doxyfile`, the `src/`, `tests/`, `docs/` layout with an importable empty package and `constants.py`, a passing smoke test, and the repository description and topics on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares Python `>=3.13`, no runtime dependencies, pytest as a dev dependency | Present | Missing or has runtime dependencies |
| 2 | `.gitignore` excludes `.venv/`, `.env`, `__pycache__/`, `.pytest_cache/`, Doxygen output | All excluded | Any missing |
| 3 | `pip install -e ".[dev]"` and `pytest` succeed in a fresh `.venv` | Exit code 0 | Fails |
| 4 | `Doxyfile` exists and points at `src/` | Present | Missing |
| 5 | Repository has description and topics | Visible on host | Not set |
| 6 | `.env` is not referenced by any file under `src/` or `tests/` | No references | Any reference |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First phase |

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

2026-10-06 — first window of [PP-001], inside the proposed two-week-or-less target.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Create pyproject.toml | Project configuration for a package named `higher_lower` under `src/`: `requires-python = ">=3.13"`, `dependencies = []`, an optional `dev` group with pytest, and pytest settings (`testpaths = ["tests"]`, `pythonpath = ["src"]`). Keeps runtime free of dependencies for S03. | No | |
| 2 | Verify Python .gitignore | A Python `.gitignore` already exists; confirm it ignores `.venv/`, `.env` (token file, personal use only), caches and Doxygen output (`docs/doxygen/`), adding entries where missing. | No | |
| 3 | Create src, tests and docs skeleton | Add `src/higher_lower/__init__.py`, `src/higher_lower/__main__.py` stub, `src/higher_lower/constants.py` (empty module with Doxygen header) and `tests/` with a smoke test importing the package. `docs/` already holds the planning artifacts. | No | |
| 4 | Add Doxyfile | Doxygen configuration with `INPUT = src`, `OUTPUT_DIRECTORY = docs/doxygen`, Python optimisation (`OPTIMIZE_OUTPUT_JAVA = YES`), recursive scan and `EXTRACT_ALL = YES`, so Doxygen comments in the source can be rendered. | No | |
| 5 | Set repository description and topics | Use the Gitea API with the token from `.env` (personal use; the token is never imported, copied or tested by the project) to set a description and topics such as `python`, `udemy`, `100-days-of-code`, `higher-lower`, `game`, `pytest`. Needs S01's go-ahead before it is run. | No | |

---

[BC-001]: ../business-case.md
[PP-001]: ../project-plan.md
[ddfe96f]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/ddfe96ffa459d5e4b2e30d71bd53878aba2cfc5d
