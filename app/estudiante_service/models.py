from sqlalchemy import Column, Integer, String
from .database import Base

class Estudiante(Base):
    __tablename__ = "estudiante"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    carrera_id = Column(Integer, nullable=True)
