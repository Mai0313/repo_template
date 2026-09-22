# Initializing a Project from This Template

This repository is a starting point, not an application to extend under the `repo_template` identity. Treat the first substantial change as project initialization: establish the new project's identity, keep the pieces that serve it, and replace the demonstration code with an intentional baseline before implementing product features.

The current scaffold is a Python package template. Do not silently assume that every new project should remain a Python CLI, but do not begin a partial migration to another language or framework either. First determine whether the requested project is:

- a distributable Python library or CLI;
- a Python service, worker, or application that benefits from this package layout;
- a project that only needs selected operational conventions from this template; or
- a project for which this template is unsuitable.

If Python remains appropriate, preserve the `src/` layout and adapt the existing toolchain. If another stack is chosen, make an explicit replacement plan for packaging, tests, formatting, dependency management, containerization, documentation, and CI before removing Python-specific files. Never leave a new repository half configured for two unrelated stacks.

## Initialization order

Complete the following phases in order. Do not add product features while template names, ownership, release targets, and executable examples still describe `repo_template`.

1. Establish the project brief: intended users, delivery form, supported platforms, runtime requirements, public API or CLI surface, persistence or external services, and release destination.
2. Choose the project identity and record the values below before bulk renaming.
3. Inventory every template placeholder and rename or replace each occurrence coherently.
4. Turn the example package, command, and test into the smallest meaningful project baseline.
5. Adapt the existing checks, deployment paths, and documentation to that baseline.
6. Run the relevant local verification, then remove only scaffolding whose replacement is working and no longer needed.

Do not use a blind repository-wide replacement for display names, package identifiers, URLs, or container labels. These names have different syntax and consumers.

## Identity and placeholder inventory

Decide and keep a short mapping for these distinct values:

| Purpose           | Current template value                     | Where it matters                                             |
| ----------------- | ------------------------------------------ | ------------------------------------------------------------ |
| GitHub repository | `Mai0313/repo_template`                    | README badge links, GitHub Pages, Actions, release links     |
| Distribution name | `repo_template`                            | `[project].name`, build and publish artifacts                |
| Import package    | `repo_template`                            | `src/repo_template/`, imports, Hatch package settings, tests |
| Display name      | `RepoTemplate` / `Python Project Template` | README titles and `mkdocs.yml`                               |
| Console commands  | `repo_template` and `cli`                  | `[project.scripts]`, examples, Docker and release artifacts  |
| Owner and author  | `Mai0313`, `Wei`, `mai@mai0313.com`        | `CODEOWNERS`, package metadata, docs, image labels           |
| Hosting URLs      | `mai0313.github.io/repo_template`          | package URLs, MkDocs, README links                           |

Search the tracked repository, including hidden configuration, for `repo_template`, `RepoTemplate`, `Mai0313`, `mai0313.github.io`, `Wei`, and `mai@mai0313.com`. Inspect each match before editing it. Also search for the old repository URL after the first pass, because badges, release configuration, and documentation commonly use the full value rather than a short placeholder.

For a Python project, choose a valid distribution name and a valid import name separately when needed. Hyphens may be suitable for a distribution but cannot be used in an import package. Rename `src/repo_template/`, update all first-party imports and tests, and then update all related fields in `pyproject.toml` together:

- `[project]` metadata, `requires-python`, dependencies, and URLs;
- `[project.scripts]` only if the project actually has a CLI;
- Hatch build include and wheel package paths;
- Poe tasks that point at `src/repo_template/cli.py`.

The release workflow currently derives its executable path and artifact name from the GitHub repository name. Either deliberately keep the repository name, import package, and executable aligned, or modify that workflow so it uses the chosen command explicitly. Do not assume those identities will remain interchangeable.

## Preserve documentation and repository signals

`README.md`, `README.zh-TW.md`, and `README.zh-CN.md` are part of the initial product surface. Keep every existing badge in every README permanently. Existing badges may only be modified to update URLs, repository identities, supported versions, package links, workflow names, or display data, and new badges may be added only when there is a real target for them. There is no later-project exception that permits deleting an existing badge. Keep the three language versions consistent in meaning.

Replace template-only prose such as the instruction to use this repository as a template. Retain and adapt useful sections for installation, local development, configuration, examples, support boundaries, security, and release use. Do not claim a package registry release, GitHub Pages site, Docker image, supported platform, or service integration until it is actually configured.

`mkdocs.yml` and `scripts/gen_docs.py` form a documentation pipeline. Update site and repository metadata before enabling publication. The generated `docs/` directory is ignored and rebuilt by `make gen-docs`; edit source READMEs and code docstrings rather than treating generated output as the source of truth.

## Treat existing automation as a starting asset

Keep the existing GitHub Actions during initialization and modify them to the new project. Do not delete a workflow merely because its initial configuration is template-specific. After the project has reached a stable stage, remove a workflow only when evidence shows that its capability is no longer needed and the user explicitly confirms the reduction. Update affected documentation, badges, required checks, and related configuration in the same change, without deleting any existing README badge.

Review each existing workflow against the project brief:

