from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=IE&tinNumber=1234567TW")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=IE&tinNumber=1234567T")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_3():
    response = client.get("/tin/validate?countryCode=IE&tinNumber=1234577W")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_4():
    response = client.get("/tin/validate?countryCode=IE&tinNumber=1234577WW")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_5():
    response = client.get("/tin/validate?countryCode=IE&tinNumber=1234577IA")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_6():
    response = client.get("/tin/validate?countryCode=IE&tinNumber=34577IA")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_7():
    response = client.get("/tin/validate?countryCode=IE&tinNumber=1234577IB")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == False
    