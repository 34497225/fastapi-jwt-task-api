🚀 FastAPI Task Management API | 企業級任務管理系統

這是一個基於 FastAPI + PostgreSQL 構建的高性能 RESTful API 服務。本專案不僅實現了完整的任務 CRUD 邏輯與 JWT 無狀態身份驗證，更導入了現代化的 Docker 容器化 與 GitHub Actions CI/CD 流程，達成 AWS 雲端的 Zero-Touch 自動化部署。

🌐 線上 API 文件 (Swagger UI)

FastAPI 內建了互動式的 API 測試介面，您可以直接點擊下方連結進行線上測試：

    📜 互動式 API 文件 (Live Demo): http://43.212.25.222:8000/docs

    📊 系統實時狀態 (Uptime Kuma): http://43.212.25.222:3001

🛠️ 技術棧 (Tech Stack)

    後端與資料庫 (Backend & Database)

    核心框架: FastAPI (Python 3.9+) - 極速非同步網頁框架

    關聯式資料庫: PostgreSQL 15

    ORM 框架: SQLAlchemy - 處理資料庫映射與查詢

    身份驗證: OAuth2 with Password (and hashing), JWT (JSON Web Tokens)

    密碼加密: Passlib (Bcrypt)

    維運與基礎設施 (DevOps & Infrastructure)

    容器化技術: Docker & Docker Compose

    雲端主機: AWS EC2 (t3.micro)

    自動化部署: GitHub Actions (CI/CD Pipeline)

    網頁伺服器: Uvicorn (ASGI)

🏗️ 系統架構圖 (Architecture Diagram)

[Client / 前端] -> [AWS 防火牆 (Port 8000)] -> [Uvicorn ASGI 伺服器]
                                                    |
                                            [FastAPI 應用程式]
                                                    |
                                      +-------------+-------------+
                                      |                           |
                            [JWT Auth 驗證模組]         [SQLAlchemy ORM]
                                                                  |
                                                    [PostgreSQL 15 資料庫]


🚀 核心專案亮點 (Project Highlights)

1. 現代化 JWT 身份驗證機制

    實作 OAuth2 密碼授權流程，配發帶有過期時間的 JWT Access Token。

    密碼透過 bcrypt 進行單向雜湊加密存儲，保障使用者帳號安全。

    所有任務 API (/tasks) 皆受到依賴注入 (Dependency Injection) 的保護，確保資料隔離。

2. 生產級 DevOps 與自動化 (CI/CD)

    環境隔離：透過 Docker Compose 將 FastAPI 與 PostgreSQL 打包，確保本地開發與雲端生產環境 100% 一致。

    Zero-Touch 部署：編寫 GitHub Actions 流水線，當代碼推送到 main 分支時，自動透過 SSH 登入 AWS 進行 docker-compose up --build -d 滾動更新。

    機密管理 (Secrets)：嚴格遵守安全規範，將 DATABASE_URL 與 SECRET_KEY 等敏感資訊存放於 GitHub Secrets，於部署時動態注入，實現密鑰不落地。


⚙️ 快速啟動 (Local Development)

若您想在本地端運行此專案進行測試，請依照以下步驟操作：

1. 取得程式碼

    git clone https://github.com/34497225/fastapi-jwt-task-api.git
    cd fastapi-jwt-task-api


2. 設定環境變數

在專案根目錄建立 .env 檔案，並填入以下內容：

    # 本地端測試用 (指向 Docker 內的 db)
    DATABASE_URL=postgresql://user:password@db:5432/mydb
    SECRET_KEY=your_super_secret_key_for_local_dev_only
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30


3. 一鍵啟動 (Docker Compose)

    請確保您的電腦已安裝 Docker Desktop。

    docker compose up --build -d


👉 啟動後，請打開瀏覽器訪問 http://localhost:8000/docs 即可看到自動生成的 Swagger UI 並開始測試 API！

👨‍💻 作者 (Author)

smg60214 * GitHub: https://github.com/34497225

專注於後端開發、雲端架構 (AWS) 與 SRE 維運自動化。