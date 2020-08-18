import RingLightAPI.services as services
from flask import Flask
from flask_cors import CORS
import logging

from RingLightAPI.services.devicefinder import LightDeviceFinder
from RingLightAPI.services.light_factory import LightFactory
from RingLightAPI.services.light_store import LightStore
from RingLightAPI.config import config


logging.basicConfig(level=logging.DEBUG) 

lightstore = LightStore()
lightfact = LightFactory(light_store=lightstore)
lightfind = LightDeviceFinder(int(config["listener"]['port']), light_factory=lightfact)

lightfind.start()

app = Flask(__name__)
app.config['lightstore'] = lightstore
CORS(app)

with app.app_context():
    from RingLightAPI.routes.ring_light import ring_bp
    app.register_blueprint(ring_bp,  url_prefix='/lighting/ringlight')

def create_app():
    global app
    app.run()