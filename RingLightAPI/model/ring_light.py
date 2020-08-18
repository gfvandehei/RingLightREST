from RingLightAPI.model.base_light import BaseLight
import struct
import socket

class RingLight(object):

    def __init__(self, name, l_id, address):
        self.name = name
        self.l_id = l_id
        self.address = address
        self.state = [[0,0,0]]*36

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def set_strip_color(self, r, g, b, brightness):
        # create message buffer
        # opcode and brightness
        for i in self.state:
            i[0] = r
            i[1] = g
            i[2] = b

        message = struct.pack("!BB", 0, brightness) # opcode 0 is frame
        for i in self.state:
            message += struct.pack("!BBB", i[0], i[1], i[2])
        print(f"Sending message {message} to {self.l_id} at address {self.address}")
        self.socket.sendto(message, self.address)

    def set_entire_frame(self, framedata, brightness):
        if len(framedata) != 36:
            raise(ValueError("Framedata needs to be 36 in length"))

        message = struct.pack("!BB", 0, brightness)
        self.state = framedata
        for i in self.state:
            message += struct.pack("!BBB", i[0], i[1], i[2])
        print(f"Sending message {message} to {self.l_id} at address {self.address}")
        self.socket.sendto(message, self.address)
