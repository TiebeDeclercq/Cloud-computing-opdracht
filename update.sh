#!/bin/bash
docker-compose build
docker-compose down
docker-compose up -d
echo "Updated!"
```

Maak executable: `chmod +x deploy.sh update.sh`

## 2. `.env` file voor secrets

`.env`:
```
INFLUXDB_PASSWORD=yourpassword
INFLUXDB_TOKEN=yoursupersecrettoken