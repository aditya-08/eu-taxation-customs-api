from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_1():
    response = client.get("/tin/validate?countryCode=IT&tinNumber=DMLPRY77D15H501F")
    assert response.status_code == 200

def test_get_2():
    response = client.get("/tin/validate?countryCode=IT&tinNumber=1MLPRY77D15H501F")
    assert response.status_code == 200
    assert response.json()["message"] == "1st character must be a letter"

def test_get_3():
    response = client.get("/tin/validate?countryCode=IT&tinNumber=DMLPRY77D15H501A")
    assert response.status_code == 200
    assert response.json()["validSyntax"] == False
    assert response.json()["message"] == "Check Digit failed"
