#!/usr/bin/env python

from distutils.core import setup

requirements = ["fastapi", "uvicorn", "pandas"]

setup(
    name="deposit_api",
    version="1.0.1",
    description="Deposit calculation",
    author="Korpusova Julia",
    packages=["deposit_api"],
    install_requires=requirements,
    entry_points={"console_scripts": ["deposits = deposit_api.app:app"]},
)
