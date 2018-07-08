import socket
from enum import Enum


class Messenger:
    class MessageType(Enum):
        PRE_SEND_META = 1
        POST_SEND_META = 2

    __con = None

    def __init__(self, con):
        self.__con = con



