FROM node:18.20.2-alpine

WORKDIR frontend

COPY ./frontend/package.json ./frontend/package-lock.json ./

RUN npm install --only prod --loglevel verbose

COPY ./frontend .

RUN npm run build

EXPOSE 3000

RUN npm install -g serve --loglevel verbose

CMD ["serve", "-s", "build"]
