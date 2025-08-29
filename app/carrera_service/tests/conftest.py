import os
import importlib
import pytest
from fastapi.testclient import TestClient

os.environ["DATABASE_URL"] = "sqlite:///:memory:"

@pytest.fixture(scope="session")
def setup_db():
    database = importlib.import_module("carrera_service.database")
    importlib.import_module("carrera_service.models")
    database.Base.metadata.create_all(bind=database.engine)
    yield
    database.Base.metadata.drop_all(bind=database.engine)

@pytest.fixture()
def client(setup_db):
    from carrera_service.main import app
    return TestClient(app)
