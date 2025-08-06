#!/bin/bash

# 一鍵執行 Docker 登入、拉取、啟動容器

# 設定帳號與 image 名稱
dockerUser="hachitsai"
imageName="$dockerUser/mylab:1.1"

echo "🔐 登入 Docker Hub..."
docker login --username "$dockerUser"

echo "📦 拉取 image: $imageName"
docker pull "$imageName"

echo "🚀 啟動容器並進入 bash"
docker run -it "$imageName" /bin/bash
