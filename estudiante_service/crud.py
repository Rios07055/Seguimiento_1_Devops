from . import models, schemas
from sqlalchemy.orm import Session

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Estudiante).offset(skip).limit(limit).all()

def get(db: Session, item_id: int):
    return db.query(models.Estudiante).filter(models.Estudiante.id == item_id).first()

def create(db: Session, item: schemas.EstudianteCreate):
    db_item = models.Estudiante(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update(db: Session, item_id: int, item: schemas.EstudianteUpdate):
    db_item = get(db, item_id)
    if not db_item:
        return None
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def delete(db: Session, item_id: int):
    db_item = get(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item
