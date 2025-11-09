# Controller Gateway

Een containergebaseerde edge-gateway die sensordata ontvangt via MQTT, verwerkt in Node-RED, opslaat in InfluxDB en beheerd wordt via Portainer.
## Architectuur
(moet niet maar ziet er misschien mooi uit NOG AANPASSEN)
flowchart LR

    Sensor --> MQTT[MQTT Broker]

    MQTT --> NR[Node-RED]

    NR --> InfluxDB

    InfluxDB --> Dashboard[InfluxDB Dashboard]

    NR --> Debug[Debug Logging]

    Portainer --> Docker
## Installatie
1. Clone repository
2. Run: `./deploy.sh`
3. Open browsers voor configuratie
## Services
- MQTT: port 1883
- Node-RED: http://localhost:1880
- InfluxDB: http://localhost:8086
- Portainer: http://localhost:9000  
## Node-RED Flow
Node-RED ontvangt MQTT-berichten van de broker.
De flow voert de volgende stappen uit:
1. Ontvangen van MQTT-data via vooraf ingestelde topics (bv. controller/buttons en controller/joystick).
2. Controle op geldig JSON-formaat, Controle op toegestane waardes (0/1 voor knoppen, bereik −100 tot 100 voor joystick)
3. Opslag van enkel geldige metingen in InfluxDB.
4. Debug log in Node-RED voor monitoring tijdens ontwikkeling.
## InfluxDB Queries
Voorbeeld van een query die gebruikt wordt:
```
from(bucket: "controller")

  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)

  |> filter(fn: (r) => r["_measurement"] == "joystick")

  |> filter(fn: (r) => r["_field"] == "x")

  |> aggregateWindow(every: v.windowPeriod, fn: mean, createEmpty: false)

  |> yield(name: "mean")
```
## CI/CD & Automatische Deploy
De omgeving bevat een `update.sh` script om containers opnieuw op te bouwen en te deployen.
Dit script:
- bouwt de containers opnieuw
- stopt de oude stack
- start de vernieuwde versie
