# ===============================
# FastAPI 相關
# ===============================
from fastapi import APIRouter, Depends, HTTPException
# ↑ APIRouter：建立 API 分組
# ↑ Depends：依賴注入（拿 DB）
# ↑ HTTPException：回傳錯誤

from sqlalchemy.orm import Session
# ↑ DB session 型別

# ===============================
# 專案內部模組
# ===============================
from app import schemas, models, auth
# ↑ schemas：Pydantic
# ↑ models：DB
# ↑ auth：hash + JWT

from app.database import SessionLocal
# ↑ 建立 DB session


# ===============================
# 建立 router
# ===============================
router = APIRouter()


# ===============================
# DB 連線（依賴注入）
# ===============================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ===============================
# 註冊 API
# ===============================
@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    註冊新使用者
    """

    # 🔹 1. 檢查帳號是否已存在
    existing_user = db.query(models.UserModel)\
        .filter(models.UserModel.username == user.username)\
        .first()

    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
        # ↑ 防止重複帳號


    # 🔹 2. 將密碼加密
    hashed_password = auth.hash_password(user.password)
    # ↑ 明碼 → hash


    # 🔹 3. 建立 DB 物件
    db_user = models.UserModel(
        username=user.username,
        password=hashed_password
    )


    # 🔹 4. 存進 DB
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    # ↑ refresh 讓 id 回來


    # 🔹 5. 回傳（不含 password）
    return db_user


# ===============================
# 登入 API
# ===============================
@router.post("/login")
def login(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    使用者登入
    """

    # 🔹 1. 找使用者
    db_user = db.query(models.UserModel)\
        .filter(models.UserModel.username == user.username)\
        .first()


    # 🔹 2. 驗證帳號 + 密碼
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
        # ↑ 帳號或密碼錯


    # 🔹 3. 建立 JWT token
    token = auth.create_access_token({
        "sub": user.username
        # ↑ token 內容（記錄是誰）
    })

    print("TOKEN CREATED:", token)
    # 🔹 4. 回傳 token
    return {
        "access_token": token,
        "token_type": "bearer"
    }