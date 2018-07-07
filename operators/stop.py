import bpy
from .. import blendervr
from .. import developer_utils as dutil


# Operator to stop the HMD
class DeActivateHMD(bpy.types.Operator):
    bl_idname = "vr.deactivate"
    bl_label = "Stop VR"
    bl_options = {'REGISTER'}

    def execute(self, context):
        dutil.deb("Stopping VR!")
        blendervr.get_device().stop()
        return {'FINISHED'}
