from estudiante_service import crud, schemas
from estudiante_service.database import SessionLocal

def test_create_and_get_estudiante(setup_db):
    db = SessionLocal()
    est_in = schemas.EstudianteCreate(nombre="Juan", email="juan@example.com", carrera_id=None)
    created = crud.create(db, est_in)
    assert created.id is not None
    assert created.nombre == "Juan"

    fetched = crud.get(db, created.id)
    assert fetched.email == "juan@example.com"
    db.close()

def test_update_and_delete(setup_db):
    db = SessionLocal()
    est_in = schemas.EstudianteCreate(nombre="Ana", email="ana@example.com", carrera_id=None)
    created = crud.create(db, est_in)
    upd = schemas.EstudianteUpdate(nombre="Ana Maria")
    updated = crud.update(db, created.id, upd)
    assert updated.nombre == "Ana Maria"

    deleted = crud.delete(db, created.id)
    assert deleted.id == created.id
    assert crud.get(db, created.id) is None
    db.close()

