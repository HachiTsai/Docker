# 🐳 技術指南：建立 Docker 映像並推送至 Docker Hub

本文件包含完整步驟與錯誤排解，適用於將本機專案打包並公開至 Docker Hub，適合快速部署與環境重現。

---

## ID對應指令

| 節點 | 指令 |用途 |
|------|--------------------------------------------------|-------------------|
| Dockerfile    | `備註*1`        |建立dockerfile |
| requirements.txt    | `備註*2`        |需要pip install的項目 |
| A    | `docker buildx create --name multi-builder --use` | 建builder(buildx才可以跨平台)|
| B    | `docker buildx inspect --bootstrap`              |執行|
| C    | `docker buildx build --platform ...`             | |
| E    | `--load`                                          | |
| F    | `docker run --rm filename:version`           | 刪除IMAGE|
| G    | `docker pull hachitsai/filename:version`           | 🔁 在其他機器拉取並執行|
| H    | `docker buildx ls`                    |🧭定期檢查 |
| I    | `docker buildx rm my-builder`        |🗑️ 刪除指定 builder |
| J    | `備註*3`           | 建立IMAGE|


## 備註區
### *1
FROM python:3.12-slim  
WORKDIR /app  
COPY . .  
RUN pip install --no-cache-dir -r requirements.txt  
CMD ["python", "main.py"]  
### *2
numpy==1.26.4  
pandas==2.2.2  
flask==3.0.3  
matplotlib==3.8.4  
scikit-learn==1.4.2  
tensorflow==2.15.0  
### *3
cd Docker  
docker buildx build --platform linux/amd64,linux/arm64 \  
  -t hachitsai/mylab1:tag \  
  --push .  
