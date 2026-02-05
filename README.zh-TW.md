<div align="center" markdown="1">

# Python 專案模板

[![PyPI version](https://img.shields.io/pypi/v/swebenchv2.svg)](https://pypi.org/project/swebenchv2/)
[![python](https://img.shields.io/badge/-Python_%7C_3.11%7C_3.12%7C_3.13%7C_3.14-blue?logo=python&logoColor=white)](https://www.python.org/downloads/source/)
[![uv](https://img.shields.io/badge/-uv_dependency_management-2C5F2D?logo=python&logoColor=white)](https://docs.astral.sh/uv/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
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
- pre-commit 套件鏈：ruff、mdformat（含多插件）、codespell、nbstripout、mypy、uv hooks
- 型別嚴謹：mypy + Pydantic 外掛設定
- pytest + coverage + xdist；PR 覆蓋率摘要留言
    - 覆蓋率門檻 80%，HTML/XML 報告輸出至 `.github/`
- MkDocs Material + mkdocstrings（繼承圖）、markdown-exec、MathJax
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
   uv tool install pre-commit    # 安裝 pre-commit
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
   - 更新 `docker/Dockerfile` 和 `.devcontainer/Dockerfile` 中的 Docker 標籤

4. **驗證設定**：
   ```bash
   make format                   # 執行 pre-commit hooks
   make test                     # 執行測試
   uv run your_project_name      # 測試您的 CLI
   ```

### 模板開發者（測試此模板）

如果您正在為此模板做貢獻：

```bash
make uv-install               # 安裝 uv
uv sync                       # 安裝依賴
uv tool install pre-commit    # 安裝 pre-commit
make format                   # 執行 pre-commit hooks
make test                     # 執行測試
uv run repo_template          # 測試範例 CLI
```

## 🧰 指令一覽

```bash
# 開發
make help               # 顯示 Makefile 指令列表
make clean              # 清理快取、產物與產生的文件
make format             # 執行所有 pre-commit hooks
make test               # 執行 pytest
make gen-docs           # 從 src/ 與 scripts/ 生成文件

# Git 子模組（如有使用）
make submodule-init     # 初始化與更新所有子模組
make submodule-update   # 更新所有子模組至遠端

# 依賴管理（uv）
make uv-install         # 安裝 uv
uv add <pkg>            # 加入正式依賴
uv add <pkg> --dev      # 加入開發依賴
# 同步選用依賴群組
uv sync --group dev     # 安裝開發用依賴（pre-commit、poe、notebook）
uv sync --group test    # 安裝測試用依賴
uv sync --group docs    # 安裝文件用依賴
```

## 📚 文件系統

- 使用 MkDocs Material
- 生成與預覽：

```bash
uv sync --group docs
make gen-docs
uv run mkdocs serve    # http://localhost:9987
```

- 自動生成腳本：`scripts/gen_docs.py`（支援 .py 與 .ipynb）

```bash
# 以 class 為單位（預設）
uv run python ./scripts/gen_docs.py --source ./src --output ./docs/Reference gen_docs

# 以檔案為單位
uv run python ./scripts/gen_docs.py --source ./src --output ./docs/Reference --mode file gen_docs
```

## 🐳 Docker 與本機服務

`docker-compose.yaml` 內提供本機開發常見服務：`redis`、`postgresql`、`mongodb`、`mysql`，以及示範 `app` 服務（執行 CLI）。

建立 `.env` 設定連線參數（預設如下）：

```bash
REDIS_PORT=6379
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_PORT=5432
MONGO_PORT=27017
MYSQL_ROOT_PASSWORD=root
MYSQL_DATABASE=mysql
MYSQL_USER=mysql
MYSQL_PASSWORD=mysql
MYSQL_PORT=3306
```

啟動服務：

```bash
docker compose up -d redis postgresql mongodb mysql

# 或啟動示範 app
docker compose up -d app
```

## 📦 打包與發佈

以 uv 產出套件（wheel/sdist 會放在 `dist/`）：

```bash
uv build
```

發佈到 PyPI（需設定 `UV_PUBLISH_TOKEN`）：

```bash
UV_PUBLISH_TOKEN=... uv publish
```

CI 亦會在建立 `v*` 標籤時自動打包多平台可執行檔與 Python 套件，並上傳到 GitHub Release。若要自動發布到 PyPI，請在 repository 設定中新增 `UV_PUBLISH_TOKEN` secret（`build_release.yml` 已設定自動發布）。

### 在本機與 PyPI 執行你的 CLI

- 本機（來源碼倉）：

```bash
uv run repo_template
uv run cli
```

- 發佈到 PyPI 後，透過 `uvx`（臨時安裝後執行）：

```bash
# 若 console script 名稱為 "repo_template"
uvx repo_template

# 或指定套件/版本與入口名稱
uvx --from your-package-name==0.1.0 your-entrypoint
```

## 🧭 選用任務管理（Poe the Poet）

`pyproject.toml` 中的 `[tool.poe.tasks]` 定義了便捷任務，安裝 dev 群組（`uv sync --group dev`）或使用 `uvx` 後可用：

```bash
uv run poe docs        # 生成 + 啟動文件預覽（需 dev 群組）
uv run poe gen         # 生成 + 發佈文件（gh-deploy）（需 dev 群組）
uv run poe main        # 執行 CLI（等同 uv run repo_template）

# 或使用 uvx（臨時環境，無需本地安裝）
uvx poe docs
```

## 🔁 CI/CD 工作流程總覽

所有流程位於 `.github/workflows/`，以下為觸發時機與用途：

- Tests（`test.yml`）

    - 觸發：對 `main`、`release/*` 的 PR
    - 執行 pytest（3.11/3.12/3.13/3.14）並留下覆蓋率摘要

- Code Quality（`code-quality-check.yml`）

    - 觸發：PR
    - 執行 ruff 與其它 pre-commit hooks

- Docs Deploy（`deploy.yml`）

    - 觸發：推送到 `main` 與 `v*` 標籤
    - 建置並發布 MkDocs 網站到 GitHub Pages
    - 需在 GitHub 啟用 Pages（Actions → Pages）

- Build and Release（`build_release.yml`）

    - 觸發：`v*` 標籤推送或手動觸發
    - 建置多平台可執行檔（透過 PyInstaller）：
        - macOS（ARM64、x64）
        - Linux（x64 GNU、ARM64 GNU）
        - Windows（x64、ARM64）
    - 建置 Python 套件（wheel & sdist）
    - 自動發布到 PyPI（需設定 `UV_PUBLISH_TOKEN` secret）
    - 上傳所有產物至 GitHub Release
    - 注意：此為 template 示範流程，請依實際專案需求調整

- Publish Docker Image（`build_image.yml`）

    - 觸發：推送到 `main` 與 `v*` 標籤
    - 發佈至 GHCR：`ghcr.io/<owner>/<repo>`（需 `docker/Dockerfile` 內有 `prod` target）

- Release Drafter（`release_drafter.yml`）

    - 觸發：推送到 `main` 與 PR 事件
    - 基於 Conventional Commits 維護草稿發佈

- PR Labeler（`auto_labeler.yml`）

    - 觸發：PR 與 Push
    - 依 `.github/labeler.yml` 自動加標籤

- Secret Scanning（`secret_scan.yml`）

    - 觸發：Push 與 PR
    - 使用 gitleaks 掃描機密

- Semantic Pull Request（`semantic-pull-request.yml`）

    - 觸發：PR 開啟/更新
    - 強制 PR 標題符合 Conventional Commits

### CI/CD 設定清單

- PR 標題遵循 Conventional Commits
- （選用）發佈到 PyPI：在 repository 設定中新增 `UV_PUBLISH_TOKEN` secret（Settings → Secrets and variables → Actions）
- （選用）啟用 GitHub Pages 以發布文件（Settings → Pages → Source: GitHub Actions）
- （選用）發佈 Docker 映像檔：確認 GHCR 權限已啟用（Settings → Actions → General → Workflow permissions: Read and write）

## 🧩 範例 CLI

`pyproject.toml` 內提供 `repo_template` 與 `cli` 兩個入口點。目前示範回傳簡單 `Response` 模型，可依需求替換。

```bash
uv run repo_template
```

## 🤝 貢獻

- 歡迎 Issue/PR
- 請遵循程式風格（ruff、型別）
- PR 標題遵循 Conventional Commits

## 📄 授權

MIT — 詳見 `LICENSE`。
