from singleton_decorator import singleton
from RingLightAPI.devices.light_abc import LightSource

@singleton
class LightStore(object):

    def __init__(self):
        self.lights = []

    def add_light(self, light_obj: LightSource):
        self.lights.append(light_obj)
        # print("added light")
        # print(self.lights)

    def get_lights(self):
        return self.lights

    def get_light(self, name):
        print(self.lights)
        for i in self.lights:
            if i.name == name:
                return i
        return None

    def get_lights_type(self, type_id: str):
        light_list = []
        for i in self.lights:
            if i.type_id == type_id:
                light_list.append(i)
        
        return light_list