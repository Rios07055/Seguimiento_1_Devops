from estudiante_service import crud, schemas, models
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

def test__get_pk_name_returns_pk_name():
    pk = crud._get_pk_name(models.Estudiante)
    assert isinstance(pk, str)
    assert pk in ("id",)


def test_get_all_pagination(setup_db):
    db = SessionLocal()
    s1 = crud.create(db, schemas.EstudianteCreate(nombre="S1", email="s1@example.com", carrera_id=None))
    s2 = crud.create(db, schemas.EstudianteCreate(nombre="S2", email="s2@example.com", carrera_id=None))
    s3 = crud.create(db, schemas.EstudianteCreate(nombre="S3", email="s3@example.com", carrera_id=None))

    all_items = crud.get_all(db, skip=0, limit=10)
    assert len(all_items) >= 3

    page = crud.get_all(db, skip=1, limit=2)
    assert isinstance(page, list)
    assert len(page) <= 2
    db.close()


def test_patch_estudiante_updates_fields_and_skips_none(setup_db):
    db = SessionLocal()
    created = crud.create(db, schemas.EstudianteCreate(nombre="Orig", email="orig@example.com", carrera_id=None))

    patch_data = {"nombre": "Parcheado", "carrera_id": None, "no_existe": "x"}
    updated = crud.patch_estudiante(db, created.id, patch_data)

    assert updated is not None
    assert updated.nombre == "Parcheado"
    assert getattr(updated, "carrera_id", None) is None
    assert not hasattr(updated, "no_existe")
    db.close()


def test_patch_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    res = crud.patch_estudiante(db, 999999, {"nombre": "Nada"})
    assert res is None
    db.close()


def test_update_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    upd = schemas.EstudianteUpdate(nombre="No Existe")
    res = crud.update(db, 999999, upd)
    assert res is None
    db.close()


def test_delete_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    res = crud.delete(db, 999999)
    assert res is None
    db.close()