from deposit_api.calc import Data, deposit, gen_values, gen_dates
from pytest import mark


@mark.parametrize(
    "periods, amount, rate, expected_values_list",
    [
        (
            7,
            10000,
            6,
            [10050.0, 10100.25, 10150.75, 10201.51, 10252.51, 10303.78, 10355.29],
        ),
    ],
)
def test_get_values(periods, amount, rate, expected_values_list):
    assert gen_values(periods, amount, rate) == expected_values_list


@mark.parametrize(
    "dt, periods, expected_dates_list",
    [
        (
            "31.01.2000",
            12,
            [
                "29.02.2000",
                "31.03.2000",
                "30.04.2000",
                "31.05.2000",
                "30.06.2000",
                "31.07.2000",
                "31.08.2000",
                "30.09.2000",
                "31.10.2000",
                "30.11.2000",
                "31.12.2000",
                "31.01.2001",
            ],
        ),
    ],
)
def test_gen_dates(dt, periods, expected_dates_list):
    assert gen_dates(dt, periods) == expected_dates_list


@mark.parametrize(
    "dt, periods, amount, rate, expected_deposit",
    [
        (
            "31.01.2000",
            7,
            10000,
            6,
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
def test_deposit(dt, periods, amount, rate, expected_deposit):
    data = Data(date=dt, periods=periods, amount=amount, rate=rate)
    result = deposit(data)
    assert len(result) == periods
    assert result == expected_deposit
