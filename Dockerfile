FROM python:3.8-slim

WORKDIR /app
ADD . /app/
RUN pip install pipenv && pipenv install