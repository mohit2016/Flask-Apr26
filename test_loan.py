import pytest
from loan import app


@pytest.fixture
def client():
    return app.test_client()


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.text == "<h1>Welcome to the Loan API V2!</h1>"


def test_predict_million(client):
    data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 10000000,
        "Credit_History": 1
    }
    resp = client.post("/predict", json=data)
    assert resp.status_code == 200
    assert resp.json['loan_approval_status'] == "Rejected"

def test_predict_low_amt(client):
    data = {
        "Gender": "Male",
        "Married": "No",
        "ApplicantIncome": 5000,
        "LoanAmount": 100,
        "Credit_History": 1
    }
    resp = client.post("/predict", json=data)
    assert resp.status_code == 200
    assert resp.json['loan_approval_status'] == "Approved"




# def test_loan_calculation():
#     response = requests.post("http://localhost:5000/predict", json={})
