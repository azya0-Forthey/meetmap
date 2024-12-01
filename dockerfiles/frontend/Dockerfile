FROM node:22.11-slim

WORKDIR /frontend

COPY frontend/package.json .
COPY frontend/package-lock.json .

RUN npm install

COPY frontend /frontend

CMD npm start