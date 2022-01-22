
bl_info = {
    "name" : "test",
    "author" : "SmashedFrenzy16",
    "description" : "Test Blender Addon",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy

from . test_operator import TEST_OT_OPERATOR

from .test_panel import Test_PT_Panel

classes = (TEST_OT_OPERATOR, Test_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)
