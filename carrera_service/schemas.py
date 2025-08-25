from typing import Optional
from pydantic import BaseModel, ConfigDict

class CarreraBase(BaseModel):
    nombre: str
    facultad_id: Optional[int] = None  # ahora opcional

class CarreraCreate(CarreraBase):
    pass

class CarreraUpdate(BaseModel):
    nombre: Optional[str] = None
    facultad_id: Optional[int] = None

class CarreraRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nombre: str
    facultad_id: Optional[int] = None
