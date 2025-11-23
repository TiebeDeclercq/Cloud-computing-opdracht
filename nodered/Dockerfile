# syntax=docker/dockerfile:1.4   # Use Docker BuildKit features

FROM nodered/node-red:latest

USER root

COPY data/flows.json /data/flows.json
COPY data/settings.js /data/settings.js
COPY data/flows_cred.json /data/flows_cred.json

ARG NODERED_SECRET

RUN sed -i "s|credentialSecret:.*|credentialSecret: \"${NODERED_SECRET}\",|" /data/settings.js

RUN npm install --omit=dev --unsafe-perm node-red-contrib-influxdb@~0.7.0 && \
    chown -R node-red:node-red /data

USER node-red
