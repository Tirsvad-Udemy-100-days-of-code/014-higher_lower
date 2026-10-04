# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [a1ff735] |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Added RC-005 review of MIL-002 | [ee58fcd] |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case traceability
target is measurable. A row is added or updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- |
| [BC-001] | BC | - | [SA-001], [PP-001] | [RC-001] |
| [SA-001] | SA | [BC-001] | [PP-001] | [RC-002] |
| [PP-001] | PP | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | [RC-003] |
| [MIL-001] | MIL | [BC-001], [PP-001] | - | [RC-004] |
| [MIL-002] | MIL | [BC-001], [PP-001], [MIL-001] | - | [RC-005] |
| [MIL-003] | MIL | [BC-001], [PP-001] | - | - |
| [MIL-004] | MIL | [BC-001], [PP-001] | - | - |

## Coverage Notes

- No use cases, user stories or design artifacts exist yet (UC-001 is planned for MIL-003).
- `-` in Upstream means foundational; in Downstream, nothing is built on it yet; in Last Reviewed, no `RC-*` exists yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-project-setup.md
[MIL-002]: ../milestones/mil-002-game-logic.md
[MIL-003]: ../milestones/mil-003-console-game.md
[MIL-004]: ../milestones/mil-004-docs-release.md
[RC-001]: ./reviews/rc-001-business-case.md
[RC-002]: ./reviews/rc-002-stakeholder-analysis.md
[RC-003]: ./reviews/rc-003-project-plan.md
[RC-004]: ./reviews/rc-004-mil-001.md
[a1ff735]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/a1ff73580fdcfad5bbb3854298fdfa0c16ada853
[RC-005]: ./reviews/rc-005-mil-002.md
[ee58fcd]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/ee58fcdc1c9c83b0721022d623e4989591a47987
