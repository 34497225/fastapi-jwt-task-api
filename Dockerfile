# ① 拿一台「已經有 Python 的乾淨電腦」
FROM python:3.11-slim

# ② 在這台電腦裡建立一個資料夾 /app
WORKDIR /app

# ③ 把你的 requirements.txt 複製進去
COPY requirements.txt .

# ④ 安裝 Python 套件
RUN pip install -r requirements.txt

# ⑤ 把你整個專案複製進去
COPY . .

# ⑥ 開放 8000 port（給外面連）
EXPOSE 8000

# ⑦ 啟動 FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]