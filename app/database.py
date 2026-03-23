
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 🔹 載入 .env 檔案中的變數
load_dotenv()

# 🔹 從環境變數讀取 DATABASE_URL
# 如果環境中沒有 DATABASE_URL，則預設連線到本地 SQLite (方便完全沒資料庫時測試)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# 建立 engine（連接資料庫）
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# 建立 Session（操作 DB 用）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base（所有 model 都要繼承）
Base = declarative_base()