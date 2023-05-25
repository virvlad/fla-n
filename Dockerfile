FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y gcc libpq-dev 

COPY ./src/create-table.py /usr/share/fla-n/create-table.py
COPY requirements.txt /usr/share/fla-n/requirements.txt

WORKDIR /usr/share/fla-n

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD gunicorn --bind 0.0.0.0:8000 create-table:app
