from pydantic import BaseModel
from typing import List

class AgentReview(BaseModel):
    concerns: List[str]
    suggestions: List[str]
    severity: str  # low, medium, high


class FinalReview(BaseModel):
    overall_score: float
    top_risks: List[str]
    priority_fixes: List[str]
    recommended_architecture: str
