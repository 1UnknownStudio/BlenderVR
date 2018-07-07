import bpy
from .operators import start, stop


class VRPanel(bpy.types.Panel):
    bl_idname = "VIEW3D_PT_BlenderVR"
    bl_label = "BlenderVR"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'

    def draw(self, context):
        self.layout.operator("vr.activate", text="Start VR")
        self.layout.operator("vr.deactivate", text="Stop VR")

