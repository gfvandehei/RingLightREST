from RingLightAPI.devices.light_abc import LightSource
from RingLightAPI.devices.client_ringlight import RingLightClient

RINGLIGHTLENGTH=36

class RingLightSource(LightSource):

    def __init__(self, name, address):
        super().__init__(name, address)
        self.state = [[0,0,0]]*RINGLIGHTLENGTH
        self.ring_client = RingLightClient(address[0])
        self.type_id = "ring"

    def set_color(self, r, g, b, brightness=255):
        for i in self.state:
            i[0] = r
            i[1] = g
            i[2] = b
        self.ring_client.send_frame(self.state, brightness)

    def set_pixel(self, pixel_num, r, g, b, brightness=255):
        if pixel_num > RINGLIGHTLENGTH:
            raise(ValueError(f"pixel num must be lower than {RINGLIGHTLENGTH}"))

        self.state[pixel_num] = [r, g, b]
        self.ring_client.send_frame(self.state, brightness)
    
    def set_frame(self, frame: list, brightness=255):
        if len(frame) != RINGLIGHTLENGTH:
            raise(ValueError(f"frame must have a length of {RINGLIGHTLENGTH}"))
        
        self.state = frame
        self.ring_client.send_frame(self.state, brightness)