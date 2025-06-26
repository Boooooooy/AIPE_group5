FROM python:3.12-slim

RUN pip install --no-cache-dir flask mysql-connector-python pandas

WORKDIR /app

COPY app /app

CMD ["python", "app.py"]