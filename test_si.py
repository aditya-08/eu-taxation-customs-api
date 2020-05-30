from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_1():
    response = client.get("/tin/validate?countryCode=SI&tinNumber=15012557")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=SI&tinNumber=15012556")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_3():
    response = client.get("/tin/validate?countryCode=SI&tinNumber=5012556")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_4():
    response = client.get("/tin/validate?countryCode=SI&tinNumber=15012556555")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True