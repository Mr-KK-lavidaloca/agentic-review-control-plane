from fastapi import APIRouter, Request
from app.schemas.analyze import AnalyzeRequest, AnalyzeResponse
from app.services.reviewer import run_analysis
from core.limiter import limiter

router = APIRouter()

@limiter.limit("5/minute")
@router.post("/", response_model=AnalyzeResponse)
async def analyze_design(request: Request, req: AnalyzeRequest):
    return await run_analysis(req.design)


