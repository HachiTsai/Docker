#!/bin/bash

# 映像名稱與版本
IMAGE_NAME="hachitsai/mylab1"
IMAGE_TAG="1.2"

# Dockerfile 路徑
DOCKERFILE="base-image/Dockerfile"

# 預設平台
DEFAULT_PLATFORM="linux/amd64,linux/arm64"

# 接收參數：平台選擇（例如 arm64、amd64）
if [ "$1" == "arm64" ]; then
    PLATFORM="linux/arm64"
elif [ "$1" == "amd64" ]; then
    PLATFORM="linux/amd64"
else
    PLATFORM="$DEFAULT_PLATFORM"
fi

echo "🧬 建構平台：$PLATFORM"

# 判斷建構上下文
if [ -f "base-image/myenv.yml" ]; then
    CONTEXT="base-image"
    echo "📁 使用 base-image/ 作為建構上下文"
elif [ -f "myenv.yml" ]; then
    CONTEXT="."
    echo "📁 使用目前目錄作為建構上下文"
else
    echo "❌ 找不到 myenv.yml，請確認檔案位置"
    exit 1
fi

# 執行建構
echo "🚀 開始建構映像：$IMAGE_NAME:$IMAGE_TAG"
docker buildx build \
    --platform "$PLATFORM" \
    -f "$DOCKERFILE" \
    -t "$IMAGE_NAME:$IMAGE_TAG" \
    "$CONTEXT" \
    --load
