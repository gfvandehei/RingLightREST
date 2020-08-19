from RingLightAPI.model.ring_light import RingLight
from singleton_decorator import singleton

@singleton
class LightStore(object):

    def __init__(self):
        self.lights = []

    def add_light(self, light_obj:RingLight):
        self.lights.append(light_obj)
        # print("added light")
        # print(self.lights)

    def get_lights(self):
        return self.lights

    def get_light(self, lid):
        print(self.lights)
        for i in self.lights:
            if i.l_id == lid:
                return i
        return None