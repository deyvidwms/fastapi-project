from fastapi import FastAPI

from app.tasks.endpoints import router as task_router

app = FastAPI()

app.include_router(task_router, prefix="/tasks", tags=["tasks"])