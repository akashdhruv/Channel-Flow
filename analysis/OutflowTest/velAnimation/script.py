# trace generated using paraview version 5.10.0
# import paraview
# paraview.compatibility.major = 5
# paraview.compatibility.minor = 10

import os

#### import the simple module from the paraview
from paraview.simple import *

#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

basename = "INS_Channel_Flow.xmf"

filenames=[
    os.getenv("SIMULATION_HOME") + os.sep + "reference/jobnode.archive/2022-10-27/" + basename,
]

# create a new 'XDMF Reader'
simulation = XDMFReader(registrationName="Simulation", FileNames=filenames)
simulation.CellArrayStatus = ["dust", "pres", "velx", "vely"]
simulation.GridStatus = ["Time_Series"]

# get active view
renderView1 = GetActiveViewOrCreate("RenderView")

# get the material library
materialLibrary1 = GetMaterialLibrary()

# get display properties
simulation_Display = GetDisplayProperties(simulation, view=renderView1)

# get color transfer function/color map for 'vtkBlockColors'
vtkBlockColorsLUT = GetColorTransferFunction("vtkBlockColors")

# get opacity transfer function/opacity map for 'vtkBlockColors'
vtkBlockColorsPWF = GetOpacityTransferFunction("vtkBlockColors")

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# create a new 'Slice'
slice1 = Slice(registrationName="Slice1", Input=simulation)
slice1.SliceType = "Plane"
slice1.SliceType.Normal = [0.0, 0.0, 1.0]

# hide data in view
Hide(simulation, renderView1)

# create a new 'Merge Blocks'
mergeBlocks1 = MergeBlocks(registrationName="MergeBlocks1", Input=slice1)

# hide data in view
Hide(slice1, renderView1)

# create a new 'Cell Data to Point Data'
cellDatatoPointData1 = CellDatatoPointData(registrationName="CellDatatoPointData1", Input=mergeBlocks1)
cellDatatoPointData1.CellDataArraytoprocess = ["dust", "pres", "velx", "vely"]

# show data in view
cellDatatoPointData1Display = Show(cellDatatoPointData1, renderView1, "UnstructuredGridRepresentation")

# hide data in view
Hide(mergeBlocks1, renderView1)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# update the view to ensure updated data information
renderView1.Update()

# reset view to fit data bounds
renderView1.ResetCamera(
    0.0, 10.0, -0.5, 0.5, 4.999999987376214e-07, 4.999999987376214e-07, False
)

# set scalar coloring
ColorBy(cellDatatoPointData1Display, ("POINTS", "velx"))

# rescale color and/or opacity maps used to include current data range
cellDatatoPointData1Display.RescaleTransferFunctionToDataRange(True, False)

# show color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, True)

# get color transfer function/color map for 'velx'
velxLUT = GetColorTransferFunction("velx")

# get opacity transfer function/opacity map for 'velx'
velxPWF = GetOpacityTransferFunction("velx")

# Rescale transfer function
velxLUT.RescaleTransferFunction(0.0, 1.2)

# Rescale transfer function
velxPWF.RescaleTransferFunction(0.0, 1.2)

# get color legend/bar for velxLUT in view renderView1
velxLUTColorBar = GetScalarBar(velxLUT, renderView1)

# Properties modified on velxLUT
velxLUT.NumberOfTableValues = 20

# change scalar bar placement
velxLUTColorBar.WindowLocation = "Any Location"

# change scalar bar placement
velxLUTColorBar.Position = [0.6594568777292575, 0.12046908315565036]

# hide color bar/color legend
cellDatatoPointData1Display.SetScalarBarVisibility(renderView1, False)

# get layout
layout1 = GetLayout()

# layout/tab size in pixels
layout1.SetSize(1832, 938)

# current camera placement for renderView1
renderView1.CameraPosition = [
    4.706096717903555,
    -0.09981620901388674,
    19.412388018016625,
]
renderView1.CameraFocalPoint = [
    5.022919463453465,
    -0.6295747792393019,
    1.230827167612428,
]
renderView1.CameraViewAngle = 16.637554585152838
renderView1.CameraParallelScale = 5.024937810560445

# save animation
SaveAnimation(
    "./velAnimation.avi",
    renderView1,
    ImageResolution=[1832, 936],
    FrameRate=5,
    FrameWindow=[0, 200],
)

# ================================================================
# addendum: following script captures some of the application
# state to faithfully reproduce the visualization during playback
# ================================================================

# --------------------------------
# saving layout sizes for layouts

# layout/tab size in pixels
layout1.SetSize(1832, 938)

# -----------------------------------
# saving camera placements for views

# current camera placement for renderView1
renderView1.CameraPosition = [
    4.706096717903555,
    -0.09981620901388674,
    19.412388018016625,
]
renderView1.CameraFocalPoint = [
    5.022919463453465,
    -0.6295747792393019,
    1.230827167612428,
]
renderView1.CameraViewAngle = 16.637554585152838
renderView1.CameraParallelScale = 5.024937810560445

# --------------------------------------------
# uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
