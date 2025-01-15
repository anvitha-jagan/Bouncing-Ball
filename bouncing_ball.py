import omni.usd
from pxr import Usd, UsdGeom, Gf  # Import Gf for vector types

# Get the Omniverse stage (this connects to the current stage)
stage = omni.usd.get_context().get_stage()

# If no stage exists, create a new one
if not stage:
    stage = Usd.Stage.CreateNew('sphere_scene.usd')

# Define a transform (Xform) at /World
world_xform = UsdGeom.Xform.Define(stage, '/World')

# Create a sphere as a child of /World
sphere = UsdGeom.Sphere.Define(stage, world_xform.GetPath().AppendPath('Sphere'))


# Set the radius of the sphere
sphere.GetRadiusAttr().Set(1.0)

# Create a cube (box) as a backdrop
box = UsdGeom.Cube.Define(stage, world_xform.GetPath().AppendPath("Backdrop"))
box.GetDisplayColorAttr().Set([(0.0, 0.0, 1.0)])

# Apply transformations to the box (scale and translate)
cube_xform_api = UsdGeom.XformCommonAPI(box)
cube_xform_api.SetScale(Gf.Vec3f(5, 5, 0.1))
cube_xform_api.SetTranslate(Gf.Vec3d(0, 0, -2))

# Set the time range for the scene
stage.SetStartTimeCode(1)
stage.SetEndTimeCode(60)

# Create XformCommonAPI object for the sphere
sphere_xform_api = UsdGeom.XformCommonAPI(sphere)
sphere_xform_api.SetTranslate(Gf.Vec3d(0, 5.5, 0))

# Set translation of the sphere at different times
sphere_xform_api.SetTranslate(Gf.Vec3d(0,  5.50, 0), time=1)  
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -4.50, 0), time=30)  
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -5.00, 0), time=45)  
sphere_xform_api.SetTranslate(Gf.Vec3d(0, -3.25, 0), time=50)  
sphere_xform_api.SetTranslate(Gf.Vec3d(0,  5.50, 0), time=60)  

# Set scale of the sphere at different times
sphere_xform_api.SetScale(Gf.Vec3f(1.00, 1.00, 1.00), time=1)  
sphere_xform_api.SetScale(Gf.Vec3f(1.00, 1.00, 1.00), time=30)   
sphere_xform_api.SetScale(Gf.Vec3f(1.00, 0.20, 1.25), time=45)   
sphere_xform_api.SetScale(Gf.Vec3f(0.75, 2.00, 0.75), time=50)  
sphere_xform_api.SetScale(Gf.Vec3f(1.00, 1.00, 1.00), time=60)  

# Save the stage to disk
stage.GetRootLayer().Save()  # Use Save() instead of Export()

# Optionally, open and display the USD file in Omniverse (assuming you have the visualization set up)
omni.usd.get_context().open_stage('sphere_scene.usd')

print("Sphere created and scene saved as 'sphere_scene.usd'")


  
