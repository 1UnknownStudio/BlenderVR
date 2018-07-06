from . import developer_utils as dUtil
from . import HMD

__g_device = None


def get_device():
    global __g_device

    if (__g_device == None):
        __g_device = HMD.Device()

    return __g_device
