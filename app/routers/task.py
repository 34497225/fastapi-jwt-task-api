from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas, crud
from app.database import SessionLocal

from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError

from app.auth import SECRET_KEY, ALGORITHM

security = HTTPBearer()

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    """
    從 Authorization header 取得 token 並驗證
    """
    # 🔹 1. 拿 token（已經去掉 Bearer）
    token = credentials.credentials
    print("TOKEN:", token)
    try:
        # 🔹 2. 解碼 JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # 🔹 3. 拿出 username
        username = payload.get("sub")

        # 🔹 4. 檢查是否存在
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except JWTError:
        # 🔹 5. token 錯誤或過期
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/tasks", response_model=schemas.TaskOut)
def create(task: schemas.Task, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@router.get("/tasks", response_model=list[schemas.TaskOut])
def read_all(db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    return crud.get_tasks(db)

@router.get("/tasks/{task_id}", response_model=schemas.TaskOut)
def read_one(task_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    task = crud.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=schemas.TaskOut)
def update(task_id: int, updated_task: schemas.Task, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    task = crud.update_task(db, task_id, updated_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/tasks/{task_id}", response_model=schemas.TaskOut)
def delete(task_id: int, db: Session = Depends(get_db), user: str = Depends(get_current_user)):
    task = crud.delete_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
