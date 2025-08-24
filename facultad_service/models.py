from sqlalchemy import Column, Integer, String
from .database import Base

class Facultad(Base):
    __tablename__ = "facultad"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
