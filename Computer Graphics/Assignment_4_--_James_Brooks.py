# ************************************************************************************
# James Brooks
# CSC 470-001
# Assignment 4
# February 15th, 2021
# ************************************************************************************

# ***************************** Import Required Libraries ****************************
# Math is used to calculate radians and trigonometry for rotate functions.
import math
# Copy is used to make the default point clouds.
import copy
# Tkinter is used for the window and rendering.
from tkinter import *

# *********************************** Initialize Window *****************************
# Initialize window width, height, and distance from the view.
# This is used in projection and display coordinate conversion calculations.
CanvasWidth = 400
CanvasHeight = 400
d = 500

# *********************************** Initialize zBuffer *****************************
# zBuffer is a double array using canvas height and width
# Default value is d (viewpoint)
zBuffer = []
for i in range(CanvasHeight):
    new = []
    for j in range(CanvasWidth):
        new.append(d)
    zBuffer.append(new)

# Deep copy zBuffer. Used for resetting zBuffer
DefaultzBuffer = copy.deepcopy(zBuffer)

# ***************************** Initialize Cube 1 Object ****************************
# New smaller Cube object that is slightly closer.
# Definition  of the eight underlying points
C1top1 = [-75,75,100]
C1top2 = [-50,75,100]
C1top3 = [-50,75,75]
C1top4 = [-75,75,75]
C1bot1 = [-75,50,75]
C1bot2 = [-50,50,75]
C1bot3 = [-50,50,100]
C1bot4 = [-75,50,100]

# Definition of the six polygon faces using the meaningful point names
# Polys are defined in clockwise order when viewed from the outside
C1frontpoly = [C1top4,C1top3,C1bot2,C1bot1]
C1rightpoly = [C1top3,C1top2,C1bot3,C1bot2]
C1backpoly = [C1top2,C1top1,C1bot4,C1bot3]
C1leftpoly = [C1top1,C1top4,C1bot1,C1bot4]
C1bottompoly = [C1bot1,C1bot2,C1bot3,C1bot4]
C1toppoly = [C1top1,C1top2,C1top3,C1top4]

# Definition of the first cube object
Cube1 = [C1toppoly, C1frontpoly, C1rightpoly, C1backpoly, C1leftpoly, C1bottompoly]
# Definition of the color associated with each face of the second cube
Cube1Color = ["#5193C2", "#321C41", "#E1CF1A", "#38444B", "#10E2A9", "#A83E77"]

# Definition of the First Cube's underlying point cloud.  No structure, just the points.
Cube1PointCloud = [C1top1, C1top2, C1top3, C1top4, C1bot1, C1bot2, C1bot3, C1bot4]
DefaultCube1PointCloud = copy.deepcopy(Cube1PointCloud)

# ***************************** Initialize Pyramid Object ***************************
# Original Pyramid.
# Definition  of the five underlying points
Papex = [0,50,100]
Pbase1 = [-50,-50,50]
Pbase2 = [50,-50,50]
Pbase3 = [50,-50,150]
Pbase4 = [-50,-50,150]

# Definition of the five polygon faces using the meaningful point names
# Polys are defined in clockwise order when viewed from the outside
Pfrontpoly = [Papex,Pbase2,Pbase1]
Prightpoly = [Papex,Pbase3,Pbase2]
Pbackpoly = [Papex,Pbase4,Pbase3]
Pleftpoly = [Papex,Pbase1,Pbase4]
Pbottompoly = [Pbase1,Pbase2,Pbase3,Pbase4]

# Definition of the pyramid object
Pyramid = [Pbottompoly, Pfrontpoly, Prightpoly, Pbackpoly, Pleftpoly]
# Definition of the color associated with each face of the pyramid
PyramidColor = ["black", "red", "green", "blue", "yellow"]

# Definition of the Pyramid's underlying point cloud.  No structure, just the points.
PyramidPointCloud = [Papex, Pbase1, Pbase2, Pbase3, Pbase4]
DefaultPyramidPointCloud = copy.deepcopy(PyramidPointCloud)

# ***************************** Initialize Cube 2 Object ****************************
# New larger Cube object that is slightly further away.
# Definition  of the eight underlying points
C2top1 = [25,75,150]
C2top2 = [75,75,150]
C2top3 = [75,75,100]
C2top4 = [25,75,100]
C2bot1 = [25,25,100]
C2bot2 = [75,25,100]
C2bot3 = [75,25,150]
C2bot4 = [25,25,150]

# Definition of the six polygon faces using the meaningful point names
# Polys are defined in clockwise order when viewed from the outside
C2frontpoly = [C2top4,C2top3,C2bot2,C2bot1]
C2rightpoly = [C2top3,C2top2,C2bot3,C2bot2]
C2backpoly = [C2top2,C2top1,C2bot4,C2bot3]
C2leftpoly = [C2top1,C2top4,C2bot1,C2bot4]
C2bottompoly = [C2bot1,C2bot2,C2bot3,C2bot4]
C2toppoly = [C2top1,C2top2,C2top3,C2top4]

# Definition of the second cube object
Cube2 = [C2toppoly, C2frontpoly, C2rightpoly, C2backpoly, C2leftpoly, C2bottompoly]
# Definition of the color associated with each face of the second cube
Cube2Color = ["white", "#cccccc", "#999999", "#666666", "#333333", "black"]

# Definition of the Second Cube's underlying point cloud.  No structure, just the points.
Cube2PointCloud = [C2top1, C2top2, C2top3, C2top4, C2bot1, C2bot2, C2bot3, C2bot4]
DefaultCube2PointCloud = copy.deepcopy(Cube2PointCloud)

# ***************************** Initialize Cylinder Object ****************************
# Definition of the 16 underlying points
front1 = [-50.0,120.7107,50.0]
front2 = [50.0,120.7107,50.0]
front3 = [120.7107,50.0,50.0]
front4 = [120.7107,-50.0,50.0]
front5 = [50.0,-120.7107,50.0]
front6 = [-50.0,-120.7107,50.0]
front7 = [-120.7107,-50.0,50.0]
front8 = [-120.7107,50.0,50.0]
back1 = [-50.0,120.7107,450.0]
back2 = [50.0,120.7107,450.0]
back3 = [120.7107,50.0,450.0]
back4 = [120.7107,-50.0,450.0]
back5 = [50.0,-120.7107,450.0]
back6 = [-50.0,-120.7107,450.0]
back7 = [-120.7107,-50.0,450.0]
back8 = [-120.7107,50.0,450.0]

# Definition of the ten polygon faces using the meaningful point names
# Polys are defined in clockwise order when viewed from the outside
northPoly = [front1, back1, back2, front2]
northEastPoly = [front2, back2, back3, front3]
eastPoly = [front3, back3, back4, front4]
southEastPoly = [front4, back4, back5, front5]
southPoly = [front5, back5, back6, front6]
southWestPoly = [front6, back6, back7, front7]
westPoly = [front7, back7, back8, front8]
northWestPoly = [front8, back8, back1, front1]
frontPoly = [front1, front2, front3, front4, front5, front6, front7, front8]
backPoly = [back1, back8, back7, back6, back5, back4, back3, back2]

