from paho.mqtt import client as mqtt_client
import random
import time
import os

BROKER = os.getenv("MQTT_BROKER", "localhost")
PORT = int(os.getenv("MQTT_PORT", 1883))
CLIENT_ID = f"joystick-simulator--{random.randint(0, 1000)}"

JOYSTICK_TOPIC = "joystick"
BUTTONS_TOPIC = "buttons"

def on_connect(client, userdata, flags, rc, properties=None):
	if rc == 0:
		print("Connected")
	else:
		print(f"Connect failed: {rc}")

def on_disconnect(client, userdata, rc):
	print(f"Disconnected (rc={rc})")

def connect_with_retries(client, broker, port, max_wait=30):
	attempt = 0
	while True:
		try:
			client.connect(broker, port)
			return
		except ConnectionRefusedError:
			attempt += 1
			wait = 5
			print(f"Connection refused, retrying in {wait}s (attempt {attempt})")
			time.sleep(wait)
		except Exception as e:
			attempt += 1
			wait = 5
			print(f"Connect error: {e!r}, retrying in {wait}s (attempt {attempt})")
			time.sleep(wait)

def main():
	client = mqtt_client.Client(client_id=CLIENT_ID)
	client.on_connect = on_connect
	client.on_disconnect = on_disconnect

	try:
		# Try to connect and keep retrying if the broker is not available
		connect_with_retries(client, BROKER, PORT)
		client.loop_start()
		while True:
			x = round(random.uniform(-1.0, 1.0), 2)
			y = round(random.uniform(-1.0, 1.0), 2)
			buttons = {"A": random.choice([0,1]), "B": random.choice([0,1]), "Y": random.choice([0,1]), "X": random.choice([0,1])}

			client.publish(JOYSTICK_TOPIC, f'{{"x":{x},"y":{y}}}')
			client.publish(BUTTONS_TOPIC, f'{{"A":{buttons["A"]},"B":{buttons["B"]},"Y":{buttons["Y"]},"X":{buttons["X"]}}}')

			time.sleep(0.5)

	except KeyboardInterrupt:
		print("Stopping...")
		try:
			client.loop_stop()
			client.disconnect()
		except Exception:
			pass

if __name__ == "__main__":
	main()
