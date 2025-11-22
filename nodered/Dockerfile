# syntax=docker/dockerfile:1.4   # Use Docker BuildKit features

FROM nodered/node-red:latest

USER root

COPY data/flows.json /data/flows.json
COPY data/settings.js /data/settings.js
COPY data/flows_cred.json /data/flows_cred.json

# 1. --mount=type=secret,id=credsecret: Dit maakt een tijdelijke mount point voor een Docker secret met de ID 'credsecret'.
# 2. sed -i "s|credentialSecret:.*|credentialSecret: \"$(cat /run/secrets/credsecret)\",|" /data/settings.js:
#    Deze opdracht zoekt in het bestand /data/settings.js naar de regel die begint met 'credentialSecret:'
#    en vervangt deze door een nieuwe regel die de waarde van de secret bevat.
RUN --mount=type=secret,id=credsecret \
    sed -i "s|credentialSecret:.*|credentialSecret: \"$(cat /run/secrets/credsecret)\",|" /data/settings.js

RUN npm install --omit=dev --unsafe-perm node-red-contrib-influxdb@~0.7.0 && \
    chown -R node-red:node-red /data

USER node-red
