import bpy

def assign_mesh_children_to_parent_bone(brick):
    
    #access this object 
    parent_rig = bpy.context.scene.objects.get(brick["armature_name"])
         
    #if parent object exists
    if parent_rig and parent_rig.type == "ARMATURE":   
             
        #scroll through all children by name
        for meshy in brick["mesh_children"]:  
                                                         
            child_mesh = bpy.context.scene.objects.get(meshy) #get each child
             
            #if child exists:
            if child_mesh and child_mesh.type == "MESH": 

                #parent this object                     
                child_mesh.parent = parent_rig
                
                #if bone exists
                if brick["bone_parent"]:
                    
                    #parent the object specifically to this bone
                    child_mesh.parent_type = 'BONE'
                    child_mesh.parent_bone = brick["bone_parent"]  
            
                    #keep transform                                      
                    child_mesh.matrix_parent_inverse = parent_rig.matrix_world.inverted()  


def deparent_each_mesh_object(this_obj):
    #access this object 
    mesh_child_ = bpy.context.scene.objects.get(this_obj)
    
    #if child exists:
    if mesh_child_:
             
        #deparent this object    
        mesh_child_.parent = None
    
        #keep transform                                  
        mesh_child_.matrix_world = mesh_child_.matrix_world.copy()    
        
#temp function        
def deparent_mesh_children_batch(this_obj):
    mesh_child_ = bpy.data.objects[this_obj.name]            #access this object it expects to exist
    mesh_child_.parent = None                                #deparent this object
    mesh_child_.matrix_world = mesh_child_.matrix_world.copy() 


def main():
    
    code = 0  #change this value to set mode
    
    match code:
        
        case 0:
            
            #populate this list
            parenter_chain = [
            {
            "armature_name": "Armature",
            "bone_parent": "Bone.001",
            "mesh_children": ["Cube"]
            },
            {
            "armature_name": "Armature",
            "bone_parent": "Bone.002",
            "mesh_children": ["Cube.002"]
            },
            {
            "armature_name": "Armature",
            "bone_parent": "Bone.003",
            "mesh_children": ["Cube.003"]
            },
            {
            "armature_name": "Armature",
            "bone_parent": "Bone.004",
            "mesh_children": ["Cube.004"]
            },
            {
            "armature_name": "Armature",
            "bone_parent": "Bone.005",
            "mesh_children": ["Cube.005"]
            },
            {
            "armature_name": "Armature",
            "bone_parent": "Bone.006",
            "mesh_children": ["Cube.006"]
            },
            
            ]
    
    
            for obj in parenter_chain:   #insert each object info dictionary into method
                assign_mesh_children_to_parent_bone(obj)
        
        case 1:
            
            deparenter_chain = ["Cube.153","Cube.004"]
    
            for x in deparenter_chain:  #insert each object name into method
                deparent_each_mesh_object(x)
            
        case 2:
        
            for x in bpy.context.selected_objects:  #collect all selected objects and put each one into method
                deparent_mesh_children_batch(x)
                
        case _:
            
            pass

if __name__ == "__main__":
    main()    