| Workflow                                                            | Initial review question                                                                                                        |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| `test.yml`                                                          | Do the Python versions, coverage threshold, test paths, and Markdown-only trigger exclusion match supported runtimes and risk? |
| `code-quality-check.yml`                                            | Does the selected formatter, linter, type checker, and pre-commit suite fit the codebase?                                      |
| `code_scan.yml`                                                     | Which security scanners and CodeQL language configuration apply to the actual code?                                            |
| `deploy.yml`                                                        | Is GitHub Pages the chosen documentation host, and are its permissions and site settings enabled?                              |
| `build_image.yml`                                                   | Is there a production image, a valid Docker target, and an intended GHCR publishing policy?                                    |
| `build_release.yml`                                                 | Is a PyInstaller binary required on all six target platforms, alongside a Python package release?                              |
| `release_drafter.yml`                                               | Does tag and draft-release behavior match the release policy?                                                                  |
| `auto_labeler.yml`, `semantic-pull-request.yml`                     | Do labels, branches, and Conventional Commit rules match the collaboration model?                                              |
| `auto_review_merge.yml`, `pre-commit-updater.yml`, `dependabot.yml` | Is unattended dependency approval, merge, or update acceptable for the new repository?                                         |

Adapt dependent configuration together: `.github/labeler.yml`, `.github/cliff.toml`, issue templates, `CODEOWNERS`, Dependabot ecosystems, and the README's CI descriptions. The current labeler includes Python, TypeScript, and JavaScript globs; refine it only after the selected stack is known. The current workflows use broad `write-all` permissions. Replace these with the minimum permissions required by each retained workflow when the required publishing and automation behavior is clear.

Never put credentials in `.env.example`, source control, workflow files, or image labels. Define non-secret variable names and document where real secrets belong. Before enabling package publication, GHCR pushes, Pages deployment, release creation, or auto-merge, verify repository settings, token scopes, protected branches, and the required secrets outside the codebase.

## Python baseline, when retained

This template uses `uv`, Hatchling, Ruff, ty, pytest, pre-commit, Zensical, and optional Poe tasks. Keep that integrated path intact until a deliberate alternative has been selected and tested. Use `uv sync` and `uv run`; update `pyproject.toml` and regenerate `uv.lock` through `uv` when dependencies change.

The example `src/repo_template/cli.py` and `tests/test_hello.py` prove packaging and test discovery only. Replace them with behavior that represents the new project. If the project has no CLI, remove the example console scripts only after removing or replacing every command, Docker, documentation, and release reference that invokes them. If it is a library, create a small import-level test and a representative public API instead of preserving a greeting command as dead scaffolding.

Keep tests under `tests/` and prefer a structure that mirrors the source package. Preserve the coverage gate only when it reflects a meaningful test suite; adjust it intentionally rather than gaming it with exclusions or empty tests. Align `requires-python`, `.python-version`, the test matrix, Docker base image, and devcontainer image before declaring a supported Python version.

`Makefile` targets, pre-commit hooks, and docs commands are conveniences with cross-file dependencies. In particular, `make gen-docs` deletes and rebuilds `docs/`, and `make clean` deletes generated reports, caches, artifacts, and documentation before running Git maintenance. Inspect these commands before using them on local work that has not been committed.

## Containers and local services

`docker/Dockerfile`, `.devcontainer/`, `docker-compose.yaml`, and `.env.example` are optional capabilities, not evidence that every new project needs Redis, PostgreSQL, MongoDB, MySQL, an application image, or the listed editor extensions.

Decide which runtime services the project needs, then revise the Compose services, health checks, ports, volumes, environment variables, image labels, and application command as one change. Keep loopback-only ports and non-root container execution unless the requirements justify a different exposure model. Update the Docker base runtime and devcontainer extensions to match the selected stack. Do not publish an image until its entrypoint, build target, registry policy, and runtime configuration have been verified.

## Verification and staged cleanup

After the identity and minimal baseline are in place, verify the paths that the new project keeps:

```bash
uv sync
uv run pre-commit run -a
uv run pytest
uv build
```

Run `make gen-docs` and `uv run zensical build` when retaining documentation, and build or exercise containers when retaining Docker support. Verify workflow YAML and inspect Actions configuration before relying on deployment or publication. Run the new command with `uv run <chosen-command>` only if the project intentionally exposes a CLI.

Before considering initialization complete, inspect `git diff` and search again for template identifiers. Ensure that references left behind are either intentional provenance or have been renamed. Confirm that the README badges still exist and point to the new project where applicable.

Only after the new baseline works should you remove unused example code, unsupported service definitions, package scripts, devcontainer extensions, dependency groups, or documentation sections. Each deletion must have a reason, a replacement or explicit decision, and verification that no remaining configuration calls it. Workflow reductions follow the stricter confirmation rule above, and existing README badges remain permanent. Prefer a small, working initial surface over preserving a broad but misleading template feature set.

## Ongoing work after initialization

For feature work, keep changes scoped, add tests for behavior changes and regressions, update public documentation with the implementation, and run the applicable formatter, linter, type checks, and tests before proposing a change. Use short English Conventional Commit messages when commits are requested. Keep pull requests as drafts until the chosen checks pass, then ask before marking them ready for review.
