import RingLightAPI.services as services
from flask import Flask
from flask_cors import CORS
import logging

logging.basicConfig(level=logging.DEBUG) 


app = Flask(__name__)
CORS(app)

from RingLightAPI.routes.ring_light import ring_bp
app.register_blueprint(ring_bp,  url_prefix='/lighting/ringlight')

def create_app():
    global app
    app.run()