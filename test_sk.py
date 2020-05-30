from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_1():
    response = client.get("/tin/validate?countryCode=SK&tinNumber=7711167420")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=SK&tinNumber=281203054")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
