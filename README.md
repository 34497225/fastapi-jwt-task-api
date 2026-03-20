FastAPI JWT Task Manager API
📌 Description

A backend RESTful API built with FastAPI, featuring JWT authentication and task management.

🚀 Features

User registration & login

JWT authentication

Protected endpoints

Task CRUD operations

🛠 Tech Stack

FastAPI

SQLAlchemy

SQLite

JWT (python-jose)

Passlib (bcrypt)

📂 Structure

app/
├── main.py
├── models.py
├── schemas.py
├── crud.py
├── auth.py
└── routers/

▶️ Run

uvicorn app.main --reload

🔐 API

POST /register
POST /login
GET /tasks
POST /tasks
PUT /tasks/{id}
DELETE /tasks/{id}

🧠 What I Learned

Implemented JWT authentication

Built modular backend architecture

Designed RESTful APIs