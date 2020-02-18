# <pep8-80 compliant>
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

import bpy
from bpy.types import Operator, Panel

bl_info = {
        "name": "Center view3D to Origin",
        "author": "Aldrik, Spirou4D",
        "blender": (2, 81, 0),
        "version": (0, 3, 1),
        "description": "Move the view to the World origin",
        "warning": "crtl + shift + Numpad .",
        "location": "3D Viewport > View",
        "wiki_url": "",
        "tracker_url": "",
        "category": "3D View"
    }

# ------ operator ------
class VIEW3D_OT_World_Origin_All(Operator):
    """Move the view to Origin without change the cursor position"""
    bl_idname = 'view3d.origin_all_view'
    bl_label = "Center view3D to Origin"
    bl_options = {'REGISTER', 'UNDO'}

    def invoke(self, context, event):
            v3d = context.space_data

            if v3d.type == 'VIEW_3D':
                csc = context.scene.cursor
                current_cloc = csc.location.xyz
                csc.location = (0, 0, 0)
                bpy.ops.view3d.view_center_cursor()
                csc.location = current_cloc
            return {'FINISHED'}

# ------ panel ------
class VIEW3D_PT_World_Origin_All(Panel):
    bl_category = "View"
    bl_label = "Center view to..."
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = 'objectmode'


    def draw(self, context):
        layout = self.layout
        row = layout.column(align=True).row(align=True)
        props = row.operator("view3d.origin_all_view", text="World origin")
        props = row.operator("view3d.view_center_cursor", text="Cursor")


classes = (VIEW3D_OT_World_Origin_All, VIEW3D_PT_World_Origin_All)
km_list = ['Object Mode','Mesh']
# ------ register ------
def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    for i in km_list:
        km = bpy.context.window_manager.keyconfigs.default.keymaps[i]
        kmi = km.keymap_items.new('view3d.origin_all_view', 'NUMPAD_PERIOD', 'PRESS', ctrl=True, shift=True )

# ------ unregister ------
def unregister():
    for i in km_list:
        km = bpy.context.window_manager.keyconfigs.default.keymaps[i]
        for kmi in (kmi for kmi in km.keymap_items if (kmi.idname == "view3d.origin_all_view")):
            km.keymap_items.remove(kmi)

    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
# ------------
if __name__ == '__main__':
    register()