# Definition of the cylinder object
Cylinder = [northPoly, northEastPoly, eastPoly, southEastPoly, southPoly, southWestPoly, westPoly, northWestPoly, frontPoly, backPoly]
# Definition of the color associated with each face of the cylinder
CylinderColor = ["green", "chartreuse", "darkgreen", "darkolivegreen", "darkseagreen", "teal", "forestgreen", "greenyellow", "lawngreen", "limegreen"]

# Definition of the Cylinder's underlying point cloud.  No structure, just the points.
CylinderPointCloud = [front1, front2, front3, front4, front5, front6, front7, front8, back1, back2, back3, back4, back5, back6, back7, back8]
DefaultCylinderPointCloud = copy.deepcopy(CylinderPointCloud)

# ****************************** Initialize Scene Object ****************************
# The Scene class is particularly useful for keeping track of the currently selected object.
# Scene now keeps track of current rendering mode.
# Scene also keeps track of Kd, Ks, specIndex, Ia, Ip, L, and V
class Scene:
    def __init__(self, Objects, ObjectColors, CurrentObject, CurrentPointCloud, CurrentMode, Kd, Ks, specIndex, Ia, Ip, L, V):
        self.Objects = Objects
        self.CurrentObject = CurrentObject
        self.ObjectColors = ObjectColors
        self.CurrentPointCloud = CurrentPointCloud
        self.CurrentMode = CurrentMode
        self.Kd = Kd
        self.Ks = Ks
        self.specIndex = specIndex
        self.Ia = Ia
        self.Ip = Ip
        self.L = L
        self.V = V

# The Pyramid is the default selected object, and mode 1 is the current mode.
# Old multi-object scenes
#myScene = Scene([Cube1, Pyramid, Cube2], [Cube1Color, PyramidColor, Cube2Color], Pyramid, PyramidPointCloud, 1)
#myScene = Scene([Cube1, Pyramid, Cube2, Cylinder], [Cube1Color, PyramidColor, Cube2Color, CylinderColor], Pyramid, PyramidPointCloud, 1)
#myScene = Scene([Pyramid], [PyramidColor], Pyramid, PyramidPointCloud, 1)

# New scene, only the cylinder
myScene = Scene([Cylinder], [CylinderColor], Cylinder, CylinderPointCloud, 1, 0.6, 0.9, 16, .3, .5, [1,1,-1], [0,0,-1])

# ************************************ Reset ****************************************
# This function resets the pyramid to its original size and location in 3D space
# Note that you have to be careful to update the values in the existing PyramidPointCloud
# structure rather than creating a new structure or just switching a pointer.  In other
# words, you'll need manually update the value of every x, y, and z of every point in
# point cloud (vertex list).
# Reset function itself is unchanged, but now resets individual objects based on the currently
# selected object.
def resetObject(pointcloud):
    if(pointcloud == PyramidPointCloud):
        for i in range(len(PyramidPointCloud)):
            for j in range(3):
                PyramidPointCloud[i][j] = DefaultPyramidPointCloud[i][j]
    elif(pointcloud == Cube1PointCloud):
        for i in range(len(Cube1PointCloud)):
            for j in range(3):
                Cube1PointCloud[i][j] = DefaultCube1PointCloud[i][j]
    elif(pointcloud == Cube2PointCloud):
        for i in range(len(Cube2PointCloud)):
            for j in range(3):
                Cube2PointCloud[i][j] = DefaultCube2PointCloud[i][j]
    else:
        for i in range(len(CylinderPointCloud)):
            for j in range(3):
                CylinderPointCloud[i][j] = DefaultCylinderPointCloud[i][j]

# ************************************ Reset zBuffer ****************************************
# Resets the zBuffer back to its initial state.
# This is done before EVERY draw.
def resetzBuffer():
    for i in range(len(zBuffer)):
        for j in range(CanvasHeight):
            zBuffer[i][j] = DefaultzBuffer[i][j]

# ********************************* Translation *************************************
# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.
# Translation function uses calculations found on page 23 of the notes.
# Receives an object and shifts its position by a given amount in a certain direction.
def translate(object, displacement):
    # For loops cycle through each of the object's points, and the dimensions of each point.
    # This is seen in the resetPyramid() function provided to us.
    for i in range(len(object)):
        for j in range(3):
            # Original Formula: New Position = Current Dimension's Location + Translation Distance
            # Shifts each of the relevant dimensions of each point by the given amount.
            object[i][j] = object[i][j] + displacement[j] 

# *********************************** Scaling **************************************
# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.
# Original Scaling function uses calculations found on page 23 of the notes.
# In Place Scaling function uses calculations found on page 26-27 of the notes.
# Scales a given object to be larger or smaller in size.
def scale(object,scalefactor):
    # Retrieves the references.
    references = getReferences(object)
    # For loops cycle through each of the object's points, and the dimensions of each point.
    # This is seen in the resetPyramid() function provided to us.
    for i in range(len(object)):
        for j in range(3):
            # Original Formula: New Position = (Current Dimension's Location - Reference) * Scale Factor + Reference
            # Moves to origin, adjusts scale for each of the relevant dimensions of each point by the given amount,
            # and then moves back to reference.
            object[i][j] = ((object[i][j] - references[j]) * scalefactor) + references[j]

# ********************************* Rotate Z *************************************
# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard postion]
# Rotation function uses calculations found on page 23 of the notes.
# In Place Rotation function uses calculations found on page 27 of the notes.
# Rotates a given object about the Z-axis by a given amount of degrees.
def rotateZ(object,degrees):
    # Retrieves the references.
    references = getReferences(object)
    # Converts degrees given to radians (Degrees * pi / 180).
    # Radians are required for the trigonometry functions in the math library.
    radians = degrees * math.pi / 180
    # For loop cycles through each of the object's points, and then sets the dimensions of each point.
    # This is seen in the original resetPyramid() function provided to us.
    for i in range(len(object)):
        # The "new" variables store the updated positions, to decouple them from the calculations still being made.
        # Moves the X point to the origin before making calculations.
        # Original Formula: X * cos(angle) - Y * sin(angle)
        # Adjusts the X position in a Z-axis rotation.
        newX = (object[i][0] - references[0]) * math.cos(radians) - (object[i][1] - references[1]) * math.sin(radians)
        # Moves the Y point to the origin before making calculations.
        # Original Formula: X * sin(angle) + Y * cos(angle)
        # Adjusts the Y position in a Z-axis rotation.
        newY = (object[i][0] - references[0]) * math.sin(radians) + (object[i][1] - references[1]) * math.cos(radians)
        # Moves the Z point to the origin before making calculations.
        # Original Formula: Z
        # Adjusts the Z position in a Z-axis rotation, which experiences no change.
        newZ = object[i][2] - references[2]
        # All dimensions are updated at the same time, after the calculations have been made.
        # This is done to avoid dimensions shifting mid calculation.
        # Points are moved back according to their reference.
        # This is done for every point.
        object[i][0] = newX + references[0]
        object[i][1] = newY + references[1]
        object[i][2] = newZ + references[2]

