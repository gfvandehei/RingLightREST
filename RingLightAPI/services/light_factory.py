import logging

class LightFactory(object):

    def __init__(self, light_store=None):
        self.created_ids = set()
        self.light_store = light_store

    def create_light(self, name, light_id, light_type):
        if light_type == "ring":
            logging.debug(f"Attempting to create light {light_id}")
            # Create a ring light
            if light_id in self.created_ids:
                logging.debug(f"Light {light_id} already exists")
                return
            else:
                
            return
        else:
            return