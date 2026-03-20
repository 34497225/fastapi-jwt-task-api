from sqlalchemy import Column, Integer, String, Boolean
# 匯入 SQLAlchemy 欄位型別
from sqlalchemy import Column, Integer, String

# 匯入 Base（所有資料表都要繼承）
from app.database import Base

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

class TaskModel(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    done = Column(Boolean, default=False)