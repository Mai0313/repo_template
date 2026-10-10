<div align="center" markdown="1">

# Python 项目模板

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

🚀 帮助 Python 开发者「快速建立新项目」的模板。内置现代化包管理、工具链、Docker 与完整 CI/CD 工作流程。

> **重要提示**：这是一个模板仓库。请勿直接在此仓库上开发。应点击下方按钮创建您自己的项目，并按照设置说明操作。

点击 [使用此模板](https://github.com/Mai0313/repo_template/generate) 后即可开始。

其他语言: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## ✨ 重点特色

- 现代 `src/` 布局 + 全面类型注解
- `uv` 超快依赖管理
- pre-commit 包链：ruff、mdformat（含多插件）、codespell、nbstripout、ty、uv hooks
- 类型严谨：ty 严格规则，直接针对项目实际环境检查
- pytest + coverage + xdist；PR 覆盖率摘要留言
    - 覆盖率门槛 80%，HTML/XML 报告输出至 `.github/`
- Zensical + mkdocstrings（继承图）、markdown-exec、MathJax
    - 开发服务器 `0.0.0.0:9987`；双语文档脚手架
- 文档生成脚本：支持 class/文件两种模式、可选执行 notebook、可并发、保留目录结构
    - 使用 anyio 异步处理与 rich 进度条
- 打包：`uv build`、git-cliff 产 changelog
- CI 自动版本：以 `dunamai` 从 git 产 PEP 440 版本
- Dockerfile 多阶段（内含 uv/uvx 与 Node.js）；Compose 服务（Redis/Postgres/Mongo/MySQL）含 healthcheck 与 volume
- GitHub Actions：测试、质量、文档部署、包打包、Docker 推送（GHCR + buildx cache）、Release Drafter、自动标签、秘密扫描、语义化 PR、pre-commit 自动更新
    - pre-commit 同时挂载多个 git 阶段（pre-commit、post-checkout、post-merge、post-rewrite）
    - i18n 友善检查（允许中文标点等 confusables）
    - 文档列出可替代的环境管理（Rye、Conda）
    - 兼容旧式流程：可用 `uv pip` 导出 `requirements.txt`

## 🚀 快速开始

### 模板用户（创建新项目）

这是启动新项目的推荐工作流程：

1. **创建您的仓库**：点击 [使用此模板](https://github.com/Mai0313/repo_template/generate) 创建新仓库

2. **克隆并设置**：

    ```bash
    git clone https://github.com/YOUR_USERNAME/your_new_project.git
    cd your_new_project
    make uv-install               # 安装 uv（仅需一次）
    uv sync                       # 安装依赖
    uvx pre-commit install        # 安装 pre-commit git hooks
    ```

3. **重命名项目**：

    - 将 `src/repo_template/` 目录重命名为 `src/your_project_name/`
    - 更新所有从 `repo_template` 到 `your_project_name` 的导入
    - 更新 `pyproject.toml` 中的项目详情：
        - 项目名称、版本、描述、作者
        - 主页和仓库 URL
        - CLI 脚本名称（如需要）
    - 更新 `mkdocs.yml`：site_name、site_url、repo_name、repo_url、site_author
    - 更新所有三个 README 文件（保留徽章，仅更新 URL）
    - 更新 `.github/CODEOWNERS` 为您的 GitHub 用户名
    - 更新 `docker/Dockerfile` 中的 Docker 标签

4. **验证设置**：

    ```bash
    make fmt                      # 运行 pre-commit hooks
    make test                     # 运行测试
    uv run your_project_name      # 测试您的 CLI
    ```

## 🧩 示例 CLI

`pyproject.toml` 内提供 `repo_template` 与 `cli` 两个入口点。目前演示返回简单 `Response` 模型，可依需求替换。

```bash
uv run repo_template
```

## 🤝 贡献

开发环境、常用命令、本机服务、文档、CI 与发布流程请参阅 [CONTRIBUTING.md](https://github.com/Mai0313/repo_template/blob/main/.github/CONTRIBUTING.md)。

## 📄 授权

MIT — 详见 `LICENSE`。
