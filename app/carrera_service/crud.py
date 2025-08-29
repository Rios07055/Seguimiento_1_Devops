from . import models, schemas
from sqlalchemy.orm import Session
from typing import Dict, Any, Optional
from sqlalchemy import inspect as sqlalchemy_inspect

def _get_pk_name(model) -> str:
    pk_cols = sqlalchemy_inspect(model).primary_key
    if not pk_cols:
        raise RuntimeError("Modelo sin primary key")
    return pk_cols[0].key

def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Carrera).offset(skip).limit(limit).all()

def get(db: Session, item_id: int):
    return db.query(models.Carrera).filter_by(id=item_id).first()


def create(db: Session, item: schemas.CarreraCreate):
    db_item = models.Carrera(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update(db: Session, item_id: int, item: schemas.CarreraUpdate):
    db_item = get(db, item_id)
    if not db_item:
        return None
    for k, v in item.model_dump(exclude_unset=True).items():
        setattr(db_item, k, v)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def patch_carrera(db: Session, carrera_id: int, obj_in: Dict[str, Any]):
    return patch_item(db, models.Carrera, carrera_id, obj_in)

def delete(db: Session, item_id: int):
    db_item = get(db, item_id)
    if not db_item:
        return None
    db.delete(db_item)
    db.commit()
    return db_item

def patch_item(db: Session, model, item_id: int, obj_in: Dict[str, Any]):
    pk_name = _get_pk_name(model)
    db_obj = db.query(model).filter(getattr(model, pk_name) == item_id).first()
    if not db_obj:
        return None

    for field, value in obj_in.items():
        if value is None:
            continue
        if hasattr(db_obj, field):
            setattr(db_obj, field, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