# ********************************* Rotate Y *************************************
# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.
# Rotation function uses calculations found on page 23 of the notes.
# In Place Rotation function uses calculations found on page 27 of the notes.
# Rotates a given object about the Y-axis by a given amount of degrees.
def rotateY(object,degrees):
    # Retrieves the references.
    references = getReferences(object)
    # Converts degrees given to radians (Degrees * pi / 180).
    # Radians are required for the trigonometry functions in the math library.
    radians = degrees * math.pi / 180
    # For loop cycles through each of the object's points, and then sets the dimensions of each point.
    # This is seen in the original resetPyramid() function provided to us.
    for i in range(len(object)):
        # The "new" variables store the updated positions, to decouple them from the calculations still being made.
        # Moves the X point to the origin before making calculations.
        # Original Formula: X * cos(angle) + Z * sin(angle)
        # Adjusts the X position in a Y-axis rotation.
        newX = (object[i][0] - references[0]) * math.cos(radians) + (object[i][2] - references[2]) * math.sin(radians)
        # Moves the Y point to the origin before making calculations.
        # Original Formula: Y
        # Adjusts the Y position in a Y-axis rotation, which experiences no change.
        newY = object[i][1] - references[1]
        # Moves the Z point to the origin before making calculations.
        # Original Formula: -X * sin(angle) + Z * cos(angle)
        # Adjusts the Z position in a Y-axis rotation.
        newZ = -(object[i][0] - references[0]) * math.sin(radians) + (object[i][2] - references[2]) * math.cos(radians)
        # All dimensions are updated at the same time, after the calculations have been made.
        # This is done to avoid dimensions shifting mid calculation.
        # Points are moved back according to their reference.
        # This is done for every point.
        object[i][0] = newX + references[0]
        object[i][1] = newY + references[1]
        object[i][2] = newZ + references[2]

# ********************************* Rotate X *************************************
# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.
# Rotation function uses calculations found on page 23 of the notes.
# In Place Rotation function uses calculations found on page 27 of the notes.
# Rotates a given object about the X-axis by a given amount of degrees.
def rotateX(object,degrees):
    # Retrieves the references.
    references = getReferences(object)
    # Converts degrees given to radians (Degrees * pi / 180).
    # Radians are required for the trigonometry functions in the math library.
    radians = degrees * math.pi / 180
    # For loop cycles through each of the object's points, and then sets the dimensions of each point.
    # This is seen in the original resetPyramid() function provided to us.
    for i in range(len(object)):
        # The "new" variables store the updated positions, to decouple them from the calculations still being made.
        # Moves the X point to the origin before making calculations.
        # Original Formula: X
        # Adjusts the X position in an X-axis rotation, which experiences no change.
        newX = object[i][0] - references[0]
        # Moves the Y point to the origin before making calculations.
        # Original Formula: Y * cos(angle) - Z * sin(angle)
        # Adjusts the Y position in an X-axis rotation.
        newY = (object[i][1] - references[1]) * math.cos(radians) - (object[i][2] - references[2]) * math.sin(radians)
        # Moves the Z point to the origin before making calculations.
        # Original Formula: Y * sin(angle) + Z * cos(angle)
        # Adjusts the Z position in an X-axis rotation.
        newZ = (object[i][1] - references[1]) * math.sin(radians) + (object[i][2] - references[2]) * math.cos(radians)
        # All dimensions are updated at the same time, after the calculations have been made.
        # This is done to avoid dimensions shifting mid calculation.
        # Points are moved back according to their reference.
        # This is done for every point.
        object[i][0] = newX + references[0]
        object[i][1] = newY + references[1]
        object[i][2] = newZ + references[2]

# ****************************** Get References *********************************
# This function calculates the references, to be used in scaling and rotating.
# These calculations can be found in page 28 of the notes.
def getReferences(object):
    # Retrieves minimums and maximums
    minimums, maximums = getMinAndMax(object)
    references = []
    # Original Formula: (Xmin + Xmax) / 2
    # Establishes the X Reference
    references.insert(0, (minimums[0]+maximums[0])/2)
    # Original Formula: (Ymin + Ymax) / 2
    # Establishes the Y Reference
    references.insert(1, (minimums[1]+maximums[1])/2)
    # Original Formula: (Zmin + Zmax) / 2
    # Establishes the Z Reference
    references.insert(2, (minimums[2]+maximums[2])/2)
    return references

# ******************************* Get Minimums **********************************
# This function retrieves the minimums and maximums of each object and orders them by dimension.
# This is used to create the references.
def getMinAndMax(object):
    minimums = []
    maximums = []
    xVal = []
    yVal = []
    zVal = []
    for i in range(len(object)):
        xVal.insert(i, object[i][0])
        yVal.insert(i, object[i][1])
        zVal.insert(i, object[i][2])
    minimums.insert(0, min(xVal))
    minimums.insert(1, min(yVal))
    minimums.insert(2, min(zVal))
    maximums.insert(0, max(xVal))
    maximums.insert(1, max(yVal))
    maximums.insert(2, max(zVal))
    return minimums, maximums

# ***************************** Check Visibility ********************************
# Simple function for checking visibility
# Returns true if vector normalization is greater than 0, false otherwise.
def isVisible(poly):
    Norm = normalizePoly(poly)
    Dvalue = Norm[0] * poly[0][0] + Norm[1] * poly[0][1] + Norm[2] * poly[0][2]
    Nnorm = Norm[0] * 0 + Norm[1] * 0 + Norm[2] * -(d) - (Dvalue)
    if Nnorm > 0:
        return True
    else:
        return False

# ***************************** Normalize Poly **********************************
# Poly normalization calculations
# Formulas on page 53 of notes.
def normalizePoly(poly):
    Px = poly[1][0] - poly[0][0]
    Py = poly[1][1] - poly[0][1]
    Pz = poly[1][2] - poly[0][2]
    Qx = poly[2][0] - poly[0][0]
    Qy = poly[2][1] - poly[0][1]
    Qz = poly[2][2] - poly[0][2]
    Nx = (Py * Qz) - (Pz * Qy)
    Ny = (Pz * Qx) - (Px * Qz)
    Nz = (Px * Qy) - (Py * Qx)
    squaresum = (Nx) ** 2 + (Ny) ** 2 + (Nz) ** 2
    denominator = math.sqrt(squaresum)
    Normx = Nx/denominator
    Normy = Ny/denominator
    Normz = Nz/denominator
    Norm = [Normx,Normy,Normz]
    return Norm

# ************************ Normalize Single Vector ******************************
# Normalizes a single vector for reflections
# From the render20Spheres method
def normalizeVector(vector):
    sumOfSquares = 0
    for i in range(len(vector)):
        sumOfSquares += vector[i]**2
    magnitude = math.sqrt(sumOfSquares)
    vect = []
    for i in range(len(vector)):
        vect.append(vector[i]/magnitude)
    return vect

# ******************************** Draw Scene ***********************************
# This function draws all objects in the entire scene at once.
def drawScene(myScene):
    Scene = myScene.Objects
    CurrentObject = myScene.CurrentObject
    ObjectColors = myScene.ObjectColors
    Mode = myScene.CurrentMode
    for i in range(len(Scene)):
        # If the object being drawn is the currently selected object,
        # Draw it red to distinguish it as the currently selected object.
        if (Scene[i] == CurrentObject):
            drawObject(myScene, Scene[i], "red", ObjectColors[i], Mode)
        # Otherwise, paint it black.
        else:
            drawObject(myScene, Scene[i], "black", ObjectColors[i], Mode)

