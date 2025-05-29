<center>

# Python 專案模板

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

🚀 **一個完整的 Python 專案模板，幫助開發者快速啟動專案，內含完整的 CI/CD 流水線和現代化工具**

點擊 [<kbd>使用此模板</kbd>](https://github.com/Mai0313/repo_template/generate) 來建立新的儲存庫，或使用我們的初始化腳本進行個人化設定。

**其他語言版本**: [English](README.md) | [中文](README_cn.md)

## ✨ 功能特色

### 🏗️ **現代化專案結構**

- **src/ 佈局**: 遵循 Python 封裝最佳實踐
- **uv 依賴管理**: 快速、可靠的現代化依賴解析
- **多版本支援**: Python 3.10、3.11 和 3.12
- **型別提示**: 完整的型別註解支援與驗證

### 🔧 **開發環境**

- **VS Code Dev Container**: 完整配置，包含 zsh、oh-my-zsh 和 powerlevel10k 主題
- **Docker 支援**: 開發和生產環境的多階段 Dockerfile
- **Pre-commit hooks**: 使用 ruff 自動化程式碼格式化和檢查
- **本地開發**: 使用 Make 命令輕鬆設定

### 🧪 **測試與品質保證**

- **pytest 框架**: 全面的測試與覆蓋率報告
- **平行執行**: 使用 pytest-xdist 加速測試執行
- **程式碼覆蓋率**: HTML 和 XML 報告，可配置閾值
- **品質門檻**: 每次提交都自動進行程式碼品質檢查

### 🚀 **完整 CI/CD 流水線**

- **多版本測試**: 跨 Python 版本的自動化測試
- **程式碼品質檢查**: ruff 檢查和格式化驗證
- **文檔部署**: 自動 GitHub Pages 部署
- **發布自動化**: 語義化版本控制和發布草稿
- **自動標籤**: 智能 PR 分類

### 📚 **文檔系統**

- **MkDocs Material**: 美觀且響應式的文檔
- **自動生成**: 從程式碼和筆記本自動生成文檔的腳本
- **API 文檔**: 自動 API 參考生成
- **部落格支援**: 內建專案更新部落格功能

### 🤖 **自動化腳本**

- **專案初始化**: `scripts/initpyrepo.go` 用於建立個人化專案
- **文檔生成**: `scripts/gen_docs.py` 用於自動生成文檔
- **Makefile 命令**: 常見開發任務自動化

## 🚀 快速開始

### 選項 1: 使用 GitHub 模板

1. 點擊 [<kbd>使用此模板</kbd>](https://github.com/Mai0313/repo_template/generate)
2. 配置您的新儲存庫
3. 複製並開始開發

### 選項 2: 使用初始化腳本

1. 複製此儲存庫
2. 執行初始化腳本：
    ```bash
    go run scripts/initpyrepo.go
    ```
3. 依照提示自訂您的專案

### 選項 3: 手動設定

1. 複製儲存庫
2. 安裝依賴：
    ```bash
    make uv-install  # 如果尚未安裝 uv
    uv sync          # 安裝專案依賴
    ```
3. 設定 pre-commit hooks：
    ```bash
    make format      # 執行 pre-commit hooks
    ```

### 選項 4: 快速自訂（推薦）

1. 複製此儲存庫
2. 全局替換 `repo_template` 為您的專案名稱（snake_case 格式）
3. 全局替換 `RepoTemplate` 為您的專案標題（PascalCase 格式）
4. 執行初始設定：
    ```bash
    make uv-install && uv sync && make format
    ```

## 📁 專案結構

```
├── .devcontainer/          # VS Code Dev Container 配置
├── .github/
│   ├── workflows/          # CI/CD 工作流程
│   └── copilot-instructions.md
├── docker/                 # Docker 配置
├── docs/                   # MkDocs 文檔
├── scripts/                # 自動化腳本
├── src/
│   └── repo_template/      # 主要套件
├── tests/                  # 測試套件
├── pyproject.toml          # 專案配置
├── Makefile               # 開發命令
└── README.md
```

## 🛠️ 可用命令

```bash
# 開發
make clean          # 清理自動生成的檔案
make format         # 執行 pre-commit hooks
make test           # 執行所有測試
make gen-docs       # 生成文檔

# 依賴管理
make uv-install     # 安裝 uv 依賴管理器
uv add <package>    # 添加生產依賴
uv add <package> --dev  # 添加開發依賴
```

## 🎯 包含內容

### CI/CD 工作流程

- **測試**: PR 上的多版本 Python 測試
- **程式碼品質**: 自動化 ruff 檢查和 pre-commit 驗證
- **文檔**: 自動 GitHub Pages 部署
- **發布**: 自動發布草稿和變更日誌生成
- **標籤**: 基於 PR 內容的自動標籤

### 開發工具

- **ruff**: 快速 Python 檢查器和格式化器
- **pytest**: 帶覆蓋率的測試框架
- **pre-commit**: 程式碼品質的 Git hooks
- **MkDocs**: 文檔生成
- **Docker**: 容器化開發和部署

### 專案模板

- **Python 套件**: 即用型套件結構
- **配置檔案**: 包含所有必要的配置檔案
- **文檔**: 完整的文檔設定
- **測試**: 全面的測試配置

## 🎨 自訂指南

### 專案名稱自訂

本模板設計為可透過簡單的全局替換快速自訂：

1. **替換套件名稱**: 將所有 `repo_template` 替換為您的專案名稱（建議使用 snake_case）
2. **替換專案標題**: 將所有 `RepoTemplate` 替換為您的專案標題（建議使用 PascalCase）
3. **更新中繼資料**: 修改 `pyproject.toml` 中的作者、描述等資訊

範例：

```bash
# 如果您的專案叫做 "awesome_project"
find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/repo_template/awesome_project/g'
find . -type f -name "*.py" -o -name "*.md" -o -name "*.toml" | xargs sed -i 's/RepoTemplate/AwesomeProject/g'
```

## 🤝 貢獻

我們歡迎貢獻！請隨時：

- 開啟問題回報錯誤或功能請求
- 提交拉取請求進行改進
- 分享您使用此模板的經驗

## 📖 文檔

詳細文檔請訪問：[https://mai0313.github.io/repo_template/](https://mai0313.github.io/repo_template/)

## 👥 貢獻者

[![Contributors](https://contrib.rocks/image?repo=Mai0313/repo_template)](https://github.com/Mai0313/repo_template/graphs/contributors)

Made with [contrib.rocks](https://contrib.rocks)

## 📄 授權

本專案採用 MIT 授權 - 詳見 [LICENSE](LICENSE) 檔案。
