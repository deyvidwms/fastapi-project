from fastapi import APIRouter, Depends, HTTPException, status, Response

from sqlalchemy.orm import Session

from app.tasks.models import Task
from app.database.db import engine, Base, get_db
from app.tasks.repositories import TaskRepository
from app.tasks.schemas import TaskCreate, TaskUpdate, Task

Base.metadata.create_all(bind=engine)

router = APIRouter()

@router.get("/", response_model=list[Task])
def get_tasks(db: Session = Depends(get_db)):
    tasks = TaskRepository.get_tasks(db)
    return tasks

@router.get("/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = TaskRepository.get_task(db, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    task = TaskRepository.create_task(db, task.title, task.description)
    return Task.from_orm(task)

@router.put("/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    task = TaskRepository.update_task(db, task_id, task.title, task.description, task.completed)
    return Task.from_orm(task)

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    TaskRepository.delete_task(db, task_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)