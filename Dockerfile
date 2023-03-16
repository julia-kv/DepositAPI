FROM python:3.8.13-slim-buster

COPY setup.py /setup.py

RUN pip install .

COPY deposit_api /deposit_api

WORKDIR /deposit_api

EXPOSE 8080

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]