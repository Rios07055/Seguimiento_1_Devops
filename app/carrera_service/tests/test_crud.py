from carrera_service import crud, schemas, models
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


def test__get_pk_name_returns_pk_name():
    pk = crud._get_pk_name(models.Carrera)
    assert isinstance(pk, str)
    assert pk in ("id",)

def test_get_all_pagination(setup_db):
    db = SessionLocal()
    c1 = crud.create(db, schemas.CarreraCreate(nombre="Carrera A", facultad_id=None))
    c2 = crud.create(db, schemas.CarreraCreate(nombre="Carrera B", facultad_id=None))
    c3 = crud.create(db, schemas.CarreraCreate(nombre="Carrera C", facultad_id=None))

    all_items = crud.get_all(db, skip=0, limit=10)
    assert len(all_items) >= 3

    page = crud.get_all(db, skip=1, limit=2)
    assert isinstance(page, list)
    assert len(page) <= 2
    if len(all_items) >= 3:
        assert page[0].nombre in ("Carrera B", "Carrera C", "Carrera A")

    db.close()

def test_patch_carrera_updates_fields_and_skips_none(setup_db):
    db = SessionLocal()
    created = crud.create(db, schemas.CarreraCreate(nombre="Original", facultad_id=None))

    patch_data = {"nombre": "Parcheado", "facultad_id": None, "no_existe": "x"}
    updated = crud.patch_carrera(db, created.id, patch_data)

    assert updated is not None
    assert updated.nombre == "Parcheado"
    assert getattr(updated, "facultad_id", None) is None

    assert not hasattr(updated, "no_existe")

    db.close()

def test_patch_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    res = crud.patch_carrera(db, 999999, {"nombre": "Nada"})
    assert res is None
    db.close()

def test_update_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    upd = schemas.CarreraUpdate(nombre="No Existe")
    res = crud.update(db, 999999, upd)
    assert res is None
    db.close()

def test_delete_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    res = crud.delete(db, 999999)
    assert res is None
    db.close()
