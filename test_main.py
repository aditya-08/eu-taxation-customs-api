from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == "Welcome to European Customs and Taxation API"

def test_tin_IT():
    response = client.post(
        "/tin/validate",
        json={
            "countryCode": "IT",
            "tin": "DMLPRY77D15H501F"
        }
    )
    assert response.status_code == 200

def test_tin_ES():
    response = client.post(
        "/tin/validate",
        json={
            "countryCode": "ES",
            "tin": "X1234567L",
            "foreigner": True
            }
    )
    assert response.status_code == 200
    response = client.post(
        "/tin/validate",
        json={
            "countryCode": "ES",
            "tin": "X1234567L"
            }
    )
    assert response.status_code == 200

def test_tin_ES_F():
    response = client.post(
        "/tin/validate",
        json={
            "countryCode": "ES",
            "tin": "X1234567L"
            }
    )
    assert response.status_code == 200