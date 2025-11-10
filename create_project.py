# create_project.py
import os
import sys

def create_project_structure():
    """创建完整的项目结构"""
    
    # 项目根目录
    project_name = "world_music_explorer"
    
    # 目录结构
    structure = {
        f"{project_name}": [
            # 后端
            "backend/app/__init__.py",
            "backend/app/main.py",
            "backend/app/models.py", 
            "backend/app/database.py",
            "backend/requirements.txt",
            "backend/data/instruments.json",
            "backend/data/quiz_questions.json",
            
            # 前端
            "frontend/app.py",
            "frontend/api_client.py", 
            "frontend/requirements.txt",
            
            # 资源文件
            "assets/audio/.gitkeep",
            "assets/images/.gitkeep",
            "assets/icons/.gitkeep",
            
            # 配置文件
            "requirements.txt",
            "start.py",
            "README.md",
            ".gitignore",
            ".env.example"
        ]
    }
    
    # 文件内容模板
    file_templates = {
        # 后端主应用
        "backend/app/main.py": '''from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(
    title="世界乐器探索 API",
    description="儿童乐器学习与文化探索平台",
    version="1.0.0"
)

# CORS配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 静态文件
app.mount("/assets", StaticFiles(directory="../../assets"), name="assets")

@app.get("/")
async def root():
    return {"message": "🎵 世界乐器探索API服务", "status": "running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/api/instruments")
async def get_instruments():
    """获取所有乐器"""
    return [
        {
            "id": "guzheng",
            "name": "古筝", 
            "country": "中国",
            "position": [39.9042, 116.4074],
            "description": "古筝是中国传统弹拨乐器，有2500多年历史...",
            "audio_url": "/api/audio/guzheng",
            "color": "#FF6B6B",
            "family": "string"
        },
        {
            "id": "sitar",
            "name": "西塔琴",
            "country": "印度", 
            "position": [28.6139, 77.2090],
            "description": "西塔琴是印度最具代表性的古典乐器...",
            "audio_url": "/api/audio/sitar",
            "color": "#4ECDC4",
            "family": "string"
        }
    ]

@app.get("/api/instruments/{instrument_id}")
async def get_instrument(instrument_id: str):
    """获取特定乐器"""
    instruments = await get_instruments()
    for inst in instruments:
        if inst["id"] == instrument_id:
            return inst
    return {"error": "乐器未找到"}

@app.get("/api/audio/{instrument_id}")
async def get_audio_info(instrument_id: str):
    """获取音频信息"""
    return {"audio_url": f"/assets/audio/{instrument_id}.mp3"}

@app.get("/api/quiz/random")
async def get_random_question():
    """获取随机问题"""
    import random
    questions = [
        {
            "id": "q1",
            "question": "古筝通常有多少根弦？",
            "options": ["16根", "21根", "25根", "30根"],
            "correct_answer": "21根",
            "explanation": "现代古筝通常有21根弦。",
            "instrument_id": "guzheng"
        }
    ]
    return random.choice(questions)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
''',

        # 数据模型
        "backend/app/models.py": '''from pydantic import BaseModel
from typing import List, Optional

class Instrument(BaseModel):
    id: str
    name: str
    country: str
    position: List[float]
    description: str
    audio_url: str
    color: str
    family: str

class QuizQuestion(BaseModel):
    id: str
    question: str
    options: List[str]
    correct_answer: str
    explanation: str
    instrument_id: str
''',

        # 数据库管理
        "backend/app/database.py": '''import json
import os
from typing import List, Dict

class DataManager:
    def __init__(self):
        self.data_dir = "data"
        
    def load_instruments(self) -> List[Dict]:
        """加载乐器数据"""
        try:
            with open(f"{self.data_dir}/instruments.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                return list(data.values()) if isinstance(data, dict) else data
        except FileNotFoundError:
            return []
    
    def load_quiz_questions(self) -> List[Dict]:
        """加载问答数据"""
        try:
            with open(f"{self.data_dir}/quiz_questions.json", "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
''',

        # 后端依赖
        "backend/requirements.txt": '''fastapi==0.104.1
uvicorn==0.24.0
python-multipart==0.0.6
pydantic==2.5.0
''',

        # 乐器数据
        "backend/data/instruments.json": '''{
    "guzheng": {
        "id": "guzheng",
        "name": "古筝",
        "country": "中国",
        "position": [39.9042, 116.4074],
        "description": "古筝是中国传统弹拨乐器，有2500多年历史，音色优美，表现力丰富。",
        "audio_url": "/api/audio/guzheng",
        "color": "#FF6B6B",
        "family": "string"
    },
    "sitar": {
        "id": "sitar",
        "name": "西塔琴", 
        "country": "印度",
        "position": [28.6139, 77.2090],
        "description": "西塔琴是印度最具代表性的古典乐器，音色悠扬，富有神秘色彩。",
        "audio_url": "/api/audio/sitar",
        "color": "#4ECDC4",
        "family": "string"
    },
    "bagpipes": {
        "id": "bagpipes",
        "name": "风笛",
        "country": "苏格兰",
        "position": [55.9533, -3.1883],
        "description": "风笛是苏格兰的传统乐器，声音洪亮，常用于庆典和军事场合。",
        "audio_url": "/api/audio/bagpipes", 
        "color": "#45B7D1",
        "family": "wind"
    }
}
''',

        # 问答数据
        "backend/data/quiz_questions.json": '''[
    {
        "id": "q1",
        "question": "古筝通常有多少根弦？",
        "options": ["16根", "21根", "25根", "30根"],
        "correct_answer": "21根",
        "explanation": "现代古筝通常有21根弦，但历史上弦数有所不同。",
        "instrument_id": "guzheng"
    },
    {
        "id": "q2", 
        "question": "西塔琴起源于哪个国家？",
        "options": ["中国", "印度", "日本", "埃及"],
        "correct_answer": "印度",
        "explanation": "西塔琴是13世纪在印度发展的乐器。",
        "instrument_id": "sitar"
    }
]
''',

        # 前端主应用
        "frontend/app.py": '''import streamlit as st
from api_client import api_client

def main():
    st.set_page_config(
        page_title="世界乐器探索",
        page_icon="🎵",
        layout="wide"
    )
    
    # 应用标题
    st.title("🌍 世界乐器探索")
    st.markdown("欢迎来到奇妙的世界乐器之旅！")
    
    # 检查API连接
    if not api_client.health_check():
        st.error("无法连接到API服务")
        return
    
    # 获取乐器数据
    instruments = api_client.get_instruments()
    
    # 显示乐器
    st.header("🎵 世界乐器")
    for instrument in instruments:
        with st.expander(f"{instrument['name']} - {instrument['country']}"):
            col1, col2 = st.columns(2)
            
            with col1:
                st.write(instrument['description'])
                audio_url = api_client.get_audio_url(instrument['id'])
                st.audio(audio_url)
                
            with col2:
                if st.button(f"学习{instrument['name']}", key=instrument['id']):
                    show_learning_page(instrument)

def show_learning_page(instrument):
    """显示学习页面"""
    st.header(f"🎵 {instrument['name']}")
    
    # 获取相关问题
    question = api_client.get_quiz_question(instrument['id'])
    if question:
        st.subheader("知识测试")
        st.write(f"**{question['question']}**")
        
        selected = st.radio("选择答案:", question['options'])
        
        if st.button("提交答案"):
            result = api_client.submit_answer(question['id'], selected)
            if result:
                if result['is_correct']:
                    st.success("✅ 回答正确！")
                else:
                    st.error("❌ 回答错误")
                st.write(f"**解释:** {result['explanation']}")

if __name__ == "__main__":
    main()
''',

        # API客户端
        "frontend/api_client.py": '''import requests
from typing import List, Dict, Optional

class APIClient:
    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
    
    def get_instruments(self) -> List[Dict]:
        """获取所有乐器"""
        try:
            response = self.session.get(f"{self.base_url}/api/instruments")
            return response.json()
        except:
            return []
    
    def get_instrument(self, instrument_id: str) -> Optional[Dict]:
        """获取单个乐器"""
        try:
            response = self.session.get(f"{self.base_url}/api/instruments/{instrument_id}")
            return response.json()
        except:
            return None
    
    def get_audio_url(self, instrument_id: str) -> str:
        """获取音频URL"""
        return f"{self.base_url}/assets/audio/{instrument_id}.mp3"
    
    def get_quiz_question(self, instrument_id: str = None) -> Optional[Dict]:
        """获取问答题目"""
        try:
            response = self.session.get(f"{self.base_url}/api/quiz/random")
            return response.json()
        except:
            return None
    
    def submit_answer(self, question_id: str, user_answer: str) -> Optional[Dict]:
        """提交答案"""
        try:
            data = {"question_id": question_id, "user_answer": user_answer}
            response = self.session.post(f"{self.base_url}/api/quiz/check", json=data)
            return response.json()
        except:
            return None
    
    def health_check(self) -> bool:
        """检查API状态"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False

# 全局客户端实例
api_client = APIClient()
''',

        # 前端依赖
        "frontend/requirements.txt": '''streamlit==1.28.0
requests==2.31.0
''',

        # 主依赖文件
        "requirements.txt": '''# 后端依赖
fastapi==0.104.1
uvicorn==0.24.0

# 前端依赖  
streamlit==1.28.0
requests==2.31.0

# 通用依赖
python-multipart==0.0.6
pydantic==2.5.0
''',

        # 启动脚本
        "start.py": '''import subprocess
import sys
import time
import webbrowser
import os

def start_backend():
    """启动后端服务"""
    print("🚀 启动后端API服务...")
    backend_dir = os.path.join(os.path.dirname(__file__), "backend")
    os.chdir(backend_dir)
    
    process = subprocess.Popen([
        sys.executable, "-m", "uvicorn", 
        "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"
    ])
    
    os.chdir(os.path.dirname(__file__))
    return process

def start_frontend():
    """启动前端服务"""
    print("🎨 启动前端应用...")
    time.sleep(3)
    
    frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
    os.chdir(frontend_dir)
    
    process = subprocess.Popen([
        sys.executable, "-m", "streamlit", "run", 
        "app.py", "--server.port", "8501"
    ])
    
    os.chdir(os.path.dirname(__file__))
    return process

def main():
    print("🎵 启动世界乐器探索应用...")
    
    backend = start_backend()
    frontend = start_frontend()
    
    time.sleep(5)
    
    webbrowser.open("http://localhost:8501")
    webbrowser.open("http://localhost:8000/docs")
    
    print("✅ 应用启动成功！")
    print("📱 前端: http://localhost:8501")
    print("📚 API文档: http://localhost:8000/docs")
    print("⏹️  按 Ctrl+C 停止服务")
    
    try:
        backend.wait()
        frontend.wait()
    except KeyboardInterrupt:
        print("🛑 停止服务...")
        backend.terminate()
        frontend.terminate()

if __name__ == "__main__":
    main()
''',

        # README文件
        "README.md": '''# 🌍 世界乐器探索

一个基于 FastAPI + Streamlit 的交互式乐器学习平台。

## 功能特色

- 🗺️ 交互式世界地图
- 🎵 多种乐器介绍
- 🔊 真实乐器音色
- ❓ 文化知识问答
- 📱 响应式界面

## 快速开始

### 安装依赖
\\`\\`\\`bash
pip install -r requirements.txt
\\`\\`\\`

### 启动应用
\\`\\`\\`bash
python start.py
\\`\\`\\`

### 单独启动

后端API:
\\`\\`\\`bash
cd backend
uvicorn app.main:app --reload
\\`\\`\\`

前端界面:
\\`\\`\\`bash
cd frontend  
streamlit run app.py
\\`\\`\\`

## 访问地址

- 前端界面: http://localhost:8501
- API文档: http://localhost:8000/docs
''',

        # Git忽略文件
        ".gitignore": '''# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
ENV/

# 虚拟环境
music_env/

# 环境变量
.env
.venv

# 编辑器
.vscode/
.idea/
*.swp
*.swo

# 系统文件
.DS_Store
Thumbs.db

# 日志文件
*.log

# 音频文件（如果较大）
assets/audio/*.mp3
!assets/audio/.gitkeep
''',

        # 环境变量示例
        ".env.example": '''# FastAPI 配置
HOST=0.0.0.0
PORT=8000
DEBUG=True

# 数据库配置（未来扩展）
DATABASE_URL=sqlite:///./music.db
'''
    }
    
    print(f"🎵 创建项目: {project_name}")
    
    # 创建目录和文件
    for base_dir, files in structure.items():
        for file_path in files:
            full_path = os.path.join(base_dir, file_path)
            directory = os.path.dirname(full_path)
            
            # 创建目录
            os.makedirs(directory, exist_ok=True)
            
            # 创建文件
            if file_path in file_templates:
                with open(full_path, 'w', encoding='utf-8') as f:
                    f.write(file_templates[file_path])
                print(f"📄 创建文件: {full_path}")
            else:
                # 创建空文件
                open(full_path, 'w').close()
                print(f"📁 创建文件: {full_path}")
    
    print(f"✅ 项目创建完成！")
    print(f"📁 项目路径: {project_name}")
    print(f"🚀 下一步: cd {project_name} && pip install -r requirements.txt")

def create_virtual_env():
    """创建虚拟环境（可选）"""
    project_name = "world_music_explorer"
    
    print("\n🔧 创建虚拟环境...")
    try:
        # 创建虚拟环境
        os.system(f"cd {project_name} && python -m venv music_env")
        print("✅ 虚拟环境创建成功")
        
        # 激活说明
        print("\n💡 激活虚拟环境:")
        print("Windows: music_env\\Scripts\\activate")
        print("Mac/Linux: source music_env/bin/activate")
        
    except Exception as e:
        print(f"❌ 虚拟环境创建失败: {e}")

if __name__ == "__main__":
    create_project_structure()
    
    # 询问是否创建虚拟环境
    create_env = input("\n是否创建虚拟环境? (y/n): ").lower().strip()
    if create_env in ['y', 'yes']:
        create_virtual_env()
    
    print("\n🎉 项目初始化完成！")
    print("下一步操作:")
    print("1. cd world_music_explorer")
    print("2. 激活虚拟环境（如果创建了）")
    print("3. pip install -r requirements.txt") 
    print("4. python start.py")