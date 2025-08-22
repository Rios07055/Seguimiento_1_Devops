from typing import Optional
from pydantic import BaseModel, ConfigDict


class EstudianteBase(BaseModel):
    nombre: str
    email: str
    carrera_id: Optional[int] = None

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    carrera_id: Optional[int] = None

class EstudianteRead(BaseModel):
    id: int
    nombre: str
    email: str
    carrera_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)
