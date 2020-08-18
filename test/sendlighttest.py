import struct
import socket
import time
from threading import Thread
buffer = []


message = struct.pack("!BB", 0, 255)
for i in range(36):
    message += struct.pack("!BBB", 255, 255, 255)

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("", 0))

def recv_thread():
    global socket

    while True:
        msg, addr = socket.recvfrom(1024)
        print(msg, addr)

Thread(target=recv_thread).start()
while True:
    socket.sendto(message, ("192.168.1.2", 8888))
    time.sleep(5)
    print("sending")



