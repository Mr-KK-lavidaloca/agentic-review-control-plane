from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    design: str

class AnalyzeResponse(BaseModel):
    key_risks: List[str]
    quick_suggestions: List[str]
