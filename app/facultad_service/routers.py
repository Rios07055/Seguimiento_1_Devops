from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
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

@router.delete("/{item_id}", response_model=schemas.FacultadRead)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item
