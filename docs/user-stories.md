# User Stories

## Metadata
| Key | Value |
| --- | --- |
| ID | US-001 |
| CrossReference | [UCD-001], [UC-001], [BC-001], [MIL-003] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Proposed | Jens Tirsvad Nielsen | S01 | Initial version | [923dde7] |

---

## Purpose and Scope

The stories for epic [MIL-003] (Console game): playing rounds and seeing the result. They support [BC-001] objective O1.

## Story List

### US-001.01 Guess which account has more followers

- **As a** Player, **I want** to guess which of two accounts has more followers and keep playing while I am right, **so that** I can build a streak.
- **Acceptance Criteria:**
  - Given a new game, when it starts, then two different accounts A and B are shown.
  - Given two accounts, when I guess the one with more followers, then my score goes up by one and the next round starts with that account as A and a new account as B.
  - Given an invalid answer, when I submit it, then I am asked again and the round does not change.
- **Traces to:** [UC-001], [MIL-003]
- **Size:** one iteration.

### US-001.02 See my final score

- **As a** Player, **I want** to see my final score when the game ends, **so that** I know how well I did.
- **Acceptance Criteria:**
  - Given a round, when I guess the account with fewer followers, then the game ends and shows my final score.
  - Given every account has been used, when no new account can be shown, then the game ends and shows my final score.
- **Traces to:** [UC-001], [MIL-003]
- **Size:** one iteration.

## INVEST Check

Both stories are Independent of each other in wording, Negotiable in detail, Valuable to the Player, Estimable, Small (one iteration) and Testable through the acceptance criteria. No exceptions.

---

[UCD-001]: ./use-case-diagram.md
[UC-001]: ./uc-001/uc.md
[BC-001]: ./business-case.md
[MIL-003]: ./milestones/mil-003-console-game.md
[923dde7]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/923dde7dc9b59d2c77eddc88336451193147c557
