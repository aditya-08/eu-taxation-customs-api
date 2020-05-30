from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=GR&tinNumber=123456789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=GR&tinNumber=123")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_3():
    response = client.get("/tin/validate?countryCode=GR&tinNumber=12345678A")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
 

    