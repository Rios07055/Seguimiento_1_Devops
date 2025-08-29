from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Any

from . import schemas, crud
from .database import engine, Base, get_db

from fastapi import APIRouter

router = APIRouter()

Base.metadata.create_all(bind=engine)

@router.get("/", response_model=list[schemas.FacultadRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)

@router.post("/", response_model=schemas.FacultadRead, status_code=201)
def create_item(item: schemas.FacultadCreate, db: Session = Depends(get_db)):
    return crud.create(db, item)

@router.get("/{item_id}", response_model=schemas.FacultadRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item

@router.put("/{item_id}", response_model=schemas.FacultadRead)
def update_item(item_id: int, item: schemas.FacultadUpdate, db: Session = Depends(get_db)):
    db_item = crud.update(db, item_id, item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item

@router.patch("/{item_id}", response_model=schemas.FacultadRead)
def patch_facultad(item_id: int, item: schemas.FacultadUpdate, db: Session = Depends(get_db)):
    update_data = item.dict(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields provided for update")
    db_obj = crud.patch_facultad(db, item_id, update_data)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Facultad not found")
    return db_obj

@router.delete("/{item_id}", response_model=schemas.FacultadRead)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item
