from pydantic import BaseModel

class EstudianteBase(BaseModel):
    nombre: str
    email: str
    carrera_id: int

class EstudianteCreate(EstudianteBase):
    pass

class EstudianteUpdate(BaseModel):
    nombre: str | None = None
    email: str | None = None
    carrera_id: int | None = None


class EstudianteRead(BaseModel):
    id: int
    nombre: str
    email: str
    carrera_id: int

class Config:
    orm_mode = True
