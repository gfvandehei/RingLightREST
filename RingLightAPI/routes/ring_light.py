from flask import Blueprint, request, current_app
from RingLightAPI.services.light_store import LightStore
import logging
import json

log = logging.getLogger(__name__)

ring_bp = Blueprint('ringlight', __name__)

@ring_bp.route('/', methods=["GET"])
def get_lights():
    light_store: LightStore = current_app.config.get("lightstore")
    lights = light_store.get_lights_type('ring')

    response = []
    for i in lights:
        resp_i = {
            "name": i.name,
            "type": i.type_id,
            "address": i.address
        }
        response.append(resp_i)
    log.debug(f"Response {response}")
    return json.dumps(response)

@ring_bp.route("/set_color", methods=["POST"])
def set_color():
    body = request.json

    try:
        light_id = body["light_id"]
        r = body['r']
        g = body['g']
        b = body['b']
        brightness = body['brightness']

        light_store = current_app.config.get("lightstore")
        print(light_store)
        light = light_store.get_light(light_id)
        light.set_color(r, g, b, brightness)
        return {"status": "OK"}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}

@ring_bp.route("/set_frame", methods=["POST"])
def set_frame():
    body = request.json

    try:
        light_id = body["light_id"]
        brightness = body['brightness']
        frame = body['frame']

        light_store = current_app.config.get("lightstore")
        print(light_store)
        light = light_store.get_light(light_id)
        light.set_frame(frame, brightness)
        print("OK")
        return {"status": "OK"}
    except Exception as e:
        print(e)
        return {"status": "ERROR", "message": str(e)}
