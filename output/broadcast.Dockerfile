FROM artprod.dev.bloomberg.com/dpkg-python-development-base:3.11

WORKDIR /workarea

COPY /output/ .

EXPOSE 5000

RUN chmod +x broadcast.sh

RUN python3.11 -m pip install -r broadcast_requirements.txt
