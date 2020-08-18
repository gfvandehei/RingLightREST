from threading import Thread
import socket
import json
import logging
from RingLightAPI.services.light_factory import LightFactory

class LightDeviceFinder(Thread):

    def __init__(self, listen_port, light_factory: LightFactory):
        Thread.__init__(self)
        self.end_f = False
        self.l_port = listen_port
        
        self.l_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.l_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.l_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.l_socket.settimeout(1)
        self.l_socket.bind(("", self.l_port))

        self.light_factory = light_factory

    def run(self):
        logging.info("Network finding activated, finding devices")
        while not self.end_f:
            try:
                data, addr = self.l_socket.recvfrom(1024)
                logging.debug(f"Received data {data}")
                data_json = json.loads(data)
                device = self.check_data_json(data_json)
                if device is not None:
                    self.register_device(device[0], device[1], device[2], (addr[0], 8888))
            except socket.timeout:
                continue
            except json.JSONDecodeError as err:
                logging.warning(f"Received invalid json {data} with err: {err}")
                continue

    def check_data_json(self, data_json):

        try:
            name = data_json['name']
            d_type = data_json['type']
            return (name, name, d_type)
        except Exception as err:
            logging.warning(err)
            return None

    def register_device(self, name, d_id, d_type, address):
        self.light_factory.create_light(name, d_id, d_type, address)
