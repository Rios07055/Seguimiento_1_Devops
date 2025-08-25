from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from . import schemas, crud
from .database import engine, Base, get_db

app = FastAPI(title="Carrera service")

Base.metadata.create_all(bind=engine)

@app.get("/", response_model=list[schemas.CarreraRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all(db, skip=skip, limit=limit)

@app.post("/", response_model=schemas.CarreraRead, status_code=201)
def create_item(item: schemas.CarreraCreate, db: Session = Depends(get_db)):
    return crud.create(db, item)

@app.get("/{item_id}", response_model=schemas.CarreraRead)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.get(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item

@app.put("/{item_id}", response_model=schemas.CarreraRead)
def update_item(item_id: int, item: schemas.CarreraUpdate, db: Session = Depends(get_db)):
    db_item = crud.update(db, item_id, item)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item

@app.delete("/{item_id}", response_model=schemas.CarreraRead)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud.delete(db, item_id)
    if not db_item:
        raise HTTPException(status_code=404, detail="Not found")
    return db_item
