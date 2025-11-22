FROM nodered/node-red:latest

USER root

COPY data/flows.json /data/flows.json
COPY data/settings.js /data/settings.js

ARG INFLUXDB_TOKEN
ENV INFLUXDB_TOKEN=${INFLUXDB_TOKEN}

RUN npm install --omit=dev --unsafe-perm node-red-contrib-influxdb@~0.7.0 && \
    chown -R node-red:node-red /data

USER node-red
