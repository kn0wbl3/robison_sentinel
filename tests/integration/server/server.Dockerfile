FROM python:3

WORKDIR /workarea

COPY /tests/integration/server .

EXPOSE 5000

RUN chmod +x server.sh
