import bpy
import os

print("\n===== AMOGH GAME ENGINE EXPORTER =====")

# Create the export folder next to the Blender file
export_folder = os.path.join(
    bpy.path.abspath("//"),
    "exports"
)

os.makedirs(export_folder, exist_ok=True)

# Get selected mesh objects
selected_meshes = [
    obj for obj in bpy.context.selected_objects
    if obj.type == 'MESH'
]

exported_count = 0

# Export each selected asset
for obj in selected_meshes:

    # Deselect everything
    bpy.ops.object.select_all(action='DESELECT')

    # Select current asset
    obj.select_set(True)
    bpy.context.view_layer.objects.active = obj

    # Create filename
    export_path = os.path.join(
        export_folder,
        f"{obj.name}.fbx"
    )

    print(f"\nExporting: {obj.name}")

    # Export FBX with explicit settings
    bpy.ops.export_scene.fbx(
        filepath=export_path,
        use_selection=True,
        apply_scale_options='FBX_SCALE_ALL',
        axis_forward='-Z',
        axis_up='Y',
        use_mesh_modifiers=True,
        add_leaf_bones=False,
        bake_anim=False
    )

    print(f"✓ Exported → {obj.name}.fbx")

    exported_count += 1

# Restore selection
bpy.ops.object.select_all(action='DESELECT')

for obj in selected_meshes:
    obj.select_set(True)

print("\n===== EXPORT COMPLETE =====")
print(f"✓ {exported_count} asset(s) exported")
print(f"📁 Location: {export_folder}")