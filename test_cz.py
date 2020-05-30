from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=CZ&tinNumber=685229/4449")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=CZ&tinNumber=795229/0292")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_3():
    response = client.get("/tin/validate?countryCode=CZ&tinNumber=816008/0610")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_4():
    response = client.get("/tin/validate?countryCode=CZ&tinNumber=816008/061011")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    