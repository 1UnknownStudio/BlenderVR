import socket
from . import developer_utils as dutil


class Server:
    __MAX_BUF = 4096
    __server = None

    def start(self):
        try:
            dutil.deb("Connecting to server...")
            self.__server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.__server.connect(('localhost', 8181))
            dutil.deb("Connected")
        except:
            dutil.err("Please start the BlenderVR-desktop application first")
            self.__server = None

    def get_server(self):
        if self.__server is None:
            self.start()
        return self.__server

    def close(self):
        if self.__server is not None:
            self.__server.close()

    def send(self, payload):
        payload = payload.encode()
        self.__server.send(payload)

    def receive(self):
        return self.__server.recv(self.__MAX_BUF)


server = Server()


def getServer():
    global server
    return server
