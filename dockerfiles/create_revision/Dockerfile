FROM python:3.13-slim

LABEL authors="Forthey"

WORKDIR /server

COPY server/requirements.txt /server/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /server/requirements.txt

COPY db.yaml /

RUN alembic init source/database/migrations | echo "Alembic initialized, skipping"

COPY server/alembic.ini /server/

COPY server/source/database/migrations /server/source/database/migrations

COPY server /server

WORKDIR /server/source
# CMD while true; do echo "hello"; sleep 2; done
CMD alembic -c ../alembic.ini revision --autogenerate