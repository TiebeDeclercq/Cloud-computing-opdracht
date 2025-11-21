FROM eclipse-mosquitto:latest

USER root

COPY config/mosquitto.conf /mosquitto/config/mosquitto.conf

RUN chown -R mosquitto:mosquitto /mosquitto/config/mosquitto.conf

USER mosquitto