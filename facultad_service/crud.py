from sqlalchemy.orm import Session
import models
import schemas

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Facultad).offset(skip).limit(limit).all()

def get(db: Session, item_id: int):
    return db.query(models.Facultad).filter(models.Facultad.id == item_id).first()

def create(db: Session, item: schemas.FacultadCreate):
    db_item = models.Facultad(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update(db: Session, item_id: int, item: schemas.FacultadUpdate):
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
