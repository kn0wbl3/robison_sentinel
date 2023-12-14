FROM artprod.dev.bloomberg.com/dpkg-python-development-base:3.11

WORKDIR /workarea

COPY /tests/docker/server .

EXPOSE 5000

RUN chmod +x server.sh

RUN python3.11 -m pip install -r requirements.txt
