<div align="center" markdown="1">

# Python Project Template

[![PyPI version](https://img.shields.io/pypi/v/swebenchv2.svg)](https://pypi.org/project/swebenchv2/)
[![python](https://img.shields.io/badge/-Python_%7C_3.12%7C_3.13%7C_3.14-blue?logo=python&logoColor=white)](https://www.python.org/downloads/source/)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![ty](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ty/main/assets/badge/v0.json)](https://github.com/astral-sh/ty)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://docs.pydantic.dev/latest/contributing/#badges)
[![tests](https://github.com/Mai0313/repo_template/actions/workflows/test.yml/badge.svg)](https://github.com/Mai0313/repo_template/actions/workflows/test.yml)
[![code-quality](https://github.com/Mai0313/repo_template/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/Mai0313/repo_template/actions/workflows/code-quality-check.yml)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/Mai0313/repo_template)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/Mai0313/repo_template/tree/main?tab=License-1-ov-file)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mai0313/repo_template/pulls)
[![contributors](https://img.shields.io/github/contributors/Mai0313/repo_template.svg)](https://github.com/Mai0313/repo_template/graphs/contributors)

</div>

🚀 A production‑ready Python project template to help developers bootstrap new Python projects fast. It includes modern packaging, local tooling, Docker, and a complete CI/CD suite.

> **Important**: This is a template repository. Do not develop directly on this repository. Instead, use it to create your own project by clicking the button below and following the setup instructions.

Click [Use this template](https://github.com/Mai0313/repo_template/generate) to start a new repository from this scaffold.

Other Languages: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## ✨ Highlights

- Modern `src/` layout and type‑hinted code
- Fast dependency management via `uv`
- Pre‑commit suite: ruff, mdformat(+plugins), codespell, nbstripout, ty, uv hooks
- Strong typing: ty with strict rules, checked against the real project environment
- Pytest with coverage and xdist; PR coverage summary comment
- Coverage gate at 80% with HTML/XML reports committed under `.github/`
- Zensical with mkdocstrings (inheritance diagrams), markdown‑exec, MathJax
- Dev server at `0.0.0.0:9987`; bilingual docs scaffolded
- Docs generator script: by class/file, optional notebook execution, concurrency, preserves folder structure
- Async file processing via anyio and rich progress bars
- Packaging with `uv build` and changelog via `git-cliff`
- Automatic PEP 440 versioning from git via `dunamai` in CI
- Dockerfile multi‑stage with uv/uvx and Node.js; Compose services (Redis/Postgres/Mongo/MySQL) with healthchecks and volumes
- GitHub Actions: tests, quality, docs deploy, package build, docker image publish (GHCR with buildx cache), release drafter, auto labeler, secret scan, semantic PR, pre‑commit auto‑update
- Pre‑commit runs on multiple git stages (pre‑commit, post‑checkout, post‑merge, post‑rewrite)
- i18n‑friendly linting (Chinese punctuation allowed confusables)
- Alternative env managers documented (Rye, Conda)
- Legacy compatibility: export `requirements.txt` via `uv pip` if needed

## 🚀 Quick Start

### For Template Users (Creating a New Project)

This is the recommended workflow for starting a new project:

1. **Create Your Repository**: Click [Use this template](https://github.com/Mai0313/repo_template/generate) to create a new repository

2. **Clone and Setup**:

    ```bash
    git clone https://github.com/YOUR_USERNAME/your_new_project.git
    cd your_new_project
    make uv-install               # Install uv (only needed once)
    uv sync                       # Install dependencies
    uvx pre-commit install        # Install pre-commit git hooks
    ```

3. **Rename the Project**:

    - Rename `src/repo_template/` directory to `src/your_project_name/`
    - Update all imports from `repo_template` to `your_project_name`
    - Update `pyproject.toml` with your project details:
        - Project name, version, description, authors
        - Homepage and Repository URLs
        - CLI script names if needed
    - Update `mkdocs.yml`: site_name, site_url, repo_name, repo_url, site_author
    - Update all three README files (preserve badges, only update URLs)
    - Update `.github/CODEOWNERS` with your GitHub username
    - Update Docker labels in `docker/Dockerfile`

4. **Verify Setup**:

    ```bash
    make fmt                      # Run pre-commit hooks
    make test                     # Run tests
    uv run your_project_name      # Test your CLI
    ```

## 🧩 Example CLI

Console entry points are defined in `pyproject.toml` as `repo_template` and `cli`. The example returns a simple `Response` model; replace with your own CLI logic.

```bash
uv run repo_template
```

## 🤝 Contributing

Development setup, commands, local services, docs, CI and releases are in [CONTRIBUTING.md](https://github.com/Mai0313/repo_template/blob/main/.github/CONTRIBUTING.md).

## 📄 License

MIT — see `LICENSE`.
