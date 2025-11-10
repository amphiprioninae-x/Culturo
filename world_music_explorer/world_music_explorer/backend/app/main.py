from fastapi import FastAPI
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