# ******************************* Draw Object ***********************************
# The function will draw an object by repeatedly callying drawPoly on each polygon in the object
def drawObject(myScene, object, linecolor, objectcolors,mode):
    normalpolys = []
    # For loop draws each polygon in a given object.
    #print(object)
    if (mode == 5 or mode == 6):
        # Calculates the normals for each vertex in the object by adding the surface normals of touching polygons together
        for i in range(8):
            # If on the first polygon, add with the 8th polygon and the next one.
            if (i == 0):
                first = normalizePoly(object[i])
                second = normalizePoly(object[7])
                combined1 = [first[0]+second[0], first[1]+second[1], first[2]+second[2]]
                third = normalizePoly(object[i+1])
                combined2 = [first[0]+third[0], first[1]+third[1], first[2]+third[2]]
                normalpolys.insert(i, [normalizeVector(combined1), normalizeVector(combined1), normalizeVector(combined2), normalizeVector(combined2)])
            # If on the eighth polygon, add with the previous polygon and the first one.
            elif (i == 7):
                first = normalizePoly(object[i])
                second = normalizePoly(object[i-1])
                combined1 = [first[0]+second[0], first[1]+second[1], first[2]+second[2]]
                third = normalizePoly(object[0])
                combined2 = [first[0]+third[0], first[1]+third[1], first[2]+third[2]]
                normalpolys.insert(i, [normalizeVector(combined1), normalizeVector(combined1), normalizeVector(combined2), normalizeVector(combined2)])
            # Otherwise, add with the previous polygon and the next one.
            else:
                first = normalizePoly(object[i])
                second = normalizePoly(object[i-1])
                combined1 = [first[0]+second[0], first[1]+second[1], first[2]+second[2]]
                third = normalizePoly(object[i+1])
                combined2 = [first[0]+third[0], first[1]+third[1], first[2]+third[2]]
                normalpolys.insert(i, [normalizeVector(combined1), normalizeVector(combined1), normalizeVector(combined2), normalizeVector(combined2)])
        # Establish normals for the front and back polygons (one surface normal)
        normalpolys.insert(8, normalizePoly(object[8]))
        normalpolys.insert(9, normalizePoly(object[9]))
    for i in range(len(object)):
        if(mode == 5 or mode == 6):
            drawPoly(myScene, object[i], linecolor, objectcolors[i], mode, normalpolys[i])
        else:
            drawPoly(myScene, object[i], linecolor, objectcolors[i], mode, 0)
        
# ******************************** Draw Poly ************************************
# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(myScene, poly, linecolor, polycolor, mode, normals):
    # If the poly is not visible, do not draw it.
    if isVisible(poly) == False:
        return
    else:
        ps = []
        # Convert poly to display coordinates
        for i in range(len(poly)):
            displayPoly = convertToDisplayCoordinates(project(poly[i]))
            ps.insert(i, displayPoly)
        # RENDERING MODE 1: WIREFRAMES
        if (mode == 1):
            for i in range(len(ps)):
                if i < (len(ps) - 1):
                    # Conversions are handled here before being passed on to the drawLine() function.
                    # Points are first converted to 2D points, before being converted to Display Coordinates.
                    # A line is drawn from the current point to the next point.
                    drawLine(ps[i], ps[i+1], linecolor)
                else:
                    # On the last point, draws a line from the last point back to the first point.
                    drawLine(ps[i], ps[0], linecolor)
                    
        # RENDERING MODE 2: WIREFRAMES AND POLYGON FILL
        elif (mode == 2):
            # Generate edge table and sort by Y
            edges = createEdgeTable(ps)
            edges = sortbyY(edges)
            # Call fill poly function
            fillPoly(edges, polycolor)
            for i in range(len(ps)):
                if i < (len(ps) - 1):
                    # Conversions are handled here before being passed on to the drawLine() function.
                    # Points are first converted to 2D points, before being converted to Display Coordinates.
                    # A line is drawn from the current point to the next point.
                    drawLine(ps[i], ps[i+1], linecolor)
                else:
                    # On the last point, draws a line from the last point back to the first point.
                    drawLine(ps[i], ps[0], linecolor)
                    
        # RENDERING MODE 3: POLYGON FILL
        elif (mode == 3):
            # Generate edge table and sort by Y
            edges = createEdgeTable(ps)
            edges = sortbyY(edges)
            # Call fill poly function
            fillPoly(edges, polycolor)

        # RENDERING MODE 4: FLAT SHADING
        elif (mode == 4):
            # Initialize variables for illumination model
            Kd = myScene.Kd
            Ks = myScene.Ks
            specIndex = myScene.specIndex
            Ia = myScene.Ia
            Ip = myScene.Ip
            L = myScene.L
            V = myScene.V
            L = normalizeVector(L)
            V = normalizeVector(V)
            ambient = Ia*Kd
            # Normalize the whole poly, and use it to calculate a single color for the whole polygon
            N = normalizePoly(poly)
            NdotL = N[0]*L[0] + N[1]*L[1] + N[2]*L[2]
            if NdotL < 0:
                NdotL = 0
            diffuse = Ip * Kd * NdotL
            R = reflect(N,L)
            RdotV = R[0]*V[0] + R[1]*V[1] + R[2]*V[2]
            if RdotV < 0:
                RdotV = 0
            specular = Ip*Ks*RdotV**specIndex
            # Calculate the color using ambient, diffuse, and specular
            color = triColorHexCode(ambient,diffuse,specular)
            edges = createEdgeTable(ps)
            edges = sortbyY(edges)
            # Use the normal fillPoly method with the newly calculated color
            fillPoly(edges, color)

        # RENDERING MODE 5: GOURAUD SHADING
        elif (mode == 5):
            # Initialize variables for illumination model
            Kd = myScene.Kd
            Ks = myScene.Ks
            specIndex = myScene.specIndex
            Ia = myScene.Ia
            Ip = myScene.Ip
            L = myScene.L
            V = myScene.V
            L = normalizeVector(L)
            V = normalizeVector(V)
            ambient = Ia*Kd
            diffuses = []
            speculars = []
            # Calculate the diffuse and specular values for each of the normalized vertices
            for i in range(len(poly)):
                # Catches if drawing the front or back polys that only have one normal
                if len(normals) < 4:
                    N = normals
                else:
                    N = normals[i]
                NdotL = N[0]*L[0] + N[1]*L[1] + N[2]*L[2]
                if NdotL < 0:
                    NdotL = 0
                diffuse = Ip * Kd * NdotL
                diffuses.insert(i, diffuse)
                R = reflect(N,L)
                RdotV = R[0]*V[0] + R[1]*V[1] + R[2]*V[2]
                if RdotV < 0:
                    RdotV = 0
                specular = Ip*Ks*RdotV**specIndex
                speculars.insert(i, specular)
            # Generate edge table (now with starting and change in diffuse and specular values) and sort by Y
            edges = createEdgeTableWithIntensity(ps, diffuses, speculars)
            edges = sortbyY(edges)
            # Call new gouraud function (very similar to fillPoly, but now updates diffuses and specular for each point)
            gouraud(edges, ambient)

        # RENDERING MODE 6: PHONG SHADING
        else:
            # Initialize variables for illumination model
            Kd = myScene.Kd
            Ks = myScene.Ks
            specIndex = myScene.specIndex
            Ia = myScene.Ia
            Ip = myScene.Ip
            L = myScene.L
            V = myScene.V
            L = normalizeVector(L)
            V = normalizeVector(V)
            ambient = Ia*Kd
            # Catches if drawing the front or back polys that only have one normal
            if len(normals) < 4:
                normals = [normals, normals, normals, normals, normals, normals, normals, normals]
            # Generate edge table (now with starting and change in normalized coordinate values) and sort by Y
            edges = createEdgeTableWithNormal(ps, normals)
            edges = sortbyY(edges)
            # Call new phong function (very similar to gouraud, but now updates normal X, Y, and Z for each point)
            phong(edges, Kd, Ks, specIndex, Ia, Ip, L, V, ambient)
                

