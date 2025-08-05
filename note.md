# 🐳 技術指南：建立 Docker 映像並推送至 Docker Hub

本文件包含完整步驟與錯誤排解，適用於將本機專案打包並公開至 Docker Hub，適合快速部署與環境重現。

---

## 🧱 建立本機專案

```bash
#mkdir my-python-app
#cd my-python-app
#git init

# app.py
# print("Hello from Docker!")

# requirements.txt
#numpy
#pandas
#flask
#matplotlib


# 建立 Dockerfile：


# -Dockerfile
#FROM python:3.11-slim
#WORKDIR /app
#COPY requirements.txt .
#RUN pip install -r requirements.txt
#COPY . .
#CMD ["python", "app.py"]

# bash 建立
# docker build -t my-python-app .

#測試 docker run

# 映像重新標記並推送
#docker tag my-python-app hachitsai/my-python-app:v1
#docker push hachitsai/my-python-app:v1

###💥 常見錯誤排除
#❌ 錯誤訊息：push access denied, repository does not exist or may require authorization
#排解方式：

#使用正確的帳號命名（你的帳號/專案名稱:tag）

#Docker Hub 上建立對應的 repository（非自動建立）

#確保已正確登入帳號 (docker login)

#確認使用的是你的帳號：docker info | grep Username


##🔁 在其他機器拉取並執行
#docker pull hachitsai/my-python-app:v1
#docker run --rm hachitsai/my-python-app:v1

#📄 建議搭配 .dockerignore
#__pycache__/
#.git
#*.log
#.env

#docker images remove ---刪除鏡像
