from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    category = Column(String)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
    last_updated = Column(DateTime, default=datetime.utcnow)