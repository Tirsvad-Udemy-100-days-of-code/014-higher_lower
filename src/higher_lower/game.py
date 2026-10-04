"""@file game.py
@brief The interactive game: what the player sees, what they type, and the game loop.

Input and output go through callables so tests can script a whole game.
"""

import random
from collections.abc import Callable, Sequence

from higher_lower.art import logo, vs
from higher_lower.constants import (
    CHOICE_A,
    CHOICE_B,
    KEY_FOLLOWER_COUNT,
    KEY_NAME,
    MSG_AGAINST_B,
    MSG_COMPARE_A,
    MSG_CORRECT,
    MSG_INVALID_CHOICE,
    MSG_WIN,
    MSG_WRONG,
    PROMPT_GUESS,
    START_SCORE,
)
from higher_lower.game_data import Account, data
from higher_lower.game_logic import (
    check_answer,
    format_data,
    get_random_account,
    pick_pair,
)

InputFunc = Callable[[str], str]
OutputFunc = Callable[[str], None]


def show_round(
    account_a: Account,
    account_b: Account,
    output: OutputFunc = print,
) -> None:
    """@brief Show the two accounts the player compares.

    @param account_a The account shown as A.
    @param account_b The account shown as B.
    @param output Where the text goes.
    """
    output(MSG_COMPARE_A.format(account=format_data(account_a)))
    output(vs)
    output(MSG_AGAINST_B.format(account=format_data(account_b)))


def ask_choice(input_func: InputFunc = input, output: OutputFunc = print) -> str:
    """@brief Ask for A or B until the player gives a valid answer.

    @param input_func Reads one line of input, given the prompt.
    @param output Where the invalid-answer message goes.
    @return "a" or "b", in lower case.
    """
    while True:
        answer = input_func(PROMPT_GUESS).strip().lower()
        if answer in (CHOICE_A, CHOICE_B):
            return answer
        output(MSG_INVALID_CHOICE)


def _pick_next_account(
    accounts: Sequence[Account],
    shown_names: set[str],
    rng: random.Random | None,
) -> Account | None:
    """@brief Draw an account that has not been shown in this game.

    @param accounts All accounts of the game.
    @param shown_names Names of the accounts already shown.
    @param rng Random generator, or None for the default.
    @return A new account, or None if every account has been shown.
    """
    unused = [account for account in accounts if account[KEY_NAME] not in shown_names]
    if not unused:
        return None
    return get_random_account(unused, rng)


def play_game(
    accounts: Sequence[Account] = data,
    rng: random.Random | None = None,
    input_func: InputFunc = input,
    output: OutputFunc = print,
) -> int:
    """@brief Play one game, from the logo to the final score.

    Each account is shown once per game. A right guess adds a point and
    makes B the next A; a wrong guess, or running out of accounts, ends
    the game.

    @param accounts The accounts to play with; needs at least two entries.
    @param rng Random generator; pass a seeded one for a repeatable game.
    @param input_func Reads one line of input, given the prompt.
    @param output Where the text goes.
    @return The final score.
    """
    output(logo)
    score = START_SCORE
    account_a, account_b = pick_pair(accounts, rng)
    shown_names = {account_a[KEY_NAME], account_b[KEY_NAME]}
    while True:
        show_round(account_a, account_b, output)
        guess = ask_choice(input_func, output)
        if not check_answer(
            guess, account_a[KEY_FOLLOWER_COUNT], account_b[KEY_FOLLOWER_COUNT]
        ):
            output(MSG_WRONG.format(score=score))
            return score
        score += 1
        output(MSG_CORRECT.format(score=score))
        next_account = _pick_next_account(accounts, shown_names, rng)
        if next_account is None:
            output(MSG_WIN.format(score=score))
            return score
        account_a, account_b = account_b, next_account
        shown_names.add(next_account[KEY_NAME])
