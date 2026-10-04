# Higher Lower

A console game from Udemy's *100 Days of Code: The Complete Python Pro Bootcamp*
(day 14). Two Instagram accounts are shown. Guess which one has more followers.
Every right guess adds a point and the winner stays for the next round. A wrong
guess ends the game.

```
Compare A: Cristiano Ronaldo, a Footballer, from Portugal.

 _    __
| |  / /____
| | / / ___/
| |/ (__  )
|___/____(_)

Against B: Ariana Grande, a Musician and actress, from United States.
Who has more followers? Type 'A' or 'B':
```

- Python 3.13 or newer, no runtime dependencies.
- The function names follow the assignment: `format_data`, `check_answer`.
- Each account is shown once per game; if you get through all 50, you win.
- Follower counts are in millions and come from the assignment's data set.

## Requirements

- [Python](https://www.python.org/downloads/) 3.13 or newer
- Optional: [Doxygen](https://www.doxygen.nl/) to build the source documentation

## Set up

Create a local virtual environment in `.venv`, activate it, and upgrade `pip`.

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

Windows (Git Bash), Linux and macOS:

```bash
python -m venv .venv
source .venv/Scripts/activate   # Linux/macOS: source .venv/bin/activate
python -m pip install --upgrade pip
```

The game itself needs nothing more. To run the tests and the code checks, install the
development tools:

```bash
python -m pip install -e ".[dev]"
```

## Run the game

```bash
python -m higher_lower
```

Type `A` or `B` and press Enter. Press Ctrl+C to quit.

## Run the tests

```bash
python -m pytest
```

Check the code style and types:

```bash
python -m ruff check src tests
python -m ruff format --check src tests
python -m mypy src tests
```

## Build the source documentation

The source uses Doxygen comments. The HTML output goes to `docs/doxygen/html`.

```bash
doxygen Doxyfile
```

## Project layout

| Path | Content |
| --- | --- |
| `src/higher_lower/` | The game: `game_logic.py` (pure functions), `game.py` (the loop), `game_data.py`, `art.py`, `constants.py` |
| `tests/` | pytest tests |
| `docs/` | Planning and review documents (business case, plan, milestones, use case) |
| `pyproject.toml` | Project configuration |
| `Doxyfile` | Doxygen configuration |

## License

GNU Affero General Public License v3.0. See [LICENSE](LICENSE).
