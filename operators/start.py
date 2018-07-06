import bpy
from .. import blendervr
from .. import developer_utils as dUtil


# Operator to start the HMD
class ActivateHMD(bpy.types.Operator):
    bl_idname = "vr.activate"
    bl_label = "Start VR"
    bl_options = {'REGISTER'}

    def execute(self, context):
        dUtil.deb("Starting VR!")
        blendervr.get_device().start()
        return {'FINISHED'}