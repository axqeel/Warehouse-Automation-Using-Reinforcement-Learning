from pydantic import BaseModel
from typing import Optional, Tuple
from datetime import datetime

class ProductBase(BaseModel):
    name: str
    x: int
    y: int
    z: int
    status: str

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int
    class Config:
        orm_mode = True

class RobotBase(BaseModel):
    x: int
    y: int
    z: int
    status: str
    current_task: Optional[str]

class Robot(RobotBase):
    id: int
    class Config:
        orm_mode = True

class TaskHistoryBase(BaseModel):
    operation: str
    product_id: int
    robot_id: int
    details: Optional[str]

class TaskHistory(TaskHistoryBase):
    id: int
    timestamp: datetime
    class Config:
        orm_mode = True

# For API requests
class CollectRequest(BaseModel):
    product_id: int
    target: Tuple[int, int, int]

class DepositRequest(BaseModel):
    product_id: int
    destination: Tuple[int, int, int]

class MoveRequest(BaseModel):
    product_id: int
    source: Tuple[int, int, int]
    destination: Tuple[int, int, int]

class ViewRequest(BaseModel):
    product_id: Optional[int]
    location: Optional[Tuple[int, int, int]]