# ******************************** Fill Poly ************************************
# Fills a given polygon with a given color based on the edges defined in its edge table.
# Unchanged from Assignment 3.
def fillPoly(edges, polycolor):
    # Stubs for displaying Edge Table
    #print("-----------------------------------------------------")
    #for i in range(len(edges)):
        #print("Xstart: " + str(edges[i][0]) + " Ystart: " + str(edges[i][1]) + " Yend: " +str(edges[i][2]) + " dX: " + str(edges[i][3]) + " Zstart: " + str(edges[i][4]) + " dZ: " + str(edges[i][5]))
    last = (len(edges)-1)
    # Instructions on pages 65/73 of the notes.
    if (len(edges) >= 2):
        FirstFillLine = edges[0][1]
        LastFillLine = edges[last][2]
        i = 0
        j = 1
        n = 2
        EdgeIX = edges[i][0]
        EdgeJX = edges[j][0]
        EdgeIZ = edges[i][4]
        EdgeJZ = edges[j][4]
        currY = FirstFillLine
        while currY < LastFillLine:
            if EdgeIX <= EdgeJX:
                LeftX = EdgeIX
                RightX = EdgeJX
                LeftZ = EdgeIZ
                RightZ = EdgeJZ
            else:
                LeftX = EdgeJX
                RightX = EdgeIX
                LeftZ = EdgeJZ
                RightZ = EdgeIZ
            currX = LeftX
            currZ = LeftZ
            
            if (RightX-LeftX != 0):
                dZFillLine = (RightZ - LeftZ)/(RightX-LeftX)
            else:
                dZFillLine = 0
                
            while currX < RightX:
                if (currZ < zBuffer[round(currX)][round(currY)]):
                    w.create_line(round(currX),round(currY),round(currX+1),round(currY),fill=polycolor)
                    zBuffer[round(currX)][round(currY)] = currZ
                currZ = currZ + dZFillLine
                currX+=1
            EdgeIX = EdgeIX + edges[i][3]
            EdgeJX = EdgeJX + edges[j][3]
            EdgeIZ = EdgeIZ + edges[i][5]
            EdgeJZ = EdgeJZ + edges[j][5]
            currY+=1
            if (currY >= edges[i][2]) and (currY < LastFillLine):
                i = n
                EdgeIX = edges[i][0]
                EdgeIZ = edges[i][4]
                n += 1
            if (currY >= edges[j][2]) and (currY < LastFillLine):
                j = n
                EdgeJX = edges[j][0]
                EdgeJZ = edges[j][4]
                n += 1

# ***************************** Gouraud Shading *********************************
# New Gouraud Shading. Similar to fillPoly, but edge table includes start, end, and change values for diffuse and specular
# Also is passed through ambient light which is static
def gouraud(edges, ambient):
    # Stubs for displaying Edge Table
    #print("-----------------------------------------------------")
    #for i in range(len(edges)):
        #print("Xstart: " + str(edges[i][0]) + " Ystart: " + str(edges[i][1]) + " Yend: " +str(edges[i][2]) + " dX: " + str(edges[i][3]) + " Zstart: " + str(edges[i][4]) + " dZ: " + str(edges[i][5]))
    last = (len(edges)-1)
    # Instructions on pages 65/73 of the notes.
    if (len(edges) >= 2):
        FirstFillLine = edges[0][1]
        LastFillLine = edges[last][2]
        i = 0
        j = 1
        n = 2
        EdgeIX = edges[i][0]
        EdgeJX = edges[j][0]
        EdgeIZ = edges[i][4]
        EdgeJZ = edges[j][4]
        # Need to keep track of the left and right diffuse and specular
        EdgeID = edges[i][6]
        EdgeJD = edges[j][6]
        EdgeIS = edges[i][8]
        EdgeJS = edges[j][8]
        currY = FirstFillLine
        while currY < LastFillLine:
            if EdgeIX <= EdgeJX:
                LeftX = EdgeIX
                RightX = EdgeJX
                LeftZ = EdgeIZ
                RightZ = EdgeJZ
                LeftD = EdgeID
                RightD = EdgeJD
                LeftS = EdgeIS
                RightS = EdgeJS
            else:
                LeftX = EdgeJX
                RightX = EdgeIX
                LeftZ = EdgeJZ
                RightZ = EdgeIZ
                LeftD = EdgeJD
                RightD = EdgeID
                LeftS = EdgeJS
                RightS = EdgeIS
            currX = LeftX
            currZ = LeftZ
            currD = LeftD
            currS = LeftS
            
            
            if (RightX-LeftX != 0):
                # Interpolate diffuse and specular
                dZFillLine = (RightZ - LeftZ)/(RightX-LeftX)
                dDFillLine = (RightD - LeftD)/(RightX-LeftX)
                dSFillLine = (RightS - LeftS)/(RightX-LeftX)
            else:
                dZFillLine = 0
                dDFillLine = 0
                dSFillLine = 0
                
            while currX < RightX:
                if (currZ < zBuffer[round(currX)][round(currY)]):
                    # Create the color using the constant ambient light added with the current diffuse and specular lighting
                    color = triColorHexCode(ambient, currD, currS)
                    w.create_line(round(currX),round(currY),round(currX+1),round(currY),fill=color)
                    zBuffer[round(currX)][round(currY)] = currZ
                currZ = currZ + dZFillLine
                currD = currD + dDFillLine
                currS = currS + dSFillLine
                currX+=1
            EdgeIX = EdgeIX + edges[i][3]
            EdgeJX = EdgeJX + edges[j][3]
            EdgeIZ = EdgeIZ + edges[i][5]
            EdgeJZ = EdgeJZ + edges[j][5]
            EdgeID = EdgeID + edges[i][7]
            EdgeJD = EdgeJD + edges[j][7]
            EdgeIS = EdgeIS + edges[i][9]
            EdgeJS = EdgeJS + edges[j][9]
            currY+=1
            if (currY >= edges[i][2]) and (currY < LastFillLine):
                i = n
                EdgeIX = edges[i][0]
                EdgeIZ = edges[i][4]
                EdgeID = edges[i][6]
                EdgeIS = edges[i][8]
                n += 1
            if (currY >= edges[j][2]) and (currY < LastFillLine):
                j = n
                EdgeJX = edges[j][0]
                EdgeJZ = edges[j][4]
                EdgeJD = edges[j][6]
                EdgeJS = edges[j][8]
                n += 1

# ******************************* Phong Shading *********************************
# New Phong Shading. Similar to gouraud, but edge table includes start, end, and change values for the Normalized X, Y, and Z instead of diffuse and specular
# Also is passed through all illumination variables necessary for each individual color calculation
def phong(edges, Kd, Ks, specIndex, Ia, Ip, L, V, ambient):
    # Stubs for displaying Edge Table
    #print("-----------------------------------------------------")
    #for i in range(len(edges)):
        #print("Xstart: " + str(edges[i][0]) + " Ystart: " + str(edges[i][1]) + " Yend: " +str(edges[i][2]) + " dX: " + str(edges[i][3]) + " Zstart: " + str(edges[i][4]) + " dZ: " + str(edges[i][5]))
    last = (len(edges)-1)
    # Instructions on pages 65/73 of the notes.
    if (len(edges) >= 2):
        FirstFillLine = edges[0][1]
        LastFillLine = edges[last][2]
        i = 0
        j = 1
        n = 2
        EdgeIX = edges[i][0]
        EdgeJX = edges[j][0]
        EdgeIZ = edges[i][4]
        EdgeJZ = edges[j][4]
        # Need to keep track of the left and right Norm X, Y, and Z
        EdgeINX = edges[i][6]
        EdgeINY = edges[i][8]
        EdgeINZ = edges[i][10]
        EdgeJNX = edges[j][6]
        EdgeJNY = edges[j][8]
        EdgeJNZ = edges[j][10]
        currY = FirstFillLine
        while currY < LastFillLine:
            if EdgeIX <= EdgeJX:
                LeftX = EdgeIX
                RightX = EdgeJX
                LeftZ = EdgeIZ
                RightZ = EdgeJZ
                LeftNX = EdgeINX
                LeftNY = EdgeINY
                LeftNZ = EdgeINZ
                RightNX = EdgeJNX
                RightNY = EdgeJNY
                RightNZ = EdgeJNZ
            else:
                LeftX = EdgeJX
                RightX = EdgeIX
                LeftZ = EdgeJZ
                RightZ = EdgeIZ
                LeftNX = EdgeJNX
                LeftNY = EdgeJNY
                LeftNZ = EdgeJNZ
                RightNX = EdgeINX
                RightNY = EdgeINY
                RightNZ = EdgeINZ
            currX = LeftX
            currZ = LeftZ
            currNX = LeftNX
            currNY = LeftNY
            currNZ = LeftNZ
            
            if (RightX-LeftX != 0):
                dZFillLine = (RightZ - LeftZ)/(RightX-LeftX)
                # Interpolate X, Y, and Z
                dNXFillLine = (RightNX - LeftNX)/(RightX-LeftX)
                dNYFillLine = (RightNY - LeftNY)/(RightX-LeftX)
                dNZFillLine = (RightNZ - LeftNZ)/(RightX-LeftX)
            else:
                dZFillLine = 0
                dNXFillLine = 0
                dNYFillLine = 0
                dNZFillLine = 0
                
            while currX < RightX:
                if (currZ < zBuffer[round(currX)][round(currY)]):
                    # Need to calculate illumination for every single point
                    N = [currNX,currNY,currNZ]
                    NdotL = N[0]*L[0] + N[1]*L[1] + N[2]*L[2]
                    if NdotL < 0:
                        NdotL = 0
                    diffuse = Ip * Kd * NdotL
                    R = reflect(N,L)
                    RdotV = R[0]*V[0] + R[1]*V[1] + R[2]*V[2]
                    if RdotV < 0:
                        RdotV = 0
                    specular = Ip*Ks*RdotV**specIndex
                    color = triColorHexCode(ambient,diffuse,specular)
                    w.create_line(round(currX),round(currY),round(currX+1),round(currY),fill=color)
                    zBuffer[round(currX)][round(currY)] = currZ
                currZ = currZ + dZFillLine
                currNX = currNX + dNXFillLine
                currNY = currNY + dNYFillLine
                currNZ = currNZ + dNZFillLine
                currX+=1
            EdgeIX = EdgeIX + edges[i][3]
            EdgeJX = EdgeJX + edges[j][3]
            EdgeIZ = EdgeIZ + edges[i][5]
            EdgeJZ = EdgeJZ + edges[j][5]
            EdgeINX = EdgeINX + edges[i][7]
            EdgeINY = EdgeINY + edges[i][9]
            EdgeINZ = EdgeINZ + edges[i][11]
            EdgeJNX = EdgeJNX + edges[j][7]
            EdgeJNY = EdgeJNY + edges[j][9]
            EdgeJNZ = EdgeJNZ + edges[j][11]
            currY+=1
            if (currY >= edges[i][2]) and (currY < LastFillLine):
                i = n
                EdgeIX = edges[i][0]
                EdgeIZ = edges[i][4]
                EdgeINX = edges[i][6]
                EdgeINY = edges[i][8]
                EdgeINZ = edges[i][10]
                n += 1
            if (currY >= edges[j][2]) and (currY < LastFillLine):
                j = n
                EdgeJX = edges[j][0]
                EdgeJZ = edges[j][4]
                EdgeJNX = edges[j][6]
                EdgeJNY = edges[j][8]
                EdgeJNZ = edges[j][10]
                n += 1

# ******************************** Sort by Y ************************************
# Sorts a given table ascending by its Y value.
# Used to keep edge tables in proper order for filling
def sortbyY(ps):
    i = 0
    j = 1
    end = len(ps)-1
    while i < end:
        if (ps[i][1] <= ps[j][1]):
            i+=1
            j+=1
        else:
            temp = ps[j]
            ps[j] = ps[i]
            ps[i] = temp
            i = 0
            j = 1
    return ps

# **************************** Create Edge Table ************************************
# Creates an Edge Table based on a set of display coordinate points.
def createEdgeTable(ps):
    edges = []
    # Edge Table formulas on page 63/71 of the notes
    for i in range(len(ps)):
        if i < (len(ps)-1):
            curr = ps[i]
            nextps = ps[i+1]
        else:
            curr = ps[i]
            nextps = ps[0]
        if ps[i][1] < nextps[1]:
            Xstart = curr[0]
            Xend = nextps[0]
            Ystart = curr[1]
            Yend = nextps[1]
            Zstart = curr[2]
            Zend = nextps[2]
            height = Yend - Ystart
            # Checks if pixel height is too small (avoids dividing by zero)
            if (abs(height) >= 1):
                dX = (Xend - Xstart)/(Yend - Ystart)
                dZ = (Zend - Zstart)/(Yend - Ystart)
                edges.insert(i, [Xstart, Ystart, Yend, dX, Zstart, dZ])
                
        # If the next point's y is smaller, flip variable assignment
        else:
            Xstart = nextps[0]
            Xend = curr[0]
            Ystart = nextps[1]
            Yend = curr[1]
            Zstart = nextps[2]
            Zend = curr[2]
            height = Yend - Ystart
            # Checks if pixel height is too small (avoids dividing by zero)
            if (abs(height) >= 1):
                dX = (Xend - Xstart)/(Yend - Ystart)
                dZ = (Zend - Zstart)/(Yend - Ystart)
                edges.insert(i, [Xstart, Ystart, Yend, dX, Zstart, dZ])
    return edges

