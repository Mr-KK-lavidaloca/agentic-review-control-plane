from fastapi import APIRouter, Request
from app.schemas.review import ReviewRequest, ReviewResponse
from app.services.reviewer import run_review
from core.limiter import limiter

router = APIRouter()

@limiter.limit("5/minute")
@router.post("/analyze", response_model=ReviewResponse)
async def analyze_design(request: Request, req: ReviewRequest):
    return await run_review(req.design)

@router.get("/health")
def health():
    return {"status": "ok"}



