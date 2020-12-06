FROM python:3.8-slim

WORKDIR /app
ADD . /app/
RUN apt update && apt install -y nmap
RUN pip install pipenv && pipenv install