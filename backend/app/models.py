from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .database import Base
import enum
from datetime import datetime

class ProductStatus(str, enum.Enum):
    in_transit = "in_transit"
    stored = "stored"

class RobotStatus(str, enum.Enum):
    idle = "idle"
    active = "active"

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
    status = Column(Enum(ProductStatus), default=ProductStatus.stored)

class Robot(Base):
    __tablename__ = "robots"
    id = Column(Integer, primary_key=True, index=True)
    x = Column(Integer)
    y = Column(Integer)
    z = Column(Integer)
    status = Column(Enum(RobotStatus), default=RobotStatus.idle)
    current_task = Column(String, nullable=True)

class TaskHistory(Base):
    __tablename__ = "task_history"
    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String)
    product_id = Column(Integer, ForeignKey("products.id"))
    robot_id = Column(Integer, ForeignKey("robots.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)
    details = Column(String)
