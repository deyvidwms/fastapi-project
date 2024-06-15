from sqlalchemy.orm import Session

from app.tasks.models import Task

class TaskRepository:
    @staticmethod
    def get_tasks(db: Session) -> list[Task]:
        return db.query(Task).all()

    @staticmethod
    def get_task(db: Session, task_id: int) -> Task:
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def create_task(db: Session, title: str, description: str) -> Task:
        task = Task(title=title, description=description)
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def update_task(db: Session, task_id: int, title: str, description: str, completed: bool) -> Task:
        task = TaskRepository.get_task(db, task_id)
        task.title = title
        task.description = description
        task.completed = completed
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete_task(db: Session, task_id: int) -> None:
        task = TaskRepository.get_task(db, task_id)
        db.delete(task)
        db.commit()
        return task
