FROM python:3.8-slim

WORKDIR /app
ADD . /app/
RUN apt-get update && apt-get install -y nmap
RUN pip install pipenv && pipenv install