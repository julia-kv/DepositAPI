# Тестовое задание 

Сервис REST API  для расчета депозита cо сложным процентом

### Установка и запуск в docker 

```bash
docker build -t docker-api .
docker run -p 8080:8080 deposit-api:latest
```

### Создание виртуального окружения и запуск тестов

Покрытие кода тестами: 97 %

```bash
python3 -m venv venv
. venv/bin/activate
pip install -U pip setuptools
pip install -e . -r requirements/test.txt

pytest --cov=deposit_api tests/
```
    
