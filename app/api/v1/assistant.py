from fastapi import APIRouter, Body, Depends
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from app.dependencies.common import get_assistant_service
from app.services.assistant_service import AssistantService
from app.services.event_handler import EventHandler

router = APIRouter()


@router.get("/assistant")
async def get_assistant(
    assistant_service: AssistantService = Depends(get_assistant_service),
):
    return await assistant_service.get_assistant()


@router.post("/assistant/threads")
async def post_thread(
    assistant_service: AssistantService = Depends(get_assistant_service),
):
    thread = await assistant_service.create_thread()

    return {"data": thread}


class Query(BaseModel):
    text: str
    thread_id: str


@router.post("/assistant/chat")
async def chat(
    query: Query = Body(...),
    assistant_service: AssistantService = Depends(get_assistant_service),
):
    thread = await assistant_service.retrieve_thread(query.thread_id)

    await assistant_service.create_message(thread.id, query.text)

    stream_it = EventHandler()
    gen = assistant_service.create_gen(thread, stream_it)
    return StreamingResponse(gen, media_type="text/event-stream")
