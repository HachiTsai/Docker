#!/bin/bash

# 預設版本（可覆寫）
PYTHON_VERSION=${PYTHON_VERSION:-3.12}
IMAGE_NAME=${IMAGE_NAME:-hachitsai/mylab1}
TAG=${TAG:-latest}
DOCKERFILE_PATH=${DOCKERFILE_PATH:-Docker/Dockerfile}
CONTEXT_PATH=${CONTEXT_PATH:-Docker}

# 顯示設定資訊
echo "📦 Python Version: $PYTHON_VERSION"
echo "🐳 Image Name: $IMAGE_NAME:$TAG"

# 進行建置
docker buildx build --platform linux/amd64,linux/arm64 \
  -f $DOCKERFILE_PATH \
  -t $IMAGE_NAME:$TAG \
  --build-arg PYTHON_VERSION=$PYTHON_VERSION \
  --push $CONTEXT_PATH
