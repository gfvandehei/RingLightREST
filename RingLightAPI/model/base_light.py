import socket

class BaseLight(object):

    def __init__(self, address, l_type, name, l_id):
        self.address = address
        self.type = l_type
        self.name = name
        self.light_id = l_id
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def send_message(self, message):
        self.socket.sendto(message, self.address)
