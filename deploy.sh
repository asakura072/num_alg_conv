#!/bin/bash
echo "开始部署 Flask 应用到 Render..."

# 1. 初始化 Git
git init
git add .
git commit -m "部署到 Render"

# 2. 推送到 GitHub
git remote add origin https://github.com/asakura072/num_alg_conv.git
git branch -M main
git push -u origin main

echo "✅ 代码已推送到 GitHub"
echo "👉 现在请到 https://render.com 连接仓库并部署"