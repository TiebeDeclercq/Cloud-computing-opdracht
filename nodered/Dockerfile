FROM nodered/node-red:latest

USER root

COPY data/flows.json /data/flows.json
COPY data/settings.js /data/settings.js

ENV INFLUXDB_TOKEN=awokentoken

RUN npm install --omit=dev --unsafe-perm node-red-contrib-influxdb@~0.7.0 && \
    chown -R node-red:node-red /data

USER node-red
