from pydantic import BaseModel

class CarreraBase(BaseModel):
    nombre: str
    facultad_id: int

class CarreraCreate(CarreraBase):
    pass

class CarreraUpdate(BaseModel):
    nombre: str | None = None
    facultad_id: int | None = None


class CarreraRead(BaseModel):
    id: int
    nombre: str
    facultad_id: int

class Config:
    orm_mode = True
