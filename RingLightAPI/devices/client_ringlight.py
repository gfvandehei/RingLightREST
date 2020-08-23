import socket
import struct
import logging

RINGLIGHTDATAPORT = 8888

log = logging.getLogger(__name__)

class RingLightClient(object):

    def __init__(self, address):
        self.ring_address = address
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind(("", 0))

    def send_frame(self, frame, brightness):
        """
        protocol is opcode 1 <0> | brightness 1 <0-255> | framedata 
        """
        # make message
        message = struct.pack("!BB", 0, brightness)
        for i in frame:
            message += struct.pack("!BBB", i[0], i[1], i[2]) 
        # send message
        self.socket.sendto(message, (self.ring_address, RINGLIGHTDATAPORT))


    