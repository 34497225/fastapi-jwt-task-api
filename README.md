🚀 FastAPI 全自動化維運專案：Task Management API

這是一個具備 CI/CD 自動化部署、環境變數安全管理與即時監控系統的後端專案。旨在展示如何將現代 DevOps 流程應用於雲端生產環境。

🌐 線上展示與監控

API 互動式文件 (Swagger UI): http://43.213.31.81:8000/docs

系統實時狀態頁 (Status Page): http://43.213.31.81:3001/status/server

🛠️ 技術棧 (Tech Stack)

後端框架: FastAPI (Python 3.9+)

資料庫: PostgreSQL 15 (Dockerized)

容器化技術: Docker & Docker Compose

雲端平台: AWS EC2 (ARM64 / Graviton 處理器)

自動化維運: GitHub Actions, GitHub Secrets, Uptime Kuma

🏗️ 系統架構亮點

1. 全自動 CI/CD 流水線

實現方式: 使用 GitHub Actions 監聽 main 分支變動。

部署邏輯: 當代碼推送到 GitHub 時，自動觸發 SSH 連線至 AWS EC2，執行遠端編譯與熱更新，達成 Zero-Touch Deployment。

2. 環境變數安全隔離 (Secret Injection)

遵循 Secrets Separation 原則：敏感資訊（如資料庫連線字串、JWT 密鑰）絕不存入 Git。

部署期間透過 GitHub Secrets 動態注入伺服器端的 .env，確保生產環境密鑰不落地。

3. 可觀測性與即時監控 (Monitoring)

整合 Uptime Kuma 進行 24/7 持續監控。

具備自動重試機制與公開狀態頁，即時追蹤 API 延遲 (Latency) 與在線率 (Uptime)。

4. 資源優化與資料持久化

記憶體優化: 在 AWS t3.micro (1GB RAM) 環境下，手動配置 2GB Swap 空間，確保 Docker 編譯穩定性。

持久化儲存: 使用 Docker Volumes 管理資料庫檔案，確保服務更新或重啟時資料不遺失。

📂 專案結構

app/
├── main.py        # 程式入口與路由整合
├── models.py      # SQLAlchemy 資料庫模型
├── schemas.py     # Pydantic 資料驗證模型
├── database.py    # 資料庫連線配置
├── auth.py        # JWT 驗證與密碼雜湊邏輯
├── routers/       # 模組化路由管理 (Auth, Tasks)
.github/           # GitHub Actions CI/CD 配置
docker-compose.yml # 容器編排配置


⚙️ 快速啟動 (Local Development)

1. 複製專案

git clone https://github.com/34497225/fastapi-jwt-task-api.git
cd fastapi-jwt-task-api


2. 設定環境變數

請在根目錄建立 .env 檔案：

DATABASE_URL=postgresql://user:password@db:5432/mydb
SECRET_KEY=your_super_secret_key
ALGORITHM=HS256


3. 使用 Docker 啟動

docker-compose up --build -d


🛡️ 安全維護 (Security & Admin)

資料庫管理: 支援透過 DBeaver 進行加密遠端維護 (Port 5432)。

日誌查詢:

docker compose logs -f api (API 運作日誌)

docker logs uptime-kuma (監控系統日誌)

👨‍💻 作者

smg60214 - GitHub