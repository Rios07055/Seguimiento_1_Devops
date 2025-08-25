from facultad_service import crud, schemas
from facultad_service.database import SessionLocal

def test_create_and_get_facultad(setup_db):
    db = SessionLocal()
    f_in = schemas.FacultadCreate(nombre="Facultad de Ciencias")
    created = crud.create(db, f_in)
    assert created.id is not None
    assert created.nombre == "Facultad de Ciencias"

    fetched = crud.get(db, created.id)
    assert fetched is not None
    assert fetched.nombre == "Facultad de Ciencias"
    db.close()

def test_update_and_delete(setup_db):
    db = SessionLocal()
    f_in = schemas.FacultadCreate(nombre="Facultad X")
    created = crud.create(db, f_in)

    upd = schemas.FacultadUpdate(nombre="Facultad X Mod")
    updated = crud.update(db, created.id, upd)
    assert updated.nombre == "Facultad X Mod"

    deleted = crud.delete(db, created.id)
    assert deleted.id == created.id
    assert crud.get(db, created.id) is None
    db.close()
