from fastapi.testclient import TestClient
from pytest import mark

from deposit_api.app import app


client = TestClient(app)


@mark.parametrize(
    "dt, periods, amount, rate, expected_status, expected_json",
    [
        (
            "31.01.2000",
            7,
            10000,
            6,
            200,
            {
                "29.02.2000": 10050.0,
                "31.03.2000": 10100.25,
                "30.04.2000": 10150.75,
                "31.05.2000": 10201.51,
                "30.06.2000": 10252.51,
                "31.07.2000": 10303.78,
                "31.08.2000": 10355.29,
            },
        ),
    ],
)
def test_app(dt, periods, amount, rate, expected_status, expected_json):
    response = client.post(
        "/deposit/",
        headers={"Content-Type:": "application/json"},
        json={"date": dt, "periods": periods, "amount": amount, "rate": rate},
    )

    assert response.status_code == expected_status
    assert response.json() == expected_json


@mark.parametrize(
    "dt,expected_status, expected_error",
    [
        ("31/01/2000", 400, "wrong date format 31/01/2000 does not match %d.%m.%Y"),
    ],
)
def test_validate_date(dt, expected_status, expected_error):
    response = client.post(
        "/deposit/",
        headers={"Content-Type:": "application/json"},
        json={"date": dt, "periods": 7, "amount": 10000, "rate": 6},
    )
    assert response.status_code == expected_status
    assert response.json()["error"] == expected_error


@mark.parametrize(
    "periods, expected_status, expected_error",
    [
        (0, 400, "wrong number of periods"),
        (100, 400, "wrong number of periods"),
        ("aa", 400, "value is not a valid integer"),
    ],
)
def test_validate_periods(periods, expected_status, expected_error):
    response = client.post(
        "/deposit/",
        headers={"Content-Type:": "application/json"},
        json={"date": "31.01.2000", "periods": periods, "amount": 10000, "rate": 6},
    )
    assert response.status_code == expected_status
    assert response.json()["error"] == expected_error


@mark.parametrize(
    "amount, expected_status, expected_json",
    [
        (1_000, 400, "wrong deposit amount"),
        (5_000_000, 400, "wrong deposit amount"),
        ("aa", 400, "value is not a valid integer"),
    ],
)
def test_validate_amount(amount, expected_status, expected_json):
    response = client.post(
        "/deposit/",
        headers={"Content-Type:": "application/json"},
        json={"date": "31.01.2000", "periods": 7, "amount": amount, "rate": 6},
    )
    assert response.status_code == expected_status
    assert response.json()["error"] == expected_json


@mark.parametrize(
    "rate, expected_status, expected_json",
    [
        (0, 400, "wrong deposit rate"),
        (9, 400, "wrong deposit rate"),
        ("aa", 400, "value is not a valid float"),
    ],
)
def test_validate_amount(rate, expected_status, expected_json):
    response = client.post(
        "/deposit/",
        headers={"Content-Type:": "application/json"},
        json={"date": "31.01.2000", "periods": 7, "amount": 10000, "rate": rate},
    )
    assert response.status_code == expected_status
    assert response.json()["error"] == expected_json
