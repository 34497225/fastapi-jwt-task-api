from sqlalchemy.orm import Session
from app.models import TaskModel

def create_task(db: Session, task):
    db_task = TaskModel(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(TaskModel).all()

def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()

def update_task(db: Session, task_id: int, updated_task):
    task = get_task(db, task_id)
    if not task:
        return None

    for key, value in updated_task.dict().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = get_task(db, task_id)
    if not task:
        return None

    db.delete(task)
    db.commit()
    return task