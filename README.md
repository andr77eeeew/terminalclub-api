<h1>
  <img src="https://terminalclub.pages.dev/favicon.svg" alt="TerminalClub" width="32"
height="32" style="vertical-align: middle;">
  TerminalClub-API
</h1>

[![Python Version](https://img.shields.io/badge/python-3.14%2B-blue)](https://www.python.org)
![GitHub License](https://img.shields.io/github/license/andr77eeeew/terminalclub-api)
[![CI](https://github.com/andr77eeeew/terminalclub-api/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/andr77eeeew/terminalclub-api/actions/workflows/ci.yml)

Backend service for terminal command trainer:
type bash, git and other commands for speed and from memory.

> Early Stage: application skeleton with a health check endpoint, no features yet.

Site: https://terminalclub.pages.dev

## Requirements

- [uv](https://docs.astral.sh/uv/) **0.13.6** — pinned via `required-version` in `pyproject.toml`; a different version will refuse to run. Installs the right Python version by itself.

Check your version and update if needed:

```bash
uv --version
uv self update 0.13.6
```

`uv self update` works if uv was installed with the official installer. If you installed it via pip, winget, Homebrew etc., update it through the same tool.

## Configuration

Settings are read from environment variables with the `TERMINALCLUB_` prefix or from a `.env` file in the current working directory (run commands from the project root). See `.env.example`.

| Variable | Description | Default |
|---|---|---|
| `TERMINALCLUB_DOCS_ENABLED` | Serve API docs at `/docs`, `/redoc` and `/openapi.json` | `false` |

## Development

Install dependencies:
```bash
uv sync
```

Run tests:
```bash
uv run pytest
```

Create a local config from the example:

```bash
cp .env.example .env
```

Run the development server:

```bash
uv run uvicorn terminalclub_api.main:create_app --factory --reload
```

- `--factory` — `create_app` is an application factory, so uvicorn calls it to get the app
- `--reload` — restarts the server on code changes (development only)

The server starts at http://127.0.0.1:8000.

Check that it's running:

```bash
curl http://127.0.0.1:8000/health
# {"status":"ok"}
```

Interactive API docs: http://127.0.0.1:8000/docs (only when `TERMINALCLUB_DOCS_ENABLED=true`, see [Configuration](#configuration))

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

Install pre-commit as a uv tool:

```bash
uv tool install pre-commit==4.7.0
```

Set up the Git hooks:

```bash
pre-commit install
```

Run all checks manually across the entire repository:

```bash
pre-commit run --all-files
```

Once installed, the hooks run automatically when creating a commit. A commit will be blocked if any check fails.
