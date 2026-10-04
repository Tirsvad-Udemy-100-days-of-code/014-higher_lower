"""@file __main__.py
@brief Entry point for `python -m higher_lower`.
"""

from higher_lower.constants import MSG_GOODBYE
from higher_lower.game import play_game


def main() -> None:
    """@brief Play a game; leave quietly if the player quits with Ctrl+C or Ctrl+D."""
    try:
        play_game()
    except (EOFError, KeyboardInterrupt):
        print()
        print(MSG_GOODBYE)


if __name__ == "__main__":
    main()
