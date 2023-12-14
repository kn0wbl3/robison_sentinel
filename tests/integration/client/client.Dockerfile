FROM artprod.dev.bloomberg.com/rhel7-minimal:latest

WORKDIR /workarea

COPY /tests/docker/client /config/set_envvars.sh ./

RUN source ./set_envvars.sh
RUN chmod +x client.sh