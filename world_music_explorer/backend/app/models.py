from pydantic import BaseModel
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
