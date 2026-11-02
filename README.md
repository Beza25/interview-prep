# interview-prep

Practice code, notes, and plans for interview preparation.

## Layout

- `algorithms/` – algorithm problems and their tests
- `python/` – Python fundamentals practice and tests
- `system_design/` – system design notes
- `context/` – prep context and study plan

## Run locally

Requires Python 3.13+ and [uv](https://docs.astral.sh/uv/).

```sh
git clone git@github.com:Beza25/interview-prep.git
cd interview-prep
uv sync            # creates .venv and installs dependencies
```

Run a single file:

```sh
uv run python algorithms/twosum.py
```

## Run the tests

```sh
uv run pytest                          # all tests (algorithms/ and python/)
uv run pytest python/test_day_01_basics.py   # one file
uv run pytest -k two_sum -v            # tests matching a name, verbose
```

In VS Code, tests are also discoverable in the Testing panel (pytest is enabled in `.vscode/settings.json`).

## Lint / format

```sh
uv run ruff check .
uv run ruff format .
```
