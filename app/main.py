from fastapi import FastAPI
from app.database import engine, Base
from app.routers import task
from app.routers import auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(task.router)
app.include_router(auth.router)