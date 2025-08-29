from carrera_service import crud, schemas
from carrera_service.database import SessionLocal

def test_create_and_get_carrera(setup_db):
    db = SessionLocal()
    c_in = schemas.CarreraCreate(nombre="Ing. Sistemas", facultad_id=None)
    created = crud.create(db, c_in)
    assert created.id is not None
    assert created.nombre == "Ing. Sistemas"

    fetched = crud.get(db, created.id)
    assert fetched is not None
    assert fetched.nombre == "Ing. Sistemas"
    db.close()

def test_update_and_delete(setup_db):
    db = SessionLocal()
    c_in = schemas.CarreraCreate(nombre="Medicina", facultad_id=None)
    created = crud.create(db, c_in)

    upd = schemas.CarreraUpdate(nombre="Medicina Veterinaria")
    updated = crud.update(db, created.id, upd)
    assert updated.nombre == "Medicina Veterinaria"

    deleted = crud.delete(db, created.id)
    assert deleted.id == created.id
    assert crud.get(db, created.id) is None
    db.close()
