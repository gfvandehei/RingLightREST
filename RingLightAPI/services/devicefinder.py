from threading import Thread
import socket
import json
import logging

class LightDeviceFinder(Thread):

    def __init__(self, config, light_factory):
        self.end_f = False
        
        self.l_port = config.get('devices.broadcastport', default=2666)
        
        self.l_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.l_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.l_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        self.l_socket.settimeout(1)
        self.l_socket.bind(("", self.l_port))

    def run(self):
        logging.info("Network finding activated, finding devices")
        while not self.end_f:
            try:
                data, addr = self.l_socket.recvfrom(1024)
                data_json = json.loads(data)
                device = self.check_data_json(data_json)
                if device is not None:
                    self.register_device(device[0], device[1], device[2])
            except socket.timeout:
                continue
            except json.JSONDecodeError as err:
                logging.warning(f"Received invalid json {data} with err: {err}")
                continue

    def check_data_json(self, data_json):
        try:
            name = data_json['name']
            d_id = data_json['id']
            d_type = data_json['type']
            return (name, d_id, d_type)
        except Exception as err:
            logging.warning(err)
            return None

    def register_device(self, name, d_id, d_type):
        pass
