# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /innowise
COPY requirements.txt /innowise/
RUN pip install -r requirements.txt
COPY . /innowise/