from flask import Blueprint, request, current_app
import logging
import json
import traceback

log = logging.getLogger(__name__)

lights_bp = Blueprint('lights', __name__)

@lights_bp.route('/', methods=["GET"])
def get_lights():
    light_store = current_app.config.get("lightstore")
    lights = light_store.get_lights()

    response = []
    for i in lights:
        resp_i = {
            "name": i.name,
            "program_id": i.uuid,
            "type": i.type_id,
            "address": i.address
        }
        response.append(resp_i)
    log.debug(f"Response {response}")
    return json.dumps(response)

@lights_bp.route("/set_color", methods=["POST"])
def set_color():
    body = request.json

    try:
        r = body['r']
        g = body['g']
        b = body['b']
        brightness = body['brightness']

        light_store = current_app.config.get("lightstore")
        print(light_store)
        for i in light_store.get_lights():
            i.set_color(r, g, b, brightness)
        return {
            "status": "OK"
        }
    except Exception as e:
        log.error(traceback.print_exc())
        return {
            "status": "ERROR",
            "message": str(e)
        }