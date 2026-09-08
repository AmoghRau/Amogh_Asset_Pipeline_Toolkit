import bpy

#get all selected objs

selected_objects = bpy.context.selected_objects

#rename them
for i, obj in enumerate (selected_objects, start = 1):
    obj.name = f"Asset_{i:02d}"
    
print ("Assets renamed succesfully!")