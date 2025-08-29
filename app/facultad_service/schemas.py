from pydantic import BaseModel

class FacultadBase(BaseModel):
    nombre: str

class FacultadCreate(FacultadBase):
    pass

class FacultadUpdate(BaseModel):
    nombre: str | None = None


class FacultadRead(BaseModel):
    id: int
    nombre: str


class Config:
    orm_mode = True
