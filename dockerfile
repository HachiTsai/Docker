# Dockerfile
FROM python:3.12-slim

# 設定工作目錄
WORKDIR /app

# 複製套件需求
COPY requirements.txt .

# 安裝套件
RUN pip install --no-cache-dir -r requirements.txt

# 複製程式碼
COPY . .

# 預設指令（可選）
CMD ["python", "main.py"]
