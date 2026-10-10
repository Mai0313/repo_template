<div align="center" markdown="1">

# Python 專案模板

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

🚀 幫助 Python 開發者「快速建立新專案」的模板。內建現代化套件管理、工具鏈、Docker 與完整 CI/CD 工作流程。

> **重要提示**：這是一個模板倉庫。請勿直接在此倉庫上開發。應點擊下方按鈕建立您自己的專案，並依照設定說明操作。

點擊 [使用此模板](https://github.com/Mai0313/repo_template/generate) 後即可開始。

其他語言: [English](README.md) | [繁體中文](README.zh-TW.md) | [简体中文](README.zh-CN.md)

## ✨ 重點特色

- 現代 `src/` 佈局 + 全面型別註解
- `uv` 超快依賴管理
- pre-commit 套件鏈：ruff、mdformat（含多插件）、codespell、nbstripout、ty、uv hooks
- 型別嚴謹：ty 嚴格規則，直接針對專案實際環境檢查
- pytest + coverage + xdist；PR 覆蓋率摘要留言
    - 覆蓋率門檻 80%，HTML/XML 報告輸出至 `.github/`
- Zensical + mkdocstrings（繼承圖）、markdown-exec、MathJax
    - 開發伺服器 `0.0.0.0:9987`；雙語文件腳手架
- 文件生成腳本：支援 class/檔案兩種模式、可選執行 notebook、可併發、保留目錄結構
    - 使用 anyio 非同步處理與 rich 進度條
- 打包：`uv build`、git-cliff 產 changelog
- CI 自動版本：以 `dunamai` 從 git 產 PEP 440 版本
- Dockerfile 多階段（內含 uv/uvx 與 Node.js）；Compose 服務（Redis/Postgres/Mongo/MySQL）含 healthcheck 與 volume
- GitHub Actions：測試、品質、文件部署、套件打包、Docker 推送（GHCR + buildx cache）、Release Drafter、自動標籤、祕密掃描、語義化 PR、pre-commit 自動更新
    - pre-commit 同時掛載多個 git 階段（pre-commit、post-checkout、post-merge、post-rewrite）
    - i18n 友善檢查（允許中文標點等 confusables）
    - 文件列出可替代的環境管理（Rye、Conda）
    - 相容舊式流程：可用 `uv pip` 匯出 `requirements.txt`

## 🚀 快速開始

### 模板使用者（建立新專案）

這是啟動新專案的推薦工作流程：

1. **建立您的倉庫**：點擊 [使用此模板](https://github.com/Mai0313/repo_template/generate) 建立新倉庫

2. **複製並設定**：

    ```bash
    git clone https://github.com/YOUR_USERNAME/your_new_project.git
    cd your_new_project
    make uv-install               # 安裝 uv（僅需一次）
    uv sync                       # 安裝依賴
    uvx pre-commit install        # 安裝 pre-commit git hooks
    ```

3. **重新命名專案**：

    - 將 `src/repo_template/` 目錄重新命名為 `src/your_project_name/`
    - 更新所有從 `repo_template` 到 `your_project_name` 的匯入
    - 更新 `pyproject.toml` 中的專案詳情：
        - 專案名稱、版本、描述、作者
        - 首頁和倉庫 URL
        - CLI 腳本名稱（如需要）
    - 更新 `mkdocs.yml`：site_name、site_url、repo_name、repo_url、site_author
    - 更新所有三個 README 檔案（保留徽章，僅更新 URL）
    - 更新 `.github/CODEOWNERS` 為您的 GitHub 使用者名稱
    - 更新 `docker/Dockerfile` 中的 Docker 標籤

4. **驗證設定**：

    ```bash
    make fmt                      # 執行 pre-commit hooks
    make test                     # 執行測試
    uv run your_project_name      # 測試您的 CLI
    ```

## 🧩 範例 CLI

`pyproject.toml` 內提供 `repo_template` 與 `cli` 兩個入口點。目前示範回傳簡單 `Response` 模型，可依需求替換。

```bash
uv run repo_template
```

## 🤝 貢獻

開發環境、常用指令、本機服務、文件、CI 與發佈流程請見 [CONTRIBUTING.md](https://github.com/Mai0313/repo_template/blob/main/.github/CONTRIBUTING.md)。

## 📄 授權

MIT — 詳見 `LICENSE`。
