from flask import Blueprint, request
from RingLightAPI.containers.basecontainer import BaseContainer
import logging
import json

log = logging.getLogger(__name__)

ring_bp = Blueprint('ringlight', __name__)

@ring_bp.route('/', methods=["GET"])
def get_lights():
    light_store = BaseContainer.light_store()
    lights = light_store.get_lights()

    response = []
    for i in lights:
        resp_i = {
            "name": i.name,
            "type": i.type,
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

        light_store = BaseContainer.light_store()
        print(light_store)
        light = light_store.get_light(light_id)
        light.set_strip_color(r, g, b, brightness)
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

        light_store = BaseContainer.light_store()
        print(light_store)
        light = light_store.get_light(light_id)
        light.set_entire_frame(frame, brightness)
        return {"status": "OK"}
    except Exception as e:
        return {"status": "ERROR", "message": str(e)}
