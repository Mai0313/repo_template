# Contributing Guide

Thank you for your interest in contributing to this Python project. This document describes how to set up the development environment, the conventions used by the project, and the workflow expected for issues and pull requests.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Ways to Contribute](#ways-to-contribute)
- [Reporting Issues](#reporting-issues)
- [Development Setup](#development-setup)
- [Local Workflow](#local-workflow)
- [Local Services](#local-services)
- [Testing](#testing)
- [Documentation](#documentation)
- [Branching Model](#branching-model)
- [Commit Convention](#commit-convention)
- [Pull Request Process](#pull-request-process)
- [CI and Releases](#ci-and-releases)
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
make fmt       # Run pre-commit hooks (ruff, mdformat, codespell, ty, ...)
make test      # Run the test suite
make gen-docs  # Generate documentation
make clean     # Remove caches and build artifacts
```

Always run `make fmt` and `make test` before opening a pull request.

Add dependencies with `uv add <pkg>`, or `uv add --dev <pkg>` for development-only ones. The optional dependency groups are declared under `[dependency-groups]` in `pyproject.toml`; install one with `uv sync --group <name>`. Shortcut tasks are defined under `[tool.poe.tasks]` and run with `uv run poe <task>`.

## Local Services

`docker-compose.yaml` defines optional local databases and an example `app` service that runs the CLI. Copy `.env.example` to `.env` to set their ports and credentials, then start only what you need:

```bash
docker compose up -d redis postgresql
docker compose up -d app
```

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
uv sync --group docs
make gen-docs
uv run zensical serve  # http://0.0.0.0:9987
```

`make gen-docs` deletes and rebuilds `docs/` from the READMEs and the docstrings under `src/` and `scripts/`, so edit those rather than the files under `docs/`. `uv run ./scripts/gen_docs.py --help` lists the generator's options.

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
| `docs`     | Documentation-only changes                              |
| `perf`     | Performance improvement                                 |
| `style`    | Formatting or stylistic changes                         |
| `test`     | Adding or correcting tests                              |
| `build`    | Build system changes                                    |
| `chore`    | Tooling or auxiliary changes                            |
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

## CI and Releases

Workflows live in `.github/workflows/`, and each file states its own triggers. Some need repository settings that no file can carry:

- A `UV_PUBLISH_TOKEN` secret, to publish to PyPI (Settings → Secrets and variables → Actions)
- GitHub Pages with "GitHub Actions" as the source, to deploy the docs site (Settings → Pages)
- Workflow permissions set to "Read and write", to push images to GHCR (Settings → Actions → General)

To release, push a `v*` tag. CI builds the executables and the Python package, uploads them to a GitHub Release, and publishes to PyPI when `UV_PUBLISH_TOKEN` is set. To build or publish by hand:

```bash
uv build                         # wheel and sdist into dist/
UV_PUBLISH_TOKEN=... uv publish
```

## Code Review

- Address all review comments or explain why a change is not needed.
- Keep discussions technical, focused, and respectful.
- Resolve conversations only after the concern has been addressed.

## Coding Standards

- **Formatting and linting**: handled by `ruff` (configured in `pyproject.toml`)
- **Typing**: `ty` with strict rules, running against the project environment so first-party imports resolve; new code should be type-annotated
- **Spelling**: enforced by `codespell` via pre-commit
- **Notebooks**: stripped of outputs by `nbstripout`

Prefer clarity over cleverness, and avoid unrelated refactors in feature or fix pull requests.

## Security Reports

Please **do not** report security vulnerabilities through public issues. Refer to the [security policy](https://github.com/Mai0313/repo_template/security/policy) for the responsible disclosure process.

## Licensing

By contributing, you agree that your contributions will be licensed under the project's license (see [`LICENSE`](../LICENSE)). Ensure that you have the right to submit any code, content, or assets you contribute.
