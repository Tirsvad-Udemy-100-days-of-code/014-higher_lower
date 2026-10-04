# UC-001 Play a Game

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001], [SSD-001], [RC-009] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [923dde7] |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-009 | pending |

---

Format: Fully Dressed

## Scope

The Higher Lower console game.

## Level

User goal.

## Primary Actor

Player.

## Stakeholders and Interests

| Stakeholder | Interest |
| --- | --- |
| S01 | A correct game that shows good practice ([SA-001]) |
| S02 | Readable behaviour that matches the assignment ([SA-001]) |

## Preconditions

The Player has started the game.

## Postconditions (Success Guarantee)

The Player has seen the final score of the game.

## Main Success Scenario

1. The Player starts a game.
2. The System shows two different accounts, A and B.
3. The Player guesses which account has more followers.
4. The System tells the Player the guess was right, adds one to the score, and shows the new score.
5. The System makes the account the Player compared against the new A and shows a new B.
6. The Player repeats from step 3 until a guess is wrong.
7. The System tells the Player the guess was wrong and shows the final score.

## Extensions / Alternative Flows

- 3a. The Player gives an answer that is not a valid choice: the System asks again; the round does not change.
- 3b. Both accounts have the same number of followers: either choice counts as right.
- 5a. No account is left that differs from the current A: the System ends the game and shows the final score.

No `<<include>>` or `<<extend>>` use cases apply.

## Special Requirements / Business Rules

- Step 2 and 5: A and B are never the same account.
- Step 3b: equal follower counts make both choices right.

## Open Issues

None.

---

[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[SA-001]: ../stakeholder-analysis.md
[SSD-001]: ./ssd.md
[923dde7]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/923dde7dc9b59d2c77eddc88336451193147c557
[RC-009]: ../sqa/reviews/rc-009-uc-001.md
