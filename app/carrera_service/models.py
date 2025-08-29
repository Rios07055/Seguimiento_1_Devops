from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base

class Carrera(Base):
    __tablename__ = "carrera"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    facultad_id = Column(Integer, nullable=True)
