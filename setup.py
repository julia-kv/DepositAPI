#!/usr/bin/env python

from distutils.core import setup

requirements = ["fastapi", "uvicorn", "pandas"]

setup(
    name="deposit_api",
    version="1.0",
    description="Deposit calculating",
    author="Korpusova Julia",
    author_email="gward@python.net",
    # url='https://www.python.org/sigs/distutils-sig/',
    packages=["deposit_api"],
    install_requires=requirements,
    entry_points={"console_scripts": ["deposits = deposit_api.app:app"]},
)
