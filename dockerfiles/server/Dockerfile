FROM python:3.13-slim

LABEL authors="azya0 && Forthey"

WORKDIR /server

COPY server/requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY server /server

WORKDIR /server/source
