from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=MT&tinNumber=199Z")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=MT&tinNumber=34581M")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_3():
    response = client.get("/tin/validate?countryCode=MT&tinNumber=223456789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_4():
    response = client.get("/tin/validate?countryCode=MT&tinNumber=233456789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False