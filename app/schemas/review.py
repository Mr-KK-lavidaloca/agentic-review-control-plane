from pydantic import BaseModel
from typing import List

class ReviewRequest(BaseModel):
    design: str

class ReviewResponse(BaseModel):
    overall_score: float
    top_risks: List[str]
    priority_fixes: List[str]
    recommended_architecture: str
