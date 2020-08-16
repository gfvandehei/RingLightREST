import RingLightAPI.services as services
import logging

logging.basicConfig(level=logging.DEBUG)

def create_app():
    services.create_init()
