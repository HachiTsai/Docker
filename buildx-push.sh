#!/bin/bash

# 映像名稱與版本
IMAGE_NAME="hachitsai/mylab1"
IMAGE_TAG="1.2"

# Dockerfile 路徑與建構上下文
DOCKERFILE="base-image/Dockerfile"
CONTEXT="base-image"

# 建構平台
PLATFORMS="linux/amd64,linux/arm64"

echo "🚀 建構並推送映像：$IMAGE_NAME:$IMAGE_TAG"
echo "🧬 支援平台：$PLATFORMS"
echo "📁 建構上下文：$CONTEXT"

# 執行建構與推送
docker buildx build \
    --platform "$PLATFORMS" \
    -f "$DOCKERFILE" \
    -t "$IMAGE_NAME:$IMAGE_TAG" \
    "$CONTEXT" \
    --push
