def test_full_crud_flow(client):
    # crear
    resp = client.post("/", json={"nombre": "Arquitectura", "facultad_id": None})
    assert resp.status_code == 201
    data = resp.json()
    assert data["nombre"] == "Arquitectura"
    item_id = data["id"]

    # obtener
    r2 = client.get(f"/{item_id}")
    assert r2.status_code == 200
    assert r2.json()["nombre"] == "Arquitectura"

    # actualizar
    r3 = client.put(f"/{item_id}", json={"nombre": "Arquitectura U"})
    assert r3.status_code == 200
    assert r3.json()["nombre"] == "Arquitectura U"

    # borrar
    r4 = client.delete(f"/{item_id}")
    assert r4.status_code == 200

    # verificar 404
    r5 = client.get(f"/{item_id}")
    assert r5.status_code == 404
