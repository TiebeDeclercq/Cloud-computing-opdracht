# Controller Gateway

Containergebaseerde edge-gateway die sensordata ontvangt via MQTT, verwerkt in Node-RED, opslaat in InfluxDB en beheerd wordt via Portainer.
## Architectuur
- **Controller (Python)**: Simuleert joystick en button data
- **MQTT Broker (Mosquitto)**: Ontvangt en distribueert sensordata
- **Node-RED**: Valideert en verwerkt data met custom function nodes
- **InfluxDB**: Tijdreeksdatabase met voorgeïnstalleerd dashboard
- **Portainer**: Container management interface
## Services
- MQTT: intern netwerk (port 1883)
- Node-RED: http://localhost:1880
- InfluxDB: http://localhost:8086
- Portainer: http://localhost:9000
## Installatie
```bash
git clone https://github.com/TiebeDeclercq/Cloud-computing-opdracht
cd Cloud-computing-opdracht
docker compose up
```

**Eerste keer opstarten:**
- InfluxDB: login met admin / admin123
- Portainer: login met admin / admin1234567
## Node-RED Dataverwerking
Twee MQTT topics worden uitgelezen:
- `joystick`: x/y waarden (-1 tot 1)
- `buttons`: A/B/X/Y knoppen (0 of 1)

Function nodes valideren:
- JSON formaat controle
- Waardebereik validatie (joystick: -1 tot 1, buttons: 0/1)
- Filtering van ongeldige data

Enkel geldige metingen worden naar InfluxDB geschreven.
## InfluxDB Dashboard
Toont automatisch:
- Live joystick X/Y waarden
- Live button status (A/B/X/Y)
- Gemiddelde over 1 uur (joystick & buttons)
- Gemiddelde over 24 uur (joystick & buttons)

Dashboard wordt automatisch geïmporteerd bij eerste start.
## CI/CD
### GitHub Actions
Push naar `main` branch triggert automatisch:
- Build van alle custom images
- Push naar GitHub Container Registry
- Deploy test via docker-compose
## Docker Compose
Alle services draaien in een geïsoleerd `internal_network`. Alleen InfluxDB, Portainer en NodeRed zijn extern toegankelijk voor UI access.

Volumes:
- `mosquitto_data` & `mosquitto_log`
- `influxdb_data`
- `portainer_data`
## Monitoring
Portainer toont real-time:
- Container status
- Resource gebruik
- Logs van alle services
## Ontwikkeld
Deze volledige containergebaseerde edge-infrastructuur werd ontwikkeld door Jarno Verbeke en Tiebe Declercq voor het opleidingsonderdeel Cloud Computing.
### Jarno Verbeke
- Initiele basis project opzetten
- Mosquitto
- Python simulator voor de controller
- CI/CD met github actions
### Tiebe Declercq
- Repo opzetten / Readme
- Node Red
- InfluxDB dashboard
