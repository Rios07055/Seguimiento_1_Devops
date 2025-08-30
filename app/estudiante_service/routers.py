from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from .database import engine, Base, get_db

from fastapi import APIRouter

router = APIRouter()




Base.metadata.create_all(bind=engine)

@router.get("/", response_model=list[schemas.EstudianteRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.EstudianteRead, status_code=201)
def create_item(item: schemas.EstudianteCreate, db: Session = Depends(get_db)):
    return crud.create(db, item)

@router.get("/{item_id}", response_model=schemas.EstudianteRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.EstudianteRead)
def update_item(item_id: int, item: schemas.EstudianteUpdate, db: Session = Depends(get_db)):
    db_item = crud.update(db, item_id, item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item

@router.patch("/{item_id}", response_model=schemas.EstudianteRead)
def patch_estudiante(item_id: int, item: schemas.EstudianteUpdate, db: Session = Depends(get_db)):
    update_data = item.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    db_obj = crud.patch_estudiante(db, item_id, update_data)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Estudiante not found")
    return db_obj

@router.delete("/{item_id}", response_model=schemas.EstudianteRead)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item
