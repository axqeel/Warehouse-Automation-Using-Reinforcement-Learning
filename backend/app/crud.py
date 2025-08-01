from sqlalchemy.orm import Session
from . import models, schemas

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def get_product_by_location(db: Session, x: int, y: int, z: int):
    return db.query(models.Product).filter(models.Product.x == x, models.Product.y == y, models.Product.z == z).first()

def get_robot(db: Session, robot_id: int):
    return db.query(models.Robot).filter(models.Robot.id == robot_id).first()

def get_idle_robot(db: Session):
    return db.query(models.Robot).filter(models.Robot.status == "idle").first()

def create_task_history(db: Session, task: schemas.TaskHistoryBase):
    db_task = models.TaskHistory(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_product_location(db: Session, product_id: int, x: int, y: int, z: int, status: str):
    product = get_product(db, product_id)
    if product:
        product.x = x
        product.y = y
        product.z = z
        product.status = status
        db.commit()
        db.refresh(product)
    return product

def update_robot_status(db: Session, robot_id: int, status: str, current_task: str = None):
    robot = get_robot(db, robot_id)
    if robot:
        robot.status = status
        robot.current_task = current_task
        db.commit()
        db.refresh(robot)
    return robot
