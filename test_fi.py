from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=FI&tinNumber=131052-308T")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=FI&tinNumber=131052B308T")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_3():
    response = client.get("/tin/validate?countryCode=FI&tinNumber=131052-308A")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == False

def test_get_4():
    response = client.get("/tin/validate?countryCode=FI&tinNumber=31052-308T")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False
    