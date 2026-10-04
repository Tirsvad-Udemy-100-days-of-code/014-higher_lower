"""@file test_game_data.py
@brief Tests for the assignment data set and art.
"""

from higher_lower.art import logo, vs
from higher_lower.constants import (
    KEY_COUNTRY,
    KEY_DESCRIPTION,
    KEY_FOLLOWER_COUNT,
    KEY_NAME,
)
from higher_lower.game_data import data

EXPECTED_KEYS = {KEY_NAME, KEY_FOLLOWER_COUNT, KEY_DESCRIPTION, KEY_COUNTRY}


def test_data_has_fifty_accounts() -> None:
    """@brief The assignment data set has 50 entries."""
    assert len(data) == 50


def test_every_account_has_the_required_keys() -> None:
    """@brief Every entry has exactly the four assignment keys."""
    assert all(set(account) == EXPECTED_KEYS for account in data)


def test_follower_counts_are_positive_integers() -> None:
    """@brief Follower counts are positive integers."""
    assert all(
        isinstance(account[KEY_FOLLOWER_COUNT], int) and account[KEY_FOLLOWER_COUNT] > 0
        for account in data
    )


def test_account_names_are_unique() -> None:
    """@brief No account appears twice."""
    names = [account[KEY_NAME] for account in data]
    assert len(names) == len(set(names))


def test_art_is_available() -> None:
    """@brief The logo and the vs art keep their shape, including backslashes."""
    assert len(logo.splitlines()) == 10
    assert "\\" in logo
    assert len(vs.splitlines()) == 6
    assert "|___/____(_)" in vs