# ********************** Create Edge Table With Intensity *************************
# Creates an Edge Table, but also includes starting, ending, and change values for diffuse and specular lighting for each edge
def createEdgeTableWithIntensity(ps, diffuses, speculars):
    edges = []
    # Edge Table formulas on page 63/71 of the notes
    for i in range(len(ps)):
        if i < (len(ps)-1):
            curr = ps[i]
            nextps = ps[i+1]
            currd = diffuses[i]
            nextd = diffuses[i+1]
            currs = speculars[i]
            nexts = speculars[i+1]
        else:
            curr = ps[i]
            nextps = ps[0]
            currd = diffuses[i]
            nextd = diffuses[0]
            currs = speculars[i]
            nexts = speculars[0]
        if ps[i][1] < nextps[1]:
            Xstart = curr[0]
            Xend = nextps[0]
            Ystart = curr[1]
            Yend = nextps[1]
            Zstart = curr[2]
            Zend = nextps[2]
            Dstart = currd
            Dend = nextd
            Sstart = currs
            Send = nexts
            height = Yend - Ystart
            # Checks if pixel height is too small (avoids dividing by zero)
            if (abs(height) >= 1):
                dX = (Xend - Xstart)/(Yend - Ystart)
                dZ = (Zend - Zstart)/(Yend - Ystart)
                dD = (Dend - Dstart)/(Yend - Ystart)
                dS = (Send - Sstart)/(Yend - Ystart)
                edges.insert(i, [Xstart, Ystart, Yend, dX, Zstart, dZ, Dstart, dD, Sstart, dS])
                
        # If the next point's y is smaller, flip variable assignment
        else:
            Xstart = nextps[0]
            Xend = curr[0]
            Ystart = nextps[1]
            Yend = curr[1]
            Zstart = nextps[2]
            Zend = curr[2]
            Dstart = nextd
            Dend = currd
            Sstart = nexts
            Send = currs
            height = Yend - Ystart
            # Checks if pixel height is too small (avoids dividing by zero)
            if (abs(height) >= 1):
                dX = (Xend - Xstart)/(Yend - Ystart)
                dZ = (Zend - Zstart)/(Yend - Ystart)
                dD = (Dend - Dstart)/(Yend - Ystart)
                dS = (Send - Sstart)/(Yend - Ystart)
                edges.insert(i, [Xstart, Ystart, Yend, dX, Zstart, dZ, Dstart, dD, Sstart, dS])
    return edges

# ********************** Create Edge Table With Normals *************************
# Creates an Edge Table, but also includes starting, ending, and change values for the Normalized X, Y, and Z values for each edge
def createEdgeTableWithNormal(ps, normals):
    edges = []
    # Edge Table formulas on page 63/71 of the notes
    for i in range(len(ps)):
        if i < (len(ps)-1):
            curr = ps[i]
            nextps = ps[i+1]
            currn = normals[i]
            nextn = normals[i+1]
        else:
            curr = ps[i]
            nextps = ps[0]
            currn = normals[i]
            nextn = normals[0]
        if ps[i][1] < nextps[1]:
            Xstart = curr[0]
            Xend = nextps[0]
            Ystart = curr[1]
            Yend = nextps[1]
            Zstart = curr[2]
            Zend = nextps[2]
            NXStart = currn[0]
            NXEnd = nextn[0]
            NYStart = currn[1]
            NYEnd = nextn[1]
            NZStart = currn[2]
            NZEnd = nextn[2]
            height = Yend - Ystart
            # Checks if pixel height is too small (avoids dividing by zero)
            if (abs(height) >= 1):
                dX = (Xend - Xstart)/(Yend - Ystart)
                dZ = (Zend - Zstart)/(Yend - Ystart)
                dNX = (NXEnd - NXStart)/(Yend-Ystart)
                dNY = (NYEnd - NYStart)/(Yend-Ystart)
                dNZ = (NZEnd - NZStart)/(Yend-Ystart)
                edges.insert(i, [Xstart, Ystart, Yend, dX, Zstart, dZ, NXStart, dNX, NYStart, dNY, NZStart, dNZ])
                
        # If the next point's y is smaller, flip variable assignment
        else:
            Xstart = nextps[0]
            Xend = curr[0]
            Ystart = nextps[1]
            Yend = curr[1]
            Zstart = nextps[2]
            Zend = curr[2]
            NXStart = nextn[0]
            NXEnd = currn[0]
            NYStart = nextn[1]
            NYEnd = currn[1]
            NZStart = nextn[2]
            NZEnd = currn[2]
            height = Yend - Ystart
            # Checks if pixel height is too small (avoids dividing by zero)
            if (abs(height) >= 1):
                dX = (Xend - Xstart)/(Yend - Ystart)
                dZ = (Zend - Zstart)/(Yend - Ystart)
                dNX = (NXEnd - NXStart)/(Yend-Ystart)
                dNY = (NYEnd - NYStart)/(Yend-Ystart)
                dNZ = (NZEnd - NZStart)/(Yend-Ystart)
                edges.insert(i, [Xstart, Ystart, Yend, dX, Zstart, dZ, NXStart, dNX, NYStart, dNY, NZStart, dNZ])
    return edges

# ******************************** Draw Line **************************************
# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
# Draws a line given a start and end point.
def drawLine(start,end,color):
    # Creates the line using tkinter given a start and end point with XY dimensions.
    # Conversions are already done and passed through from the drawPoly() function.
    # Also paints it either green or black if it is or is not the currently selected object.
    # Color is passed all the way down from drawScene.
    w.create_line(round(start[0]),round(start[1]),round(end[0]),round(end [1]), fill = color)

# ************************* Perspective Projection ******************************
# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
# Perspective Projection function uses calculations found on page 11 of the notes.
# Converts a 3D point to a 2D point.
def project(point):
    ps = []
    # Original Formula: Distance * X / (Distance + Z)
    # Converts the X dimension for the 2D point.
    ps.insert(0, (d * point[0] / (d + point[2])))
    # Original Formula: Distance * Y / (Distance + Z)
    # Converts the Y dimension for the 2D point.
    ps.insert(1, (d * point[1] / (d + point[2])))
    ps.insert(2, (d * point[2] / (d + point[2])))
    return ps

# *************************** Display Coordinates ******************************
# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.
# Display Coordinate function uses calculations found on page 13 of the notes.
# Converts a 2D point to a Display Coordinate.
def convertToDisplayCoordinates(point):
    displayXY = []
    # Original Formula: Window Width / 2 + X
    # Converts the X dimension for the display coordinate.
    displayXY.insert(0, (round(CanvasWidth / 2 + point[0])))
    # Original Formula: Window Height / 2 + Y
    # Converts the Y dimension for the display coordinate.
    displayXY.insert(1, (round(CanvasHeight / 2 - point[1])))
    displayXY.insert(2, point[2])
    return displayXY

