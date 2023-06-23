#Blender script to import OBJ and generate animation
#this script runs in blender
import bpy
import os

# obj_path
folder_path = r"D:\work\ComputerGraphics\PBF\pbf3d-master\data\01\obj"

# init params
start_frame = 0
end_frame = 299
last_obj = None
# Loop all files in the folder
for frame in range(start_frame, end_frame + 1):
    # set current frame
    bpy.context.scene.frame_set(frame)

    # import obj file
    filename = f"Frame_{frame+300}.obj"
    file_path = os.path.join(folder_path, filename)
    bpy.ops.import_scene.obj(filepath=file_path)

    # set keyframe and change obj location to make animation
    obj = bpy.context.selected_objects[0]
    if(frame != 0):
        last_obj.location[2] = 0
        last_obj.keyframe_insert(data_path='location', frame=bpy.context.scene.frame_current)
        obj.keyframe_insert(data_path='location', frame=bpy.context.scene.frame_current - 1)
    obj.location[2] = 10
    obj.keyframe_insert(data_path='location', frame=bpy.context.scene.frame_current)

    last_obj = obj