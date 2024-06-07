import logging
import aiofiles
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.api.v1 import assistant
from app.core.config import settings

logging.basicConfig(level=logging.INFO)

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION,
)

# Povolit CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(assistant.router, prefix=settings.API_V1_STR)

@app.get("/healthcheck",tags=["Root"])
async def health():
    """Check the api is running"""
    return {"status": "👌"}

@app.get("/", response_class=HTMLResponse, tags=["Root"])
async def get_chat_page():
    """Get root html page"""
    async with aiofiles.open("static/index.html", mode='r') as file:
        html_content = await file.read()
    return HTMLResponse(content=html_content)
