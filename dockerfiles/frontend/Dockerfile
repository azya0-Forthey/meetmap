FROM node:22.11-slim

WORKDIR frontend

COPY ./frontend/package.json package.json

RUN yarn --only=prod --loglevel verbose

COPY ./frontend .

RUN npm run build

EXPOSE 3000

RUN npm install -g serve --loglevel verbose

CMD ["serve", "-s", "build"]
