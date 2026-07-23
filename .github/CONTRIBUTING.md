# Contributing Guide

Thank you for your interest in contributing to this Python project. This document describes how to set up the development environment, the conventions used by the project, and the workflow expected for issues and pull requests.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Reporting Issues](#reporting-issues)
- [Development Setup](#development-setup)
- [Local Workflow](#local-workflow)
- [Testing](#testing)
- [Documentation](#documentation)
- [Branching Model](#branching-model)
- [Commit Convention](#commit-convention)
- [Pull Request Process](#pull-request-process)
- [Code Review](#code-review)
- [Coding Standards](#coding-standards)
- [Security Reports](#security-reports)
- [Licensing](#licensing)

## Code of Conduct

All contributors are expected to behave professionally and respectfully. Personal attacks, harassment, and discriminatory language are not tolerated. By participating, you agree to uphold a welcoming environment for everyone.

## Ways to Contribute

- Reporting bugs and reproducible issues
- Proposing or implementing new features
- Improving documentation, examples, and tutorials
- Reviewing pull requests and providing constructive feedback
- Suggesting tooling, performance, or security improvements

## Reporting Issues

Before opening a new issue:

1. Search existing issues to avoid duplicates.
2. Confirm the problem reproduces on the latest release or `main`.
3. Use the appropriate issue template.

Please include:

- A clear, descriptive title
- The Python version, OS, and project version or commit
- Minimal reproduction steps and a code snippet when applicable
- Expected vs. actual behavior
- Full stack traces, logs, or screenshots

## Development Setup

This project uses [`uv`](https://docs.astral.sh/uv/) for Python and dependency management.

```bash
# Install uv (one-time setup)
make uv-install

# Clone your fork
git clone https://github.com/<your-username>/<repo>.git
cd <repo>

# Install dependencies and create the virtual environment
uv sync

# Install pre-commit hooks
uv run pre-commit install
```

Supported Python versions are declared in `pyproject.toml`. Use `uv` to manage interpreters when needed:

```bash
uv python install 3.12
```

## Local Workflow

Common tasks are exposed via the `Makefile`. Run `make help` to list all targets. Frequently used ones:

```bash
make fmt       # Run pre-commit hooks (ruff, mdformat, codespell, ty, mypy, ...)
make test      # Run the test suite
make gen-docs  # Generate documentation
make clean     # Remove caches and build artifacts
```

Always run `make fmt` and `make test` before opening a pull request.

## Testing

- Tests are written with **pytest** and live under `tests/`.
- Coverage is enforced at **80%** minimum; new code should not lower the project's coverage.
- Use `pytest-xdist` for parallel execution where helpful.

Useful commands:

```bash
uv run pytest                       # Run all tests
uv run pytest tests/test_foo.py     # Run a single file
uv run pytest -k "expression"       # Run tests matching an expression
uv run pytest --cov                 # Run with coverage
```

Add tests for every behavioral change. Bug fixes should include a regression test.

## Documentation

Documentation uses **Zensical** with `mkdocstrings` and lives under `docs/`. To preview locally:

```bash
make gen-docs
uv run zensical serve  # http://0.0.0.0:9987
```

Update README, docstrings, and examples when changing public behavior. Documentation contributions are first-class and very welcome.

## Branching Model

- `main` is the default branch and must always be releasable.
- Feature branches: `feat/<short-description>`
- Bug fix branches: `fix/<short-description>`
- Documentation branches: `docs/<short-description>`

## Commit Convention

Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/) and **must be written in English**.

Format:

```
<type>(<optional scope>): <short summary>

<optional body>

<optional footer>
```

Allowed types:

| Type       | Purpose                                                 |
| ---------- | ------------------------------------------------------- |
| `feat`     | A new feature                                           |
| `fix`      | A bug fix                                               |
| `refactor` | Code change that neither fixes a bug nor adds a feature |
| `doc`      | Documentation-only changes                              |
| `perf`     | Performance improvement                                 |
| `style`    | Formatting or stylistic changes                         |
| `test`     | Adding or correcting tests                              |
| `chore`    | Build, tooling, or auxiliary changes                    |
| `ci`       | Continuous integration changes                          |
| `revert`   | Reverting a previous commit                             |

Append `!` after the type or include `BREAKING CHANGE:` in the footer to indicate a breaking change. Reference issues with `Closes #123` or `Refs #123`.

## Pull Request Process

1. Ensure your branch is up to date with the target branch.
2. Run `make fmt` and `make test` locally; both must pass.
3. Ensure CI checks pass on the pull request.
4. Use a descriptive title following the commit convention; it is validated by **semantic-pull-request**.
5. Fill out the pull request template, including motivation, summary, and testing notes.
6. Link related issues and design documents.
7. Mark the PR as **draft** while still in progress.
8. Request review only after self-review and a green CI.

Pull requests are typically merged via **squash merge** to keep history linear.

## Code Review

- Address all review comments or explain why a change is not needed.
- Keep discussions technical, focused, and respectful.
- Resolve conversations only after the concern has been addressed.

## Coding Standards

- **Formatting and linting**: handled by `ruff` (configured in `pyproject.toml`)
- **Typing**: `ty` runs first with strict rules; `mypy` (with the Pydantic plugin) runs alongside during the migration; new code should be type-annotated
- **Spelling**: enforced by `codespell` via pre-commit
- **Notebooks**: stripped of outputs by `nbstripout`

Prefer clarity over cleverness, and avoid unrelated refactors in feature or fix pull requests.

## Security Reports

Please **do not** report security vulnerabilities through public issues. Refer to [`SECURITY.md`](./SECURITY.md) for the responsible disclosure process.

## Licensing

By contributing, you agree that your contributions will be licensed under the project's license (see [`LICENSE`](../LICENSE)). Ensure that you have the right to submit any code, content, or assets you contribute.
