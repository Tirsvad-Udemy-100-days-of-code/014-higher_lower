# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001], [PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | pending |

---

## Purpose

Identify who is affected by the Higher Lower project and what each needs, using a power/interest grid. Stakeholder IDs are stable and cited by every other artifact.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant; Product Owner, developer and reviewer | Tirsvad | HIGH | HIGH | Manage Closely | A correct, tested, well-documented solution that shows good practice |
| S02 | Udemy coursists | Course participants who share and compare solutions | Udemy community | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names, and README instructions to run it |
| S03 | GitHub viewers | Visitors browsing the repository for ideas | Public | LOW | LOW | Monitor | Clear repository description, topics and README; no runtime dependencies |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, writes and reviews everything.
- **Keep Informed (S02):** no decision power, but they are the main audience; served by README and code clarity.
- **Monitor (S03):** casual visitors; served by repository metadata and a short README.

## Primary Concerns and FURPS+ Mapping

| ID | Concern | FURPS+ attribute |
| --- | --- | --- |
| S01 | Game behaves correctly and is covered by tests | Functionality, Reliability |
| S01 | Planning trail and review records exist | Supportability |
| S02 | Code is readable and uses the assignment's function names | Supportability |
| S02 | Can run the game and tests from the README | Usability |
| S03 | Findable and understandable repository | Usability |
| S03 | Nothing extra to install | Implementation (no runtime dependencies) |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| S01 | Pull request review | Per milestone | Reviewed milestone deliverable | MIL-001 to MIL-004 |
| S02 | README | At release | Run and test instructions | MIL-004 |
| S03 | Repository description, topics, README | At release | Repository metadata | MIL-001, MIL-004 |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| Heavy tooling (Doxygen, review records) versus a simple repository for visitors | S01, S03 | Keep tooling in `docs/` and config files; README stays short and runtime stays dependency-free |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | Correct, tested game | [BC-001] O1, O3 |
| S02 | Readable code, run instructions | [BC-001] O2, O4 |
| S03 | Description, topics, no dependencies | [BC-001] O4, O5 |

## Sign-Off

| Stakeholder | Decision | Date |
| --- | --- | --- |
| S01 | Pending review | |

---

[BC-001]: ./business-case.md
[PP-001]: ./project-plan.md
