"""@file game_logic.py
@brief Pure functions of the game: drawing accounts, describing them and checking guesses.
"""

import random
from collections.abc import Sequence

from higher_lower.constants import (
    ACCOUNT_TEMPLATE,
    CHOICE_A,
    CHOICE_B,
    KEY_DESCRIPTION,
    KEY_NAME,
    KEY_COUNTRY,
)
from higher_lower.game_data import Account, data

_DEFAULT_RNG = random.Random()


def get_random_account(
    accounts: Sequence[Account] = data,
    rng: random.Random | None = None,
) -> Account:
    """@brief Return one random account.

    @param accounts The accounts to draw from.
    @param rng Random generator; pass a seeded one to make the draw repeatable.
    @return A random entry of accounts.
    """
    return (rng or _DEFAULT_RNG).choice(accounts)


def pick_pair(
    accounts: Sequence[Account] = data,
    rng: random.Random | None = None,
) -> tuple[Account, Account]:
    """@brief Return two different random accounts.

    @param accounts The accounts to draw from; needs at least two entries.
    @param rng Random generator; pass a seeded one to make the draw repeatable.
    @return The accounts A and B, never the same entry.
    @throws ValueError If accounts has fewer than two entries.
    """
    first, second = (rng or _DEFAULT_RNG).sample(accounts, 2)
    return first, second


def format_data(account: Account) -> str:
    """@brief Describe an account for the player.

    @param account The account to describe.
    @return Text such as "Nike, a Sportswear multinational, from United States".
    """
    return ACCOUNT_TEMPLATE.format(
        name=account[KEY_NAME],
        description=account[KEY_DESCRIPTION],
        country=account[KEY_COUNTRY],
    )


def check_answer(guess: str, a_followers: int, b_followers: int) -> bool:
    """@brief Tell whether the guess names the account with more followers.

    Equal follower counts make either choice correct.

    @param guess "a" or "b", in any case.
    @param a_followers Follower count of account A.
    @param b_followers Follower count of account B.
    @return True if the guess is right.
    @throws ValueError If guess is neither "a" nor "b".
    """
    choice = guess.lower()
    if choice == CHOICE_A:
        return a_followers >= b_followers
    if choice == CHOICE_B:
        return b_followers >= a_followers
    raise ValueError(f"guess must be {CHOICE_A!r} or {CHOICE_B!r}, got {guess!r}")
