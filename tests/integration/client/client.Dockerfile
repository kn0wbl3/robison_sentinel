FROM artprod.dev.bloomberg.com/rhel7-minimal:latest

WORKDIR /workarea

COPY /tests/integration/client /config/set_envvars.sh main.py ./

RUN source ./set_envvars.sh
RUN chmod +x client.sh