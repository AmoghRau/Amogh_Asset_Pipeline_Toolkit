import bpy 

poly_limit = 1000

for obj in bpy.context.selected_objects:
    if obj.type == 'MESH' :
        
        #counting the polygons
        poly_count = len(obj.data.polygons)
        
        #deciding whether the asset is okay or not
        if poly_count <= poly_limit :
            print(f" ✓ {obj.name}: {poly_count} polygons - GOOD")
        else:
            print(f"⚠ {obj.name} : {poly_count} polygons - TOO HIGH")