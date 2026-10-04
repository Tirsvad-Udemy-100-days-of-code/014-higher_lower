"""@file constants.py
@brief Constants shared by the game modules.
"""

## Keys of an account dictionary.
KEY_NAME = "name"
KEY_FOLLOWER_COUNT = "follower_count"
KEY_DESCRIPTION = "description"
KEY_COUNTRY = "country"

## The two choices the player can type, in lower case.
CHOICE_A = "a"
CHOICE_B = "b"

## Score at the start of a game.
START_SCORE = 0

## How an account is described to the player.
ACCOUNT_TEMPLATE = "{name}, a {description}, from {country}"

## Texts shown to the player.
MSG_COMPARE_A = "Compare A: {account}."
MSG_AGAINST_B = "Against B: {account}."
PROMPT_GUESS = "Who has more followers? Type 'A' or 'B': "
MSG_INVALID_CHOICE = "Please type 'A' or 'B'."
MSG_CORRECT = "You're right! Current score: {score}."
MSG_WRONG = "Sorry, that's wrong. Final score: {score}"
MSG_WIN = "You went through every account! Final score: {score}"
MSG_GOODBYE = "Goodbye!"
