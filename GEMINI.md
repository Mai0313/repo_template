# GEMINI.md

This file provides context and guidance for Gemini when working with this repository.

## Project Overview

This is a **Python project template** designed to bootstrap production-ready projects. It features a modern `src/` layout, comprehensive tooling (ruff, mypy, pytest), documentation generation (MkDocs), and a full CI/CD suite using GitHub Actions.

- **Package Name:** `repo_template`
- **Python Version:** 3.11+ (Supports 3.11, 3.12, 3.13, 3.14)
- **Dependency Manager:** `uv`
- **Build System:** `hatchling`
- **Documentation:** MkDocs Material with `mkdocstrings`

## Operational Guidelines

### 1. Environment & Dependencies

This project uses `uv` for dependency management. **Do not use pip directly.**

- **Install uv:** `make uv-install` (or via official script)
- **Install Dependencies:**
    - `uv sync`: Install base dependencies.
    - `uv sync --group dev`: Install development tools (pre-commit, poe, notebook).
    - `uv sync --group test`: Install testing dependencies.
    - `uv sync --group docs`: Install documentation dependencies.
- **Adding Dependencies:**
    - `uv add <package>`: Add a production dependency.
    - `uv add <package> --dev`: Add a development dependency.

### 2. Building and Running

- **CLI Entry Points:**
    - `uv run repo_template`: Run the main CLI.
    - `uv run cli`: Alternative entry point.
- **Build Artifacts:**
    - `uv build`: Creates `dist/` containing wheel and sdist.
- **Docker:**
    - `docker compose up -d app`: Run the application container.
    - `docker compose up -d redis postgresql mongodb mysql`: Start optional local services.

### 3. Quality Assurance (QA)

Strict code quality standards are enforced. Always run these checks before committing.

- **Formatting & Linting:**
    - `make format`: Runs all pre-commit hooks (Ruff, Mypy, etc.). **Required.**
    - `pre-commit run -a`: Equivalent to `make format`.
- **Testing:**
    - `make test`: Runs `pytest` with coverage.
    - `pytest`: Run tests directly.
    - `uv run pytest -n auto`: Run tests in parallel (faster).
- **Type Checking:**
    - Mypy is configured in `pyproject.toml` and runs via pre-commit.
    - Use Pydantic models for strict data validation.

### 4. Documentation

- **Generate Docs:** `make gen-docs` (Uses `scripts/gen_docs.py` to generate API docs).
- **Serve Docs:** `uv run mkdocs serve` (Available at http://localhost:9987).
- **Docstrings:** Follow **Google Style** docstrings.

## Project Structure

- `src/repo_template/`: Main application source code.
    - `cli.py`: Entry point and example logic.
- `tests/`: Test suite (Pytest).
- `docs/`: Documentation source (Markdown).
- `scripts/`: Utility scripts (e.g., `gen_docs.py`).
- `.github/workflows/`: CI/CD definitions.
- `docker/`: Dockerfile and related configs.
- `pyproject.toml`: Configuration for `uv`, `ruff`, `pytest`, `mypy`, `poe`, etc.
- `Makefile`: Shortcuts for common tasks.

## Development Conventions

- **Language:** Python 3.11+.
- **Style:** Follows standard Python conventions (PEP 8) enforced by Ruff.
    - Functions/Variables: `snake_case`
    - Classes: `PascalCase`
    - Constants: `UPPER_CASE`
- **Type Hinting:** Mandatory for public functions. Use standard Python typing + Pydantic.
- **Commit Messages:** Must follow **Conventional Commits** (e.g., `feat: add new feature`, `fix: resolve bug`).
    - PR titles are linted in CI.
- **Testing:** New features must include tests. Coverage threshold is **80%**.

## Key Files for Context

- `pyproject.toml`: The central configuration file. Read this to understand tool settings.
- `Makefile`: Defines the standard command interface.
- `CLAUDE.md`: Contains detailed instructions for AI coding assistants (highly relevant reference).
- `AGENTS.md`: Context for AI agents.

---

**Note:** When generating code, ensure it is fully typed, formatted according to project rules, and includes necessary Pydantic models.
