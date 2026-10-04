# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `src/pyeventroute/route.py:4` - the whole "router" is `accept(data)` doing `print(data)`, and `ConfigRoute` (`src/pyeventroute/configs.py:9`) defines no options; the package does not do what `pyproject.toml:15`/README promise ("route events to loggers or to any other place") yet is published to PyPI as `Development Status :: 4 - Beta` (`pyproject.toml:23`); implement the routing (e.g. via `logging`) or mark it `1 - Planning`/`2 - Pre-Alpha`.
- `pyproject.toml:89` - the mypy `ignore_missing_imports` override lists the project's own package `pyeventroute.*`; the package is found via `mypy_path = "src"` (mypy passes on `src tests` without it), so the override only hides future import errors - remove it and keep only `pytconf.*` (which ships no `py.typed`).
- `rsconstruct.toml:28` - `src_dirs` for `ruff` (and `mypy` at `rsconstruct.toml:32`) include `config`, which holds only `.lua` files (mypy reports "There are no .py[i] files in directory 'config'"); drop `config` from both lists.

## Low

- `pyproject.toml:82` - `mypy_path = "src:python:scripts"` names `python/` and `scripts/` directories that do not exist in this repo; reduce it to `"src"`.
- `src/pyeventroute/route.py:4` - `accept` has no type annotations or docstring (mypy `--strict` flags `no-untyped-def`); annotate it as part of implementing it.
- `doc/TODO.txt:1` - empty file; delete it or put the actual open items in it.
