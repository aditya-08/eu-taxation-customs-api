from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=BG&tinNumber=7501010010")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=BG&tinNumber=7501010011")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == False

def test_get_3():
    response = client.get("/tin/validate?countryCode=BG&tinNumber=750101001")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_4():
    response = client.get("/tin/validate?countryCode=BG&tinNumber=750101001A")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_5():
    response = client.get("/tin/validate?countryCode=BG&tinNumber=7513010010")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_6():
    response = client.get("/tin/validate?countryCode=BG&tinNumber=7501320010")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False