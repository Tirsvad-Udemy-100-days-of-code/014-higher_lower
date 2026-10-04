# System Sequence Diagram: Play a Game

## Metadata
| Key | Value |
| --- | --- |
| ID | SSD-001 |
| CrossReference | [UC-001], [RC-010] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-04 | Deprecated | Jens Tirsvad Nielsen | S01 | Initial version | [923dde7] |
| 2026-10-04 | Accepted | Jens Tirsvad Nielsen | S01 | Accepted after review RC-010 | pending |

---

## Source Use Case

[UC-001] Play a Game, main success scenario. The alternative flows (invalid answer, tie, no account left) are out of scope for this diagram.

## Diagram

```plantuml
@startuml
actor Player
participant ":System" as System
Player -> System : startGame()
System --> Player : accounts A and B
loop while the guess is right
  Player -> System : makeGuess(choice)
  System --> Player : right, score, new accounts A and B
end
Player -> System : makeGuess(choice)
System --> Player : wrong, final score
@enduml
```

## System Operations Table

| Step | Message (verb phrase) | Parameters | Return | Use case step |
| --- | --- | --- | --- | --- |
| 1 | startGame | none | accounts A and B | 1, 2 |
| 2 | makeGuess | choice (A or B) | right, new score, new accounts A and B | 3, 4, 5, 6 |
| 3 | makeGuess | choice (A or B) | wrong, final score | 3, 7 |

Steps 2 and 3 are the same operation; the loop shows the right-guess outcome repeating, and the last call shows the wrong-guess outcome.

## Lifecycle Notes

A game starts with `startGame` and ends when `makeGuess` returns wrong; the System keeps the score and the current accounts in between.

---

[UC-001]: ./uc.md
[923dde7]: https://git.tirsystem.com/Tirsvad-Udemy-100_days_of_code/014-higher_lower/commit/923dde7dc9b59d2c77eddc88336451193147c557
[RC-010]: ../sqa/reviews/rc-010-ssd-001.md
