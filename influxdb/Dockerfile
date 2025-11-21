FROM influxdb:2

USER root

ARG INFLUXDB_PASSWORD
ARG INFLUXDB_TOKEN

COPY controller_dashboard.json /config/controller_dashboard.json

COPY influx-init.sh /docker-entrypoint-initdb.d/influx-init.sh
RUN chmod +x /docker-entrypoint-initdb.d/influx-init.sh

ENV DOCKER_INFLUXDB_INIT_MODE=setup
ENV DOCKER_INFLUXDB_INIT_USERNAME=admin
ENV DOCKER_INFLUXDB_INIT_PASSWORD=${INFLUXDB_PASSWORD}
ENV DOCKER_INFLUXDB_INIT_ADMIN_TOKEN=${INFLUXDB_TOKEN}
ENV DOCKER_INFLUXDB_INIT_ORG=Dectronics
ENV DOCKER_INFLUXDB_INIT_BUCKET=controller
ENV DOCKER_INFLUXDB_INIT_TEMPLATE=/config/controller_dashboard.json

USER influxdb