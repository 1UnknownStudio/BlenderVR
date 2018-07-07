"""
Copyright (C) 2018 Lars Johan Nyboe
http://github.com/larsjohan/blendervr

Created by Lars Johan Nyboe

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import bpy

# load and reload submodules
##################################

import importlib
from . import developer_utils as dutil
from . import ui
import traceback

importlib.reload(dutil)
importlib.reload(ui)
modules = dutil.setup_addon_modules(__path__, __name__, "bpy" in locals())


# Addon meta
##################################
bl_info = {
    "name": "BlenderVR",
    "description": "An addon for viewing and editing 3D models in VR",
    "author": "Lars Johan Nyboe",
    "version": (0, 1, 1),
    "blender": "2.79",
    "location": "View3D",
    "warning": "This addon is still in development.",
    "wiki_url": "https://github.com/larsjohan/blendervr/wiki",
    "category": "VR"
}

# register
##################################


def register():
    try:
        bpy.utils.register_module(__name__)
    except:
        traceback.print_exc()

    dutil.deb("Registered {} with {} modules".format(bl_info["name"], len(modules)))


def unregister():
    try:
        bpy.utils.unregister_module(__name__)
    except:
        traceback.print_exc()

    dutil.deb("Unregistered {}".format(bl_info["name"]))
