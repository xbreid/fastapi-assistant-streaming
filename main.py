import logging

from fastapi import FastAPI

from app.api.v1 import assistant
from app.core.config import settings

logging.basicConfig(level=logging.DEBUG)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

app.include_router(assistant.router, prefix=settings.API_V1_STR)


@app.get("/", tags=["Root"])
async def health():
    """Check the api is running"""
    return {"status": "👌"}
