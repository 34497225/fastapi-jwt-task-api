from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite 資料庫（存在本地檔案）
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# 建立 engine（連接資料庫）
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# 建立 Session（操作 DB 用）
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base（所有 model 都要繼承）
Base = declarative_base()