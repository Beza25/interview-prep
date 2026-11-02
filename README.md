# interview-prep

Practice code, notes, and plans for interview preparation.

## Layout

- `algorithms/` – algorithm problems and their tests (e.g. `two_pointer_algo.py`: two-sum, three-sum)
- `python/` – Python fundamentals practice and tests
- `system_design/` – system design notes

## Run locally

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```sh
git clone git@github.com:Beza25/interview-prep.git
cd interview-prep
uv sync            # creates .venv and installs dependencies
```

Run a single file:

```sh
uv run python algorithms/two_pointer_algo.py
```

## Run the tests

```sh
uv run pytest                          # all tests (algorithms/ and python/)
uv run pytest algorithms/test_two_pointer_algo.py   # one file
uv run pytest -k three_sum -v          # tests matching a name, verbose
```

Tests can import modules from the repo root (e.g. `from algorithms.two_pointer_algo import two_sum`) because `pythonpath = ["."]` is set in `pyproject.toml`.

In VS Code, tests are also discoverable in the Testing panel (pytest is enabled in `.vscode/settings.json`).

## Lint / format

```sh
uv run ruff check .
uv run ruff format .
```
