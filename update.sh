#!/bin/bash
docker-compose down -v
docker-compose build --pull
docker-compose up -d
echo "Updated!"