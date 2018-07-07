from . import HMD


__g_device = None


def get_device():
    global __g_device

    if __g_device is None:
        __g_device = HMD.Device()

    return __g_device
