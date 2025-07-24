<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

⚠️ **IMPORTANT**: You MUST modify `.github/copilot-instructions.md` every time you make changes to the project.

# Project Background

This is a pre-configured Python project template designed to streamline the development process. It includes essential tools and configurations for modern Python development, such as dependency management, code formatting, linting, testing, and documentation.
Everything in this file SHOULD BE MODIFIED to reflect the current state of the project.

# Core Infrastructure

- **Modern Python**: Supports Python 3.10, 3.11, and 3.12
- **Dependency Management**: Uses `uv` for fast and reliable dependency management
- **Project Structure**: src/ layout following Python packaging best practices
- **Docker Support**: Multi-stage Dockerfile for development and production
- **VS Code Dev Container**: Fully configured development environment with zsh, oh-my-zsh, and powerlevel10k

# CI/CD Pipeline

- **Pre-commit Hooks**: You can run `pre-commit run -a` to apply all hooks.
- **Github Action**: All actions you may need are defined in `.github/workflows/` directory.

# Coding Style

- All rules are pre-defined by using `pre-commit run -a` command.
- Follow PEP 8 naming conventions:
    - snake_case for functions and variables
    - PascalCase for classes
    - UPPER_CASE for constants
- Use pydantic model, and all pydantic models should include `Field`, and `description` should be included.
- Use `pytest` for testing, and all tests should be placed in the `tests/` directory

# Type Hints / Documentation

- Use type hints for all function parameters and returns
- Use `TypeVar` for generic types
- Use `Protocol` for duck typing
- Use Google-style docstrings
- All documentation should be in English
- Use proper inline comments for better mkdocs support

# Dependencies

- Use `uv` for dependency management
- Separate dev dependencies by adding `--dev` flag when adding dependencies
    - Production:
        - Add Dependencies: `uv add <package>`
        - Remove Dependencies: `uv remove <package>`
    - Development:
        - Add Dependencies: `uv add <package> --dev`
        - Remove Dependencies: `uv remove <package> --dev`
