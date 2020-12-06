FROM python:3.8-slim

RUN apt-get update && apt-get install -y nmap

WORKDIR /app
ADD . /app/

RUN pip install pipenv && pipenv install