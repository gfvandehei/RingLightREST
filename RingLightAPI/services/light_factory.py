import logging
from RingLightAPI.model.ring_light import RingLight
from RingLightAPI.services.light_store import LightStore

log = logging.getLogger(__name__)

class LightFactory(object):

    def __init__(self, light_store: LightStore):
        print(light_store)
        self.created_ids = set()
        self.light_store = light_store

    def create_light(self, name, light_id, light_type, address):
        if light_type == "ring":
            log.debug(f"Attempting to create light {light_id}")
            # Create a ring light
            if light_id in self.created_ids:
                log.debug(f"Light {light_id} already exists")
            else:
                new_ring_light = RingLight(name, light_id, address)
                self.light_store.add_light(new_ring_light)
                self.created_ids.add(light_id)
                log.debug(f"Created light {light_id}")
        else:
            return