# ******************************* Reflect *************************************
# From the render20Spheres method
def reflect(N,L):
    R = []
    N = normalizeVector(N)
    L = normalizeVector(L)
    twoCosPhi = 2 * (N[0]*L[0] + N[1]*L[1] + N[2]*L[2])
    if twoCosPhi > 0:
        for i in range(3):
            R.append(N[i] - (L[i] / twoCosPhi))

    elif twoCosPhi == 0:
        for i in range(3):
            R.append( - L[i])
            
    else:
        for i in range(3):
            R.append( - N[i] + (L[i] / twoCosPhi))
    return normalizeVector(R)

# ************************ TriColorHexCode *************************************
# From the render20Spheres method
def triColorHexCode(ambient, diffuse, specular):
    combinedColorCode = colorHexCode(ambient+diffuse+specular)
    specularColorCode = colorHexCode(specular)
    colorString = "#"+specularColorCode+combinedColorCode+specularColorCode
    return colorString

# ************************* ColorHexCode *************************************
def colorHexCode(intensity):
    hexString = str(hex(round(255*intensity)))
    if hexString[0] == "-":
        trimmedHexString = "00"
    else:
        trimmedHexString = hexString[2:]
        if len(trimmedHexString) == 1:
            trimmedHexString = "0"+trimmedHexString
    return trimmedHexString

# *****************************************************************************
# Everything below this point implements the interface
# The structure of these functions remains largely the same,
# but have been changed to account for the new objects and functions.
def reset():
    w.delete(ALL)
    resetObject(myScene.CurrentPointCloud)
    resetzBuffer()
    drawScene(myScene)

# Adjusted scale factor to make scaling more consistent.
def larger():
    w.delete(ALL)
    scale(myScene.CurrentPointCloud,1.25)
    resetzBuffer()
    drawScene(myScene)

# Adjusted scale factor to make scaling more consistent.
def smaller():
    w.delete(ALL)
    scale(myScene.CurrentPointCloud,.8)
    resetzBuffer()
    drawScene(myScene)

def forward():
    w.delete(ALL)
    translate(myScene.CurrentPointCloud,[0,0,5])
    resetzBuffer()
    drawScene(myScene)

def backward():
    w.delete(ALL)
    translate(myScene.CurrentPointCloud,[0,0,-5])
    resetzBuffer()
    drawScene(myScene)

def left():
    w.delete(ALL)
    translate(myScene.CurrentPointCloud,[-5,0,0])
    resetzBuffer()
    drawScene(myScene)

def right():
    w.delete(ALL)
    translate(myScene.CurrentPointCloud,[5,0,0])
    resetzBuffer()
    drawScene(myScene)

def up():
    w.delete(ALL)
    translate(myScene.CurrentPointCloud,[0,5,0])
    resetzBuffer()
    drawScene(myScene)

def down():
    w.delete(ALL)
    translate(myScene.CurrentPointCloud,[0,-5,0])
    resetzBuffer()
    drawScene(myScene)

def xPlus():
    w.delete(ALL)
    rotateX(myScene.CurrentPointCloud,5)
    resetzBuffer()
    drawScene(myScene)

def xMinus():
    w.delete(ALL)
    rotateX(myScene.CurrentPointCloud,-5)
    resetzBuffer()
    drawScene(myScene)

def yPlus():
    w.delete(ALL)
    rotateY(myScene.CurrentPointCloud,5)
    resetzBuffer()
    drawScene(myScene)

def yMinus():
    w.delete(ALL)
    rotateY(myScene.CurrentPointCloud,-5)
    resetzBuffer()
    drawScene(myScene)

def zPlus():
    w.delete(ALL)
    rotateZ(myScene.CurrentPointCloud,5)
    resetzBuffer()
    drawScene(myScene)

def zMinus():
    w.delete(ALL)
    rotateZ(myScene.CurrentPointCloud,-5)
    resetzBuffer()
    drawScene(myScene)

# Selection Functions
# Sets a new currently selected object and respective point cloud, before redrawing the scene.
def selectCube1():
    w.delete(ALL)
    myScene.CurrentObject = Cube1
    myScene.CurrentPointCloud = Cube1PointCloud
    resetzBuffer()
    drawScene(myScene)

def selectPyramid():
    w.delete(ALL)
    myScene.CurrentObject = Pyramid
    myScene.CurrentPointCloud = PyramidPointCloud
    resetzBuffer()
    drawScene(myScene)

def selectCube2():
    w.delete(ALL)
    myScene.CurrentObject = Cube2
    myScene.CurrentPointCloud = Cube2PointCloud
    resetzBuffer()
    drawScene(myScene)

def selectCylinder():
    w.delete(ALL)
    myScene.CurrentObject = Cylinder
    myScene.CurrentPointCloud = CylinderPointCloud
    resetzBuffer()
    drawScene(myScene)

# Change Render Mode
# Adjusts render mode based on key press
# 1 is just wireframe, 2 is fill and wireframe, 3 is just fill.
# 4 is flat shading, 5 is gouraud, and 6 is phong.
def changeMode(k):
    if k.char == '1':
        w.delete(ALL)
        myScene.CurrentMode = 1
        #print("Mode is 1.")
        resetzBuffer()
        drawScene(myScene)
    if k.char == '2':
        w.delete(ALL)
        myScene.CurrentMode = 2
        #print("Mode is 2.")
        resetzBuffer()
        drawScene(myScene)
    if k.char == '3':
        w.delete(ALL)
        myScene.CurrentMode = 3
        #print("Mode is 3.")
        resetzBuffer()
        drawScene(myScene)
    if k.char == '4':
        w.delete(ALL)
        myScene.CurrentMode = 4
        #print("Mode is 4.")
        resetzBuffer()
        drawScene(myScene)
    if k.char == '5':
        w.delete(ALL)
        myScene.CurrentMode = 5
        #print("Mode is 5.")
        resetzBuffer()
        drawScene(myScene)
    if k.char == '6':
        w.delete(ALL)
        myScene.CurrentMode = 6
        #print("Mode is 6.")
        resetzBuffer()
        drawScene(myScene)
    else:
        return

root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
resetzBuffer()
# Draws full scene
drawScene(myScene)
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

downButton = Button(translatecontrols, text="DN", command=down)
downButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

# Selection Controls
selectioncontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
selectioncontrols.pack(side=LEFT)

selectioncontrolslabel = Label(selectioncontrols, text="Selection")
selectioncontrolslabel.pack()

selectCube1Button = Button(selectioncontrols, text="C1", command=selectCube1)
selectCube1Button.pack(side=LEFT)

selectPyramidButton = Button(selectioncontrols, text="P", command=selectPyramid)
selectPyramidButton.pack(side=LEFT)

selectCube2Button = Button(selectioncontrols, text="C2", command=selectCube2)
selectCube2Button.pack(side=LEFT)

selectCylinderButton = Button(selectioncontrols, text="Cy", command=selectCylinder)
selectCylinderButton.pack(side=LEFT)

# Change Render Mode Binds
outerframe.bind("<KeyPress>", changeMode)
outerframe.focus_set()

root.mainloop()
