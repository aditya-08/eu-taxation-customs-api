from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_1():
    response = client.get("/tin/validate?countryCode=ES&tinNumber=54237A")
    assert response.status_code == 200

def test_get_2():
    response = client.get("/tin/validate?countryCode=ES&tinNumber=X1234567L")
    assert response.status_code == 200

def test_get_3():
    response = client.get("/tin/validate?countryCode=ES&tinNumber=Z123456AR")
    assert response.status_code == 200

def test_get_4():
    response = client.get("/tin/validate?countryCode=ES&tinNumber=Z12345A7R")
    assert response.status_code == 200

def test_get_5():
    response = client.get("/tin/validate?countryCode=ES&tinNumber=Z1234A67R")
    assert response.status_code == 200

def test_get_checkDigitFail():
    response = client.get("/tin/validate?countryCode=ES&tinNumber=X1234567A")
    assert response.status_code == 200
    assert response.json() == {"tinNumber": "X1234567A", "validStructure": True, "validSyntax": False, "message": "Check Digit - failed", "countryCode": "ES"}
