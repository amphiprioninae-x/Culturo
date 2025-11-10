import json
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
