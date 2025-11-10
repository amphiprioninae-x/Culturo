# 🌍 世界乐器探索

一个基于 FastAPI + Streamlit 的交互式乐器学习平台。

## 功能特色

- 🗺️ 交互式世界地图
- 🎵 多种乐器介绍
- 🔊 真实乐器音色
- ❓ 文化知识问答
- 📱 响应式界面

## 快速开始

### 安装依赖
\`\`\`bash
pip install -r requirements.txt
\`\`\`

### 启动应用
\`\`\`bash
python start.py
\`\`\`

### 单独启动

后端API:
\`\`\`bash
cd backend
uvicorn app.main:app --reload
\`\`\`

前端界面:
\`\`\`bash
cd frontend  
streamlit run app.py
\`\`\`

## 访问地址

- 前端界面: http://localhost:8501
- API文档: http://localhost:8000/docs
