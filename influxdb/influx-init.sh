#!/bin/bash
set -e
influx apply -f $DOCKER_INFLUXDB_INIT_TEMPLATE -o $DOCKER_INFLUXDB_INIT_ORG -t $DOCKER_INFLUXDB_INIT_ADMIN_TOKEN --force yes
echo ">> Dashboard template applied."