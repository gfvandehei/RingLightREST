from paho.mqtt.client import Client
import json
import time


client = Client()
client.connect('192.168.1.19', 1883)

message_object = {
    "message_type": "identification",
    "type": "ring_light",
    "id": 123456,
    "name": "fakelight"
}
message_str = json.dumps(message_object)

while True:
    print("Here")
    client.publish("home/lighting", message_str)
    time.sleep(1)