import RingLightAPI.services as services
from flask import Flask
from flask_cors import CORS
import logging
from logging import handlers
import sys

from RingLightAPI.services.devicefinder import LightDeviceFinder
from RingLightAPI.services.light_factory import LightFactory
from RingLightAPI.services.light_store import LightStore
from RingLightAPI.config import config

if config['logging']['file'] == "true":
    class StreamToLogger(object):
        """
        Fake file-like stream object that redirects writes to a logger instance.
        """
        def __init__(self, logger, log_level=logging.INFO):
                self.logger = logger
                self.log_level = log_level
                self.linebuf = ''

        def write(self, buf):
                for line in buf.rstrip().splitlines():
                    self.logger.log(self.log_level, line.rstrip())

        def flush(self):
            pass

    logging.basicConfig(
        level=int(config['logging']['level']),
        format="[%(asctime)s] %(levelname)s: <%(filename)s:%(lineno)s> %(message)s",
        filename="out.log",
        filemode='w'
    )

    stdout_logger = logging.getLogger('STDOUT')
    sl = StreamToLogger(stdout_logger, logging.INFO)
    sys.stdout = sl

    stderr_logger = logging.getLogger('STDERR')
    sl = StreamToLogger(stderr_logger, logging.ERROR)
    sys.stderr = sl
else:
    logging.basicConfig(
        level=int(config['logging']['level']),
        format="[%(asctime)s] %(levelname)s: <%(filename)s:%(lineno)s> %(message)s",
    )

"""logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: <%(filename)s:%(lineno)s> %(message)s",
    level=int(config['logging']['level'])
) """

lightstore = LightStore()
lightfact = LightFactory(light_store=lightstore)
lightfind = LightDeviceFinder(int(config["listener"]['port']), light_factory=lightfact)

lightfind.start()

app = Flask(__name__, template_folder=config['angular']['path'], static_folder="/home/gabriel/Documents/projects/RingLightAngular/dist/", static_url_path="/static")
app.config['lightstore'] = lightstore
CORS(app)

with app.app_context():
    from RingLightAPI.routes.main import main_bp
    app.register_blueprint(main_bp)
    from RingLightAPI.routes.lights import lights_bp
    app.register_blueprint(lights_bp, url_prefix="/lights")
    from RingLightAPI.routes.ring_light import ring_bp
    app.register_blueprint(ring_bp,  url_prefix='/ringlights')

def create_app():
    global app
    app.run(host='0.0.0.0', port=80)