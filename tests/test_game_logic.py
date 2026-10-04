"""@file test_game_logic.py
@brief Tests for the pure game functions.
"""

import random

import pytest

from higher_lower.constants import KEY_NAME
from higher_lower.game_data import Account, data
from higher_lower.game_logic import (
    check_answer,
    format_data,
    get_random_account,
    pick_pair,
)


def test_get_random_account_returns_an_entry_of_the_data() -> None:
    """@brief The drawn account comes from the data set."""
    assert get_random_account(rng=random.Random(1)) in data


def test_get_random_account_is_repeatable_with_a_seed() -> None:
    """@brief The same seed draws the same account."""
    assert get_random_account(rng=random.Random(7)) == get_random_account(
        rng=random.Random(7)
    )


def test_pick_pair_never_returns_the_same_account() -> None:
    """@brief A and B are always different entries."""
    rng = random.Random(0)
    for _ in range(200):
        first, second = pick_pair(rng=rng)
        assert first[KEY_NAME] != second[KEY_NAME]


def test_pick_pair_with_two_accounts_returns_both() -> None:
    """@brief With only two accounts, the pair holds both of them."""
    two = data[:2]
    first, second = pick_pair(two, random.Random(3))
    assert {first[KEY_NAME], second[KEY_NAME]} == {a[KEY_NAME] for a in two}


def test_pick_pair_with_one_account_raises() -> None:
    """@brief A pair cannot be drawn from a single account."""
    with pytest.raises(ValueError):
        pick_pair(data[:1])


def test_format_data_describes_the_account() -> None:
    """@brief The description holds name, description and country."""
    account: Account = {
        "name": "Nike",
        "follower_count": 109,
        "description": "Sportswear multinational",
        "country": "United States",
    }
    assert (
        format_data(account)
        == "Nike, a Sportswear multinational, from United States"
    )


@pytest.mark.parametrize(
    ("guess", "a_followers", "b_followers", "expected"),
    [
        ("a", 200, 100, True),
        ("a", 100, 200, False),
        ("b", 100, 200, True),
        ("b", 200, 100, False),
        ("A", 200, 100, True),
        ("B", 100, 200, True),
        ("a", 100, 100, True),
        ("b", 100, 100, True),
    ],
)
def test_check_answer(
    guess: str, a_followers: int, b_followers: int, expected: bool
) -> None:
    """@brief The answer is right for the higher account, and for either on a tie."""
    assert check_answer(guess, a_followers, b_followers) is expected


def test_check_answer_rejects_an_unknown_choice() -> None:
    """@brief A guess other than a or b is an error."""
    with pytest.raises(ValueError):
        check_answer("c", 1, 2)
