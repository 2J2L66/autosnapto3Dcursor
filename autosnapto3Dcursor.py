bl_info = {
    "name": "Auto Snap to 3D Cursor",
    "author": "jjl",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "description": "Déplace automatiquement l'objet actif vers le curseur 3D.",
    "category": "3D View",
}

import bpy

enabled = False

def follow_cursor(scene):
    if not enabled:
        return
    obj = bpy.context.active_object
    cursor = bpy.context.scene.cursor.location
    if obj and obj.mode == 'OBJECT':
        obj.location = cursor

class OBJECT_OT_toggle_auto_snap(bpy.types.Operator):
    bl_idname = "object.toggle_auto_snap"
    bl_label = "Activer/Désactiver Auto Snap"
    bl_description = "Active ou désactive le déplacement automatique vers le curseur 3D"
    
    def execute(self, context):
        global enabled
        enabled = not enabled
        self.report({'INFO'}, f"Auto Snap is now {'enabled' if enabled else 'disabled'}")
        return {'FINISHED'}

class VIEW3D_PT_auto_snap_panel(bpy.types.Panel):
    bl_label = "Auto Snap to 3D Cursor"
    bl_idname = "VIEW3D_PT_auto_snap_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.toggle_auto_snap", text="Activer/Désactiver Auto Snap")

def register():
    bpy.utils.register_class(OBJECT_OT_toggle_auto_snap)
    bpy.utils.register_class(VIEW3D_PT_auto_snap_panel)
    bpy.app.handlers.depsgraph_update_post.append(follow_cursor)

def unregister():
    bpy.utils.unregister_class(OBJECT_OT_toggle_auto_snap)
    bpy.utils.unregister_class(VIEW3D_PT_auto_snap_panel)
    bpy.app.handlers.depsgraph_update_post.remove(follow_cursor)

if __name__ == "__main__":
    register()
