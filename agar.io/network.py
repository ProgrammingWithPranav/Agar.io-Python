import socket

class Network:
    def __init__(self):
        self.network = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "172.16.8.21"
        self.port = 5555
        sefl.addr = (self.server, self.port)

    def connect(self):
        pass

    def disconnect(self, name):
        pass

    def send(self, data, pick=False):
        pass 