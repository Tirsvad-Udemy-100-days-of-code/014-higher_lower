"""@file test_game.py
@brief Tests for the game loop, run with scripted input and no real console.
"""

import io
import random
from collections.abc import Callable, Iterable, Sequence

import pytest

from higher_lower import __main__ as entry_point
from higher_lower.art import logo
from higher_lower.game import ask_choice, play_game, show_round
from higher_lower.game_data import Account

ACCOUNTS: list[Account] = [
    {
        "name": "First",
        "follower_count": 30,
        "description": "Test one",
        "country": "Denmark",
    },
    {
        "name": "Second",
        "follower_count": 20,
        "description": "Test two",
        "country": "Norway",
    },
    {
        "name": "Third",
        "follower_count": 10,
        "description": "Test three",
        "country": "Sweden",
    },
]


class FirstRng(random.Random):
    """@brief Random generator that takes the first entries, so a game is fixed."""

    def sample(  # type: ignore[override]
        self, population: Sequence[Account], k: int, **kwargs: object
    ) -> list[Account]:
        """@brief Return the first k entries."""
        return list(population)[:k]

    def choice(self, seq: Sequence[Account]) -> Account:  # type: ignore[override]
        """@brief Return the first entry."""
        return seq[0]


def scripted(answers: Iterable[str]) -> Callable[[str], str]:
    """@brief Make an input function that gives the answers one by one.

    @param answers The answers to give.
    @return A function with the signature of input().
    """
    iterator = iter(answers)
    return lambda _prompt: next(iterator)


def run_game(answers: Iterable[str]) -> tuple[int, str]:
    """@brief Play a fixed game and return the score and everything shown.

    @param answers The answers the player gives.
    @return The final score and the output joined with newlines.
    """
    lines: list[str] = []
    score = play_game(ACCOUNTS, FirstRng(), scripted(answers), lines.append)
    return score, "\n".join(lines)


def test_show_round_shows_both_accounts() -> None:
    """@brief Both accounts are described, with the vs art between them."""
    lines: list[str] = []
    show_round(ACCOUNTS[0], ACCOUNTS[1], lines.append)
    assert lines[0] == "Compare A: First, a Test one, from Denmark."
    assert lines[2] == "Against B: Second, a Test two, from Norway."


@pytest.mark.parametrize("typed", ["a", "A", " a "])
def test_ask_choice_accepts_a(typed: str) -> None:
    """@brief A is accepted in any case and with spaces around it."""
    assert ask_choice(scripted([typed]), lambda _line: None) == "a"


def test_ask_choice_asks_again_after_an_invalid_answer() -> None:
    """@brief Invalid answers are rejected and the player is asked again."""
    lines: list[str] = []
    assert ask_choice(scripted(["x", "", "b"]), lines.append) == "b"
    assert len(lines) == 2


def test_correct_streak_adds_a_point_per_round() -> None:
    """@brief Each right guess adds one to the score and B becomes the next A."""
    score, shown = run_game(["a", "a"])
    assert score == 2
    assert "Current score: 1." in shown
    assert "Compare A: Second" in shown


def test_wrong_first_guess_ends_the_game_with_zero() -> None:
    """@brief A wrong guess ends the game and shows the final score."""
    score, shown = run_game(["b"])
    assert score == 0
    assert "Sorry, that's wrong. Final score: 0" in shown


def test_wrong_guess_after_a_point_keeps_the_score() -> None:
    """@brief The final score is the number of right guesses."""
    score, shown = run_game(["a", "b"])
    assert score == 1
    assert "Final score: 1" in shown


def test_invalid_input_does_not_change_the_round() -> None:
    """@brief An invalid answer is re-asked without ending the game or scoring."""
    score, shown = run_game(["x", "a", "a"])
    assert score == 2
    assert shown.count("Compare A: First") == 1


def test_game_ends_with_a_win_when_the_accounts_run_out() -> None:
    """@brief Using every account ends the game instead of failing."""
    score, shown = run_game(["a", "a"])
    assert score == 2
    assert "You went through every account!" in shown


def test_game_starts_with_the_logo() -> None:
    """@brief The logo is shown first."""
    _score, shown = run_game(["b"])
    assert shown.startswith(logo)


def test_full_game_with_the_assignment_data_ends() -> None:
    """@brief A game with the real data set ends with a final score."""
    lines: list[str] = []
    score = play_game(
        rng=random.Random(5), input_func=lambda _prompt: "a", output=lines.append
    )
    assert score >= 0
    assert "Final score" in lines[-1]


def test_main_plays_a_game(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """@brief main() runs a game on the console."""
    monkeypatch.setattr("sys.stdin", io.StringIO("a\n" * 100))
    entry_point.main()
    assert "Final score" in capsys.readouterr().out


def test_main_leaves_quietly_on_end_of_input(
    monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    """@brief Ctrl+D ends the game with a goodbye, not a traceback."""
    monkeypatch.setattr("sys.stdin", io.StringIO(""))
    entry_point.main()
    assert "Goodbye!" in capsys.readouterr().out
