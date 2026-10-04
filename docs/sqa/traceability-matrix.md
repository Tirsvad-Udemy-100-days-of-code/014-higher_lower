# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Added RC-006 and the UC-001 artifacts | [923dde7] |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Added RC-007 to RC-010 for UCD-001, US-001, UC-001 and SSD-001 | [c7164fe] |

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
| [MIL-003] | MIL | [BC-001], [PP-001], [MIL-002], [US-001] | [UC-001] | [RC-006] |
| [MIL-004] | MIL | [BC-001], [PP-001] | - | - |
| [UCD-001] | UCD | [SA-001], [BC-001] | [US-001], [UC-001] | [RC-007] |
| [US-001] | US | [UCD-001], [BC-001], [MIL-003] | [UC-001] | [RC-008] |
| [UC-001] | UC | [UCD-001], [US-001], [SA-001] | [SSD-001] | [RC-009] |
| [SSD-001] | SSD | [UC-001] | - | [RC-010] |

## Coverage Notes

- No domain model or design artifacts exist yet.
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
[RC-005]: ./reviews/rc-005-mil-002.md
[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[UC-001]: ../uc-001/uc.md
[SSD-001]: ../uc-001/ssd.md
[RC-006]: ./reviews/rc-006-mil-003.md
[923dde7]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/923dde7dc9b59d2c77eddc88336451193147c557
[RC-007]: ./reviews/rc-007-ucd-001.md
[RC-008]: ./reviews/rc-008-us-001.md
[RC-009]: ./reviews/rc-009-uc-001.md
[RC-010]: ./reviews/rc-010-ssd-001.md
[c7164fe]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/c7164feab1333951bf6f557baf95a26764656be0
