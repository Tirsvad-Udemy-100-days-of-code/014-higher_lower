"""@file art.py
@brief ASCII art shown by the game, as given by the assignment.

The lines are raw strings so the backslashes in the art survive unchanged.
They are concatenated line by line, rather than written as one multi-line
string, so Doxygen does not read the backticks in the art as markup.
"""

## The game logo.
logo = (
    "\n"
    r"    __  ___       __             "
    "\n"
    r"   / / / (_)___ _/ /_  ___  _____"
    "\n"
    r"  / /_/ / / __ `/ __ \/ _ \/ ___/"
    "\n"
    r" / __  / / /_/ / / / /  __/ /    "
    "\n"
    r"/_/ ///_/\__, /_/ /_/\___/_/     "
    "\n"
    r"   / /  /____/_      _____  _____"
    "\n"
    r"  / /   / __ \ | /| / / _ \/ ___/"
    "\n"
    r" / /___/ /_/ / |/ |/ /  __/ /    "
    "\n"
    r"/_____/\____/|__/|__/\___/_/     "
    "\n"
)

## The "vs" shown between the two accounts.
vs = (
    "\n"
    r" _    __    "
    "\n"
    r"| |  / /____"
    "\n"
    r"| | / / ___/"
    "\n"
    r"| |/ (__  ) "
    "\n"
    r"|___/____(_)"
    "\n"
)
