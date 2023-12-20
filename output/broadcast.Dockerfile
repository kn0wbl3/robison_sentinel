FROM artprod.dev.bloomberg.com/dpkg-python-development-base:3.11

WORKDIR /workarea

COPY /output/ .

EXPOSE 5001

RUN chmod +x broadcast.sh
