import bpy

#check every selected object for their material, if no material, needs attention!

for obj in bpy.context.selected_objects:
    
    #only checking 3D mesh objects
    
    if obj.type == 'MESH':
        
        #count material
        mat_count = len(obj.data.materials)
        
        #check whether obj has material
        if mat_count > 0:
            print(f" ✓ {obj.name} : Has material - GOOD")
        else:
            print( f" ⚠ {obj.name} : No material - NEEDS ATTENTION")
            