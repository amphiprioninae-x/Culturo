import requests
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
