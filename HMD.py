import bpy
import openvr
from . import developer_utils as dUtil

C = bpy.context
D = bpy.data
O = bpy.ops


class Device:
    # IVRSystem pointer
    __system = None

    # Blender cameras
    eyeL = None
    eyeR = None

    def __init__(self):
        dUtil.deb("Initiated HMD-instance")

    def start(self):
        self.__system = openvr.init(openvr.VRApplication_Scene)
        #projMatrixL = openvr.IVRSystem.getProjectionMatrix(openvr.EVREye., 0, 1)
        self.build_cameras()

    def stop(self):
        openvr.shutdown()
        self.destroy_cameras()

    def build_cameras(self):
        O.object.add(type='CAMERA', location=[1.0, 0.0, 4.0])
        self.eyeL = C.active_object

        O.object.add(type='CAMERA', location=[2.0, 0.0, 4.0])
        self.eyeR = C.active_object

        self.eyeL.name = "eyeL"
        self.eyeR.name = "eyeR"

    def destroy_cameras(self):
        self.eyeL.select = True
        O.object.delete()

        self.eyeR.select = True
        O.object.delete()