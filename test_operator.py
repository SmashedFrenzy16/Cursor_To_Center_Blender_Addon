import bpy

class TEST_OT_OPERATOR(bpy.types.Operator):
    bl_idname = "view3d.cursor_center"
    bl_label = "Simple operator"
    bl_description = "Centers the 3d cursor"

    def execute(self, context):
        bpy.ops.view3d.snap_cursor_to_center()


        return {"FINISHED"}

