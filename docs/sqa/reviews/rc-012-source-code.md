# SQA Review Record: Source code of higher_lower

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-012 |
| CrossReference | [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Initial version | [267e34f] |

---

## Artifact Under Review

- Instance reviewed: the Python source in `src/higher_lower/` and `tests/` at the commit of this review (source code has no artifact ID)
- Checklist used: [QC-PY-001]

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | Modules and functions snake_case, constants UPPER_SNAKE, TypedDict PascalCase; ruff (E, F, I, UP, FLY, B) passes. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names say purpose (check_answer, pick_pair); i/n-style names are not used. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | `ruff check` and `ruff format --check` pass; the only suppression is E501 for the verbatim data file, with a comment in pyproject.toml. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All signatures annotated; `mypy --strict src tests` reports no issues. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No bare except; `main` catches EOFError and KeyboardInterrupt on purpose and leaves with a goodbye. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; the data list default is a read-only module constant. |
| 7 | Files, locks and connections are managed with context managers | N-A | The code opens no files, locks or connections. |
| 8 | Public modules, classes and functions have docstrings that say what, not how (Optional) | Pass | Every module, class and function has a Doxygen docstring; checked with an AST script. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | N-A | The game prints its interface to the console; there is no logging, and no secrets or personal data are printed. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | No Design Class Diagram exists or is planned; the only class is the Account TypedDict, and the functions implement the operations of SSD-001. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 36 pytest tests named for behaviour, with scripted input and seeded randomness; no network, no order dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment (Optional) | Pass | mypy strict runs without errors; no Any is used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused (Optional) | Pass | No runtime dependencies; dev tools declared in pyproject.toml with version ranges. |

## Overall Verdict

Go — all applicable criteria pass. The review found a lint ordering error, format differences and strict-typing errors; they were fixed before this verdict (ruff import order and format, `Final` on the account key constants). Reviewer and author are both S01: the project has a single participant, so the framework's author/reviewer separation cannot be met. S01 accepted this deviation when requesting acceptance (2026-10-04).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | — | — |

---

[QC-PY-001]: ../../../framework/qc/qc-programming-python.md
[267e34f]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/267e34fc9f1fb9d76cc20032f3b09dc8e9dd82c7
