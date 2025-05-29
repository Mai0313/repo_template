<center>

# Python Project Template

[![python](https://img.shields.io/badge/-Python_3.10_%7C_3.11_%7C_3.12-blue?logo=python&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![tests](https://github.com/Mai0313/repo_template/actions/workflows/test.yml/badge.svg)](https://github.com/Mai0313/repo_template/actions/workflows/test.yml)
[![code-quality](https://github.com/Mai0313/repo_template/actions/workflows/code-quality-check.yml/badge.svg)](https://github.com/Mai0313/repo_template/actions/workflows/code-quality-check.yml)
[![codecov](https://codecov.io/gh/Mai0313/repo_template/branch/master/graph/badge.svg)](https://codecov.io/gh/Mai0313/repo_template)
[![license](https://img.shields.io/badge/License-MIT-green.svg?labelColor=gray)](https://github.com/Mai0313/repo_template/tree/master?tab=License-1-ov-file)
[![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/Mai0313/repo_template/pulls)
[![contributors](https://img.shields.io/github/contributors/Mai0313/repo_template.svg)](https://github.com/Mai0313/repo_template/graphs/contributors)

</center>

🚀 **A comprehensive Python project template to kickstart your development with complete CI/CD pipelines and modern tooling**

Click on [<kbd>Use this template</kbd>](https://github.com/Mai0313/repo_template/generate) to initialize a new repository, or use our initialization script for a personalized setup.

**Other Languages**: [English](README.md) | [中文](README_cn.md)

## ✨ Features

### 🏗️ **Modern Project Structure**

- **src/ layout**: Following Python packaging best practices
- **uv dependency management**: Fast, reliable, and modern dependency resolution
- **Multi-version support**: Python 3.10, 3.11, and 3.12
- **Type hints**: Full type annotation support with validation

### 🔧 **Development Environment**

- **VS Code Dev Container**: Fully configured with zsh, oh-my-zsh, and powerlevel10k theme
- **Docker support**: Multi-stage Dockerfile for development and production
- **Pre-commit hooks**: Automated code formatting and linting with ruff
- **Local development**: Easy setup with Make commands

### 🧪 **Testing & Quality Assurance**

- **pytest framework**: Comprehensive testing with coverage reporting
- **Parallel execution**: Faster test runs with pytest-xdist
- **Code coverage**: HTML and XML reports with configurable thresholds
- **Quality gates**: Automated code quality checks on every commit

### 🚀 **Complete CI/CD Pipeline**

- **Multi-version testing**: Automated testing across Python versions
- **Code quality checks**: ruff linting and formatting validation
- **Documentation deployment**: Automatic GitHub Pages deployment
- **Release automation**: Semantic versioning and release drafting
- **Auto-labeling**: Intelligent PR categorization

### 📚 **Documentation**

- **MkDocs Material**: Beautiful, responsive documentation
- **Auto-generation**: Scripts to generate docs from code and notebooks
- **API documentation**: Automatic API reference generation
- **Blog support**: Built-in blog functionality for project updates

### 🤖 **Automation Scripts**

- **Project initialization**: `scripts/initpyrepo.go` for creating personalized projects
- **Documentation generation**: `scripts/gen_docs.py` for auto-generating documentation
- **Makefile commands**: Common development tasks automated

## 🚀 Quick Start

### Option 1: Use GitHub Template

1. Click [<kbd>Use this template</kbd>](https://github.com/Mai0313/repo_template/generate)
2. Configure your new repository
3. Clone and start developing

### Option 2: Use Initialization Script

1. Clone this repository
2. Run the initialization script:
    ```bash
    go run scripts/initpyrepo.go
    ```
3. Follow the prompts to customize your project

### Option 3: Manual Setup

1. Clone the repository
2. Install dependencies:
    ```bash
    make uv-install  # Install uv if not already installed
    uv sync          # Install project dependencies
    ```
3. Set up pre-commit hooks:
    ```bash
    make format      # Run pre-commit hooks
    ```

### Option 4: Quick Customization (Recommended)

1. Clone this repository
2. Globally replace `repo_template` with your project name (snake_case format)
3. Globally replace `RepoTemplate` with your project title (PascalCase format)
4. Run initial setup:
    ```bash
    make uv-install && uv sync && make format
    ```

## 📁 Project Structure

```
├── .devcontainer/          # VS Code Dev Container configuration
├── .github/
│   ├── workflows/          # CI/CD workflows
│   └── copilot-instructions.md
├── docker/                 # Docker configurations
├── docs/                   # MkDocs documentation
├── scripts/                # Automation scripts
├── src/
│   └── repo_template/      # Main package
├── tests/                  # Test suite
├── pyproject.toml          # Project configuration
├── Makefile               # Development commands
└── README.md
```

## 🛠️ Available Commands

```bash
# Development
make clean          # Clean autogenerated files
make format         # Run pre-commit hooks
make test           # Run all tests
make gen-docs       # Generate documentation

# Dependencies
make uv-install     # Install uv dependency manager
uv add <package>    # Add production dependency
uv add <package> --dev  # Add development dependency
```

## 🎯 What's Included

### CI/CD Workflows

- **Testing**: Multi-version Python testing on PRs
- **Code Quality**: Automated ruff checks and pre-commit validation
- **Documentation**: Automatic GitHub Pages deployment
- **Release**: Automated release drafting and changelog generation
- **Labeling**: Auto-labeling based on PR content

### Development Tools

- **ruff**: Fast Python linter and formatter
- **pytest**: Testing framework with coverage
- **pre-commit**: Git hooks for code quality
- **MkDocs**: Documentation generation
- **Docker**: Containerized development and deployment

### Project Templates

- **Python package**: Ready-to-use package structure
- **Configuration files**: All necessary config files included
- **Documentation**: Complete documentation setup
- **Testing**: Comprehensive test configuration

## 🎨 Customization Guide

### Project Name Customization

This template is designed for quick customization through simple global replacements:

1. **Replace package name**: Change all instances of `repo_template` to your project name (recommended: snake_case)
2. **Replace project title**: Change all instances of `RepoTemplate` to your project title (recommended: PascalCase)
3. **Update metadata**: Modify author, description, and other details in `pyproject.toml`

Example:

```bash
# If your project is called "awesome_project"
find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/repo_template/awesome_project/g'
find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/RepoTemplate/AwesomeProject/g'
```

## 🤝 Contributing

We welcome contributions! Please feel free to:

- Open issues for bugs or feature requests
- Submit pull requests for improvements
- Share your experience using this template

## 📖 Documentation

For detailed documentation, visit: [https://mai0313.github.io/repo_template/](https://mai0313.github.io/repo_template/)

## 👥 Contributors

[![Contributors](https://contrib.rocks/image?repo=Mai0313/repo_template)](https://github.com/Mai0313/repo_template/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
