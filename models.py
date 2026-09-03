from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from sqlalchemy.sql import func

class Producto(Base):
    __tablename__ = 'productos'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String(50), index=True, nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, nullable=False)
    created_at = Column(DateTime, nullable=False, default=func.now())