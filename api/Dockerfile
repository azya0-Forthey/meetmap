FROM golang:1.23.1

WORKDIR api

COPY go.mod go.sum ./

RUN go mod download

COPY . .

WORKDIR source

RUN ls

RUN go build -o ./run
