from fastapi import FastAPI
from app.database import engine
from app.models import Base
from app.routers import task
from app.routers import auth

app = FastAPI()

# --- 新增這段來測試自動化部署 ---
@app.get("/")
def read_root():
    return {"message": "Hello! GitHub Actions 自動部署成功了！"}
# ----------------------------


Base.metadata.create_all(bind=engine)

app.include_router(task.router)
app.include_router(auth.router)