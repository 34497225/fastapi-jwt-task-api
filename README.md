# FastAPI Task Manager (Docker + PostgreSQL)

## 📌 Overview

This is a backend API project built with FastAPI.
It includes authentication (JWT), database integration (PostgreSQL), and containerization using Docker.

## 🚀 Features

* User Registration & Login (JWT Authentication)
* CRUD API for Tasks
* PostgreSQL Database
* Docker & Docker Compose setup

## 🛠 Tech Stack

* FastAPI
* PostgreSQL
* SQLAlchemy
* Docker / Docker Compose
* JWT Authentication

## ⚙️ Setup (Local)

### 1. Clone repository

git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git

### 2. Run with Docker

docker-compose up --build

### 3. Open API docs

http://localhost:8000/docs

## 📂 Project Structure

app/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── auth.py

## 🔐 Authentication

* Uses JWT token
* Login to get token
* Use "Authorize" in Swagger UI

## 🐳 Docker

* API + PostgreSQL via docker-compose
* Persistent database using volumes

## 📈 Future Improvements

* User-task ownership
* Pagination
* Deployment to cloud (AWS / Render)

## 👨‍💻 Author

Your Name
