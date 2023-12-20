FROM alpine:3.14

WORKDIR /workarea

COPY /input /config ./

RUN apt-get update && apt-get install python3

RUN chmod +x client.sh
