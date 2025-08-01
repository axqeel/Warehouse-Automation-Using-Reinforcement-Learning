from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import crud, schemas, models

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/collect")
def collect_item(request: schemas.CollectRequest, db: Session = Depends(get_db)):
    robot = crud.get_idle_robot(db)
    if not robot:
        raise HTTPException(status_code=400, detail="No idle robot available")
    product = crud.get_product(db, request.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Simulate robot moving to target and collecting
    crud.update_robot_status(db, robot.id, "active", f"Collecting product {product.id}")
    crud.update_product_location(db, product.id, *request.target, "in_transit")
    crud.create_task_history(db, schemas.TaskHistoryBase(
        operation="collect", product_id=product.id, robot_id=robot.id, details=f"To {request.target}"
    ))
    crud.update_robot_status(db, robot.id, "idle", None)
    return {"status": "success", "robot_id": robot.id}

@router.post("/deposit")
def deposit_item(request: schemas.DepositRequest, db: Session = Depends(get_db)):
    robot = crud.get_idle_robot(db)
    if not robot:
        raise HTTPException(status_code=400, detail="No idle robot available")
    product = crud.get_product(db, request.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    crud.update_robot_status(db, robot.id, "active", f"Depositing product {product.id}")
    crud.update_product_location(db, product.id, *request.destination, "stored")
    crud.create_task_history(db, schemas.TaskHistoryBase(
        operation="deposit", product_id=product.id, robot_id=robot.id, details=f"To {request.destination}"
    ))
    crud.update_robot_status(db, robot.id, "idle", None)
    return {"status": "success", "robot_id": robot.id}

@router.post("/move")
def move_item(request: schemas.MoveRequest, db: Session = Depends(get_db)):
    robot = crud.get_idle_robot(db)
    if not robot:
        raise HTTPException(status_code=400, detail="No idle robot available")
    product = crud.get_product(db, request.product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    # Simulate move
    crud.update_robot_status(db, robot.id, "active", f"Moving product {product.id}")
    crud.update_product_location(db, product.id, *request.destination, "in_transit")
    crud.create_task_history(db, schemas.TaskHistoryBase(
        operation="move", product_id=product.id, robot_id=robot.id, details=f"{request.source} -> {request.destination}"
    ))
    crud.update_product_location(db, product.id, *request.destination, "stored")
    crud.update_robot_status(db, robot.id, "idle", None)
    return {"status": "success", "robot_id": robot.id}

@router.post("/view")
def view_item(request: schemas.ViewRequest, db: Session = Depends(get_db)):
    if request.product_id:
        product = crud.get_product(db, request.product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return product
    elif request.location:
        product = crud.get_product_by_location(db, *request.location)
        if not product:
            return {"message": "No product at this location"}
        return product
    else:
        raise HTTPException(status_code=400, detail="Provide product_id or location")

@router.get("/state")
def get_state(db: Session = Depends(get_db)):
    robots = db.query(models.Robot).all()
    products = db.query(models.Product).all()
    return {"robots": robots, "products": products}

@router.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(models.TaskHistory).order_by(models.TaskHistory.timestamp.desc()).limit(20).all()
    return tasks
