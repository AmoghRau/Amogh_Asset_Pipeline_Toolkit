import bpy

print("\n ==== AMOGH AUTOMATIC CLEANUP ====")

#checking for empty material slots
for obj in bpy.context.selected_objects:
    
    #only clean mesh objs
    if obj.type != 'MESH':
        continue
    before = len(obj.data.materials)
    
    #remove empty material slots
    for i in range(len(obj.data.materials) -1, -1, -1):
        if obj.data.materials[i] is None:
            obj.materials.pop(index = i)
            
    after = len(obj.data.materials)
    removed = before - after
    
    #applying transforms  (location, rotation, scale)
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    
    bpy.ops.object.transform_apply(
        location = True,
        rotation = True,
        scale = True
    )
    
    #standardize obj names like v01
    old_name = obj.name
    obj.name = f"Asset_{i:02d}"
    #report result
    print(f"\n✓ {old_name} -> {obj.name}")
    
    
    
    #if anything happened, report it
 
    if removed > 0:
        print(f" ✓ {obj.name} : Removed {removed} empty material slot(s)")
    else:
        print(f" {obj.name} : No empty material slots")
        
        
    print(f" -> Transforms Applied")
    print(f" -> Name Standardized") 

print(" ==== CLEANUP COMPLETE ==== ")

    