from facultad_service import crud, schemas, models
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

def test__get_pk_name_returns_pk_name():
    pk = crud._get_pk_name(models.Facultad)
    assert isinstance(pk, str)
    assert pk in ("id",)

def test_patch_facultad_updates_fields_and_skips_none(setup_db):
    db = SessionLocal()
    created = crud.create(db, schemas.FacultadCreate(nombre="Orig"))


    patch_data = {"nombre": "Parcheado", "no_existe": "x", "descripcion": None}
    updated = crud.patch_facultad(db, created.id, patch_data)


    assert updated is not None
    assert updated.nombre == "Parcheado"
    assert getattr(updated, "descripcion", None) is None
    assert not hasattr(updated, "no_existe")
    db.close()




def test_patch_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    res = crud.patch_facultad(db, 999999, {"nombre": "Nada"})
    assert res is None
    db.close()




def test_update_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    upd = schemas.FacultadUpdate(nombre="No Existe")
    res = crud.update(db, 999999, upd)
    assert res is None
    db.close()


def test_delete_nonexistent_returns_none(setup_db):
    db = SessionLocal()
    res = crud.delete(db, 999999)
    assert res is None
    db.close()