import requests
import time

frame = [[255,0,0]]*36

while True:
    for i in range(36):
        frame[i] = [255,255,0]
        requests.post("http://localhost:5000/ringlights/set_frame", json={
            "light_id": "RING1",
            "brightness": 255,
            "frame": frame
        })
        time.sleep(.1)
    for i in range(36):
        frame[i] = [255,0,255]
        requests.post("http://localhost:5000/ringlights/set_frame", json={
            "light_id": "RING1",
            "brightness": 255,
            "frame": frame
        })
        time.sleep(.1)