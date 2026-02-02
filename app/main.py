from fastapi import FastAPI, Request
from app.routes.review import router as review_router
from app.routes.analyze import router as analyze_router
from app.logging import logger
import time

app = FastAPI(title="Agentic AI Backend")

# ---- Observability middleware ----
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = round(time.time() - start, 3)

    logger.info(
        f"{request.method} {request.url.path} {response.status_code} {duration}s"
    )
    return response

# ---- Routes ----
app.include_router(review_router, prefix="/review")
app.include_router(analyze_router, prefix="/analyze")
