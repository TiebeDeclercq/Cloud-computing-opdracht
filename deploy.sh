#!/bin/bash
docker-compose down
docker-compose build
docker-compose up -d
echo "Deployed! Check http://localhost:9000 (Portainer)"