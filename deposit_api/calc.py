from typing import List, Dict

import pandas as pd

from deposit_api.request_data import Data, FORMAT


def gen_values(periods: int, amount: int, rate: float, freq: int = 12) -> List[float]:
    """
    Compounding rate
    Generates a list of deposit values  for every next month
    """
    return [
        round(amount * pow(1 + rate / 100 / freq, i), 2) for i in range(1, periods + 1)
    ]


def gen_dates(first_date: str, periods: int) -> List[str]:
    """
    Generates a list of dates for every next month
    """
    date_list = []

    first_date = pd.to_datetime(first_date, format=FORMAT)

    first_date_month = first_date + pd.offsets.MonthEnd(0) - pd.offsets.MonthBegin()
    delta = first_date.day

    for i in range(periods):
        first_date_month += pd.DateOffset(months=1)
        cur_delta = min(delta, first_date_month.days_in_month)
        cur_date = first_date_month + pd.DateOffset(days=cur_delta - 1)
        date_list.append(cur_date.strftime(FORMAT))

    return date_list


def deposit(data: Data) -> Dict[str, float]:
    """
    Calculates pairs of dates and deposit values
    """

    final_values = gen_values(data.periods, data.amount, data.rate)
    dates = gen_dates(data.date, data.periods)

    return dict(zip(dates, final_values))
