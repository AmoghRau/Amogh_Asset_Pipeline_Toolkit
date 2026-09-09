#Asset Validator

import bpy

#validation settings
POLYGON_LIMIT = 1000

print("\n ==== AMOGH ASSET VALIDATOR ====")

for obj in bpy.context.selected_objects:
    #only validate mesh objects
    if obj.type != 'MESH':
        continue
    issues = []
    
    #poly count checker
    polygon_count = len(obj.data.polygons)
    
    if polygon_count > POLYGON_LIMIT:
        issues.append(f"Too many polygons ({polygon_count})")
        
    #material checker
    mat_count = len(obj.data.materials)
    if mat_count == 0:
        issues.append("No material")
    
    #printing result
    if len(issues) == 0:
        print(f" ✓ {obj.name}: READY ")
    else:
        print(f" ⚠ {obj.name} : NEEDS ATTENTION ")
        for issues in issues:
            print(f"    - {issues}")

print("==== VALIDATION COMPLETE ====")
       
        
    