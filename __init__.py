# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "setorigin",
    "author" : "bguenthe",
    "description" : "",
    "blender" : (2, 80, 0),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

import bpy

class MoveOrigin(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.origin_to_selected"
    bl_label = "Origin to selected"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        #obj = context.active_object
        return True
        #return obj is not None and obj.mode == 'EDIT'

    def execute(self, context):
        objmode = context.active_object.mode
        saved_location = bpy.context.scene.cursor.location.copy()
        bpy.ops.view3d.snap_cursor_to_selected()

        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')  
        bpy.context.scene.cursor.location = saved_location

        if objmode == 'EDIT':        
            bpy.ops.object.mode_set(mode = 'EDIT')
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')

        return {'FINISHED'}

class MoveOriginAndCursor(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.origin_and_cursor_to_selected"
    bl_label = "Origin and cursor to selected"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):
        obj = context.active_object
        return True
        #return obj is not None and obj.mode == 'EDIT'

    def execute(self, context):
        objmode = context.active_object.mode
        bpy.ops.view3d.snap_cursor_to_selected()

        bpy.ops.object.mode_set(mode = 'OBJECT')
        bpy.ops.object.origin_set(type='ORIGIN_CURSOR')  

        if objmode == 'EDIT':        
            bpy.ops.object.mode_set(mode = 'EDIT')
        else:
            bpy.ops.object.mode_set(mode = 'OBJECT')

        return {'FINISHED'}        

def menu_func(self, context):
    self.layout.operator(MoveOrigin.bl_idname)

def register():
    bpy.utils.register_class(MoveOrigin)
    bpy.types.VIEW3D_MT_object_context_menu.append(menu_func)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.append(menu_func)
    
    bpy.utils.register_class(MoveOriginAndCursor)

def unregister():
    bpy.utils.unregister_class(MoveOrigin)
    bpy.types.VIEW3D_MT_object_context_menu.remove(menu_func)
    bpy.types.VIEW3D_MT_edit_mesh_context_menu.remove(menu_func)
    bpy.utils.unregister_class(MoveOriginAndCursor)


if __name__ == "__main__":
    register()