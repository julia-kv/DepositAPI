import pandas as pd
from pydantic import BaseModel, validator

FORMAT = "%d.%m.%Y"


class Data(BaseModel):
    """ " """

    date: str
    periods: int
    amount: int
    rate: float

    @validator("date")
    def date_validator(cls, v):
        try:
            pd.to_datetime(v, format=FORMAT)
        except ValueError:
            raise ValueError(f"wrong date format {v} does not match {FORMAT}")
        return v

    @validator("periods")
    def periods_validator(cls, v):
        if v < 1 or v > 60:
            raise ValueError("wrong number of periods")
        return v

    @validator("amount")
    def amount_validator(cls, v):
        if v < 10_000 or v > 3_000_000:
            raise ValueError("wrong deposit amount")
        return v

    @validator("rate")
    def rate_validator(cls, v):
        if v < 1.0 or v > 8.0:
            raise ValueError("wrong deposit rate")
        return v
