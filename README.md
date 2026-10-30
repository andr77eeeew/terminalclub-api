<h1>
  <img src="https://terminalclub.pages.dev/favicon.svg" alt="TerminalClub" width="32"
height="32" style="vertical-align: middle;">
  TerminalClub-API
</h1>

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue)](https://www.python.org)
![GitHub License](https://img.shields.io/github/license/andr77eeeew/terminalclub-api)

Backend service for terminal command trainer:
type bash, git and other commands for speed and from memory.

> Early Stage: project structure only, no features yet.

Site: https://terminalclub.pages.dev

## Requirements

- [uv](https://docs.astral.sh/uv/) — installs the right Python version by itself

## Development

Install dependencies:
```bash
uv sync
```

Run tests:
```bash
uv run pytest
```

## Code Quality

The project uses **Ruff** for linting and code formatting, **mypy** for static type checking, and **pre-commit** to automatically run checks before each commit.

### Available Checks

Make sure the project dependencies are installed:

```bash
uv sync
```

**1. Linting (Ruff)**

Check the code for linting errors:

```bash
uv run ruff check
```

**2. Code Formatting (Ruff)**

Check whether the code follows the formatting rules without modifying files:

```bash
uv run ruff format --check
```

To automatically format the code:

```bash
uv run ruff format
```

**3. Type Checking (mypy)**

Run static type checking:

```bash
uv run mypy
```

The files checked by mypy are configured in `pyproject.toml`.

### Pre-commit Hooks

Pre-commit automatically runs all configured checks before each Git commit.

Install the Git hook tool for uv:

```bash
uv tool install pre-commit
```

Install pre commit hook:
```bash
pre-commit install
```

Run all checks manually across the entire repository:

```bash
uv run pre-commit run --all-files
```

Once installed, the hooks run automatically when creating a commit. A commit will be blocked if any check fails.
