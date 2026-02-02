import pytest
from httpx import AsyncClient, ASGITransport
from fastapi import HTTPException
from app.main import app

transport = ASGITransport(app=app)

@pytest.mark.asyncio
async def test_health_check():
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        res = await client.get("/review/health")

    assert res.status_code == 200
    assert res.json() == {"status": "ok"}


@pytest.mark.asyncio
async def test_analyze_success():
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {"design": "Simple FastAPI app with no auth and one EC2 instance"}
        res = await client.post("/analyze/", json=payload)

    assert res.status_code == 200
    data = res.json()
    assert "key_risks" in data
    assert "quick_suggestions" in data



