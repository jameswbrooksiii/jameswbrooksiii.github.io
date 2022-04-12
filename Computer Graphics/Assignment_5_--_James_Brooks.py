# ************************************************************************************
# James Brooks
# CSC 470-001
# Assignment 5
# February 25th, 2021
# ************************************************************************************

# ******** Import Required Libraries **********
import math
from tkinter import *

# ******************** Initialize Window *********************
# Initialize window width, height, and distance from the view.
canvasWidth = 400
canvasHeight = 400
d = 500
centerOfProjection = [0,0,-d]
lightSource = [500,500,0]
skyBoxColor = [.6, .8, .9]

# *********************************************************** Define Sphere ***********************************************************
# Define sphere class. Class requires the sphere's centerPoint, radius, localColor, Kd, Ks, specIndex, localWeight, and reflectedWeight
class sphere:
    def __init__(self, centerPoint, radius, localColor, Kd, Ks, specIndex, Ia, Ip, V, localWeight, reflectWeight):
        self.centerPoint = centerPoint
        self.radius = radius
        self.localColor = localColor
        self.Kd = Kd
        self.Ks = Ks
        self.specIndex = specIndex
        self.Ia = Ia
        self.Ip = Ip
        self.V = V
        self.localWeight = localWeight
        self.reflectWeight = reflectWeight

    # Checks for intersection with object given a startpoint and a ray
    def intersect(self, startPoint, ray):
        i = ray[0]
        j = ray[1]
        k = ray[2]
        l = self.centerPoint[0]
        m = self.centerPoint[1]
        n = self.centerPoint[2]
        r = self.radius
        X1 = startPoint[0]
        Y1 = startPoint[1]
        Z1 = startPoint[2]
        a = i**2 + j**2 + k**2
        b = 2*i*(X1-l) + 2*j*(Y1-m) + 2*k*(Z1-n)
        c = l**2 + m**2 + n**2 + X1**2 + Y1**2 + Z1**2 + 2*(-l*X1-m*Y1-n*Z1)-r**2
        discriminant = b**2-4*a*c
        if discriminant < 0:
            t = []
            intersectionPoint = []
            return t, intersectionPoint
        elif discriminant == 0:
            P = -b/(2*a)
            t = P
            X = X1 + i*t
            Y = Y1 + j*t
            Z = Z1 + k*t
            intersectionPoint = [X,Y,Z]
            return t
        else:
            P1 = (-b + math.sqrt(discriminant))/(2*a)
            P2 = (-b - math.sqrt(discriminant))/(2*a)
            if P2 < P1:
                t = P2
                X = X1 + i*t
                Y = Y1 + j*t
                Z = Z1 + k*t
                intersectionPoint = [X,Y,Z]
                return t, intersectionPoint
            else:
                t = P1
                X = X1 + i*t
                Y = Y1 + j*t
                Z = Z1 + k*t
                intersectionPoint = [X,Y,Z]
                return t, intersectionPoint

    # Reflect ray method for sphere
    def reflect(self,intersectionPoint, ray):
        N = computeUnitVector(self.centerPoint, intersectionPoint)
        R = []
        twoCosPhi = 2 * (N[0]*-ray[0] + N[1]*-ray[1] + N[2]*-ray[2])
        if twoCosPhi > 0:
            for i in range(3):
                R.append(N[i] + (ray[i] / twoCosPhi))

        elif twoCosPhi == 0:
            for i in range(3):
                R.append(ray[i])
                
        else:
            for i in range(3):
                R.append( - N[i] - (ray[i] / twoCosPhi))
        R = normalize(R)
        return R

    # Reflect light method for sphere
    def reflectLight(self, intersectionPoint, ray):
        N = computeUnitVector(self.centerPoint, intersectionPoint)
        R = []
        twoCosPhi = 2 * (N[0]*ray[0] + N[1]*ray[1] + N[2]*ray[2])
        if twoCosPhi > 0:
            for i in range(3):
                R.append(N[i] - (ray[i] / twoCosPhi))

        elif twoCosPhi == 0:
            for i in range(3):
                R.append( - ray[i])
                
        else:
            for i in range(3):
                R.append( - N[i] + (ray[i] / twoCosPhi))
        R = normalize(R)
        return R

    # Calculate intensity for sphere
    def phongIntensity(self, intersectionPoint, L):
        N = computeUnitVector(self.centerPoint, intersectionPoint)
        ambient = self.Ia*self.Kd
        NdotL = N[0]*L[0] + N[1]*L[1] + N[2]*L[2]
        if NdotL < 0:
            NdotL = 0
        diffuse = self.Ip * self.Kd * NdotL
        R = self.reflectLight(intersectionPoint,L)
        RdotV = R[0]*self.V[0] + R[1]*self.V[1] + R[2]*self.V[2]
        if RdotV < 0:
            RdotV = 0
        specular = self.Ip*self.Ks*RdotV**self.specIndex
        return ambient, diffuse, specular

    # Detect if current object is a plane
    def isPlane(self):
        return False

# ******************************************************** Define Checkerboard ********************************************************
# Define checkerboard class. Class requires the board's surfaceNormal, anchorPoint, Kd, Ks, specIndex, localWeight, and reflectedWeight
class checkerboard:
    def __init__(self, surfaceNormal, anchorPoint, Kd, Ks, specIndex, Ia, Ip, V, localWeight, reflectWeight):
        self.surfaceNormal = surfaceNormal
        self.anchorPoint = anchorPoint
        self.Kd = Kd
        self.Ks = Ks
        self.specIndex = specIndex
        self.Ia = Ia
        self.Ip = Ip
        self.V = V
        self.localWeight = localWeight
        self.reflectWeight = reflectWeight

    # Checks for intersection with object given a startpoint and a ray
    def intersect(self, startPoint, ray):
        i = ray[0]
        j = ray[1]
        k = ray[2]
        A = self.surfaceNormal[0]
        B = self.surfaceNormal[1]
        C = self.surfaceNormal[2]
        a = self.anchorPoint[0]
        b = self.anchorPoint[1]
        c = self.anchorPoint[2]
        X1 = startPoint[0]
        Y1 = startPoint[1]
        Z1 = startPoint[2]
        D = A*a+B*b+C*c
        denominator = A*i + B*j + C*k
        if denominator <= 0:
            t = []
            intersectionPoint = []
            return t, intersectionPoint
        else:
            t = -(A*X1 + B*Y1 + C*Z1 - D)/denominator
            X = X1 + i*t
            Y = Y1 + j*t
            Z = Z1 + k*t
            intersectionPoint = [X,Y,Z]
            return t, intersectionPoint

    # Reflect ray method for plane
    def reflect(self, intersectionPoint, ray):
        N = self.surfaceNormal
        R = []
        twoCosPhi = 2 * (N[0]*-ray[0] + N[1]*-ray[1] + N[2]*-ray[2])
        if twoCosPhi > 0:
            for i in range(3):
                R.append(N[i] + (ray[i] / twoCosPhi))

        elif twoCosPhi == 0:
            for i in range(3):
                R.append(ray[i])
                
        else:
            for i in range(3):
                R.append( - N[i] - (ray[i] / twoCosPhi))
        R = normalize(R)
        return R

    # Reflect light method for plane
    def reflectLight(self, intersectionPoint, ray):
        N = self.surfaceNormal
        R = []
        twoCosPhi = 2 * (N[0]*ray[0] + N[1]*ray[1] + N[2]*ray[2])
        if twoCosPhi > 0:
            for i in range(3):
                R.append(N[i] - (ray[i] / twoCosPhi))

        elif twoCosPhi == 0:
            for i in range(3):
                R.append( - ray[i])
                
        else:
            for i in range(3):
                R.append( - N[i] + (ray[i] / twoCosPhi))
        R = normalize(R)
        return R

    # Calculate intensity for plane
    def phongIntensity(self, intersectionPoint, L):
        N = self.surfaceNormal
        ambient = self.Ia*self.Kd
        NdotL = N[0]*L[0] + N[1]*L[1] + N[2]*L[2]
        if NdotL < 0:
            NdotL = 0
        diffuse = self.Ip * self.Kd * NdotL
        R = self.reflectLight(intersectionPoint,L)
        RdotV = R[0]*self.V[0] + R[1]*self.V[1] + R[2]*self.V[2]
        if RdotV < 0:
            RdotV = 0
        specular = self.Ip*self.Ks*RdotV**self.specIndex
        return ambient, diffuse, specular

    # Detect if the current object is a plane
    def isPlane(self):
        return True

# *********************************************** Initialize Spheres ***********************************************
# Initialize three spheres with centerPoint, radius, localColor, Kd, Ks, specIndex, Ia, Ip, V, localWeight, and reflectedWeight
redSphere = sphere([300,-100,800], 200, [1,0.5,0.5], 0.5, 0.5, 8, .3, .5, [0,0,-1], .5, .5)
greenSphere = sphere([-300,-200,1000], 100, [0.5,1,0.5], 0.5, 0.5, 8, .3, .5, [0,0,-1], .5, .5)
blueSphere = sphere([0,0,1500], 300, [0.5,0.5,1], 0.5, 0.5, 8, .3, .5, [0,0,-1], .5, .5)

# ************ Initialize Board *************
# Initialize the board underneath the spheres
board = checkerboard([0,-1,0], [0,-300,0], 0.6, 0.4, 8, .3, .5, [0,0,-1], 0.005, 0.6)

# ************* Initialize Scene List*****************
# Initializes the scene list that contains all objects
scene = [redSphere, greenSphere, blueSphere, board]
#scene = [redSphere, greenSphere, blueSphere]

# ************* Compute Unit Vector **************
# Returns a normalized unit vector from two points
def computeUnitVector(start, end):
    return normalize([end[0]-start[0], end[1]-start[1], end[2]-start[2]])

# ******** Normalize Single Vector *********
# Normalizes a single vector for reflections
# From the render20Spheres method
def normalize(vector):
    sumOfSquares = 0
    for i in range(len(vector)):
        sumOfSquares += vector[i]**2
    magnitude = math.sqrt(sumOfSquares)
    vect = []
    for i in range(len(vector)):
        vect.append(vector[i]/magnitude)
    return vect

# ************* Trace Ray Method *******************
def traceRay(startPoint, ray, depth):
    # Return “black” when you reach the bottom of the recursive calls

    if depth == 0:
        returnColor = [0,0,0]
        return returnColor
    # Intersect ray with all objects and find closest intersection point
    tMin = 999999
    for object in scene:
        t, intersectionPoint = object.intersect(startPoint, ray)
        if t != []:
            if t > 0.001:
                if t < tMin:
                    tMin = t
                    nearestObject = object
                    nearestIntersectionPoint = intersectionPoint
    # If the ray doesn’t hit anything, let color equal “sky box” color
    if tMin == 999999:
        returnColor = skyBoxColor
        return returnColor
    # Make the behind of the plane finite (better shows curve in reflection)
    if nearestIntersectionPoint[2] <= 0:
        returnColor = skyBoxColor
        return returnColor
    # Calculate light ray and intensity
    lightRay = computeUnitVector(nearestIntersectionPoint, lightSource)
    ambient, diffuse, specular = nearestObject.phongIntensity(nearestIntersectionPoint, lightRay)
    # Check if in shadow
    if inShadow(nearestObject, nearestIntersectionPoint) == True:
        intensity = ambient
        #intensity = ambient+diffuse+specular
        #intensity *= 0.25
    else:
        intensity = ambient+diffuse+specular
    # Compute local color (from Phong Illumination model)

    # If the current object is a plane, generate the checkerboard
    if nearestObject.isPlane() == True:
        if nearestIntersectionPoint[0] >= 0:
            colorFlag = 1
        else:
            colorFlag = 0
        if abs(nearestIntersectionPoint[0]) % 200 > 100:
            colorFlag = (colorFlag + 1) % 2
        if abs(nearestIntersectionPoint[2]) % 200 > 100:
            colorFlag = (colorFlag + 1) % 2
        if colorFlag == 1:
            color = [255,0,0]
        else:
            color = [255,255,255]
    # Otherwise, set the local color
    else:
        color = nearestObject.localColor
    localColor = [color[0]*intensity*2, color[1]*intensity*2, color[2]*intensity*2]
    localWeight = nearestObject.localWeight
    # Calculate direction of reflected ray
    reflectWeight = nearestObject.reflectWeight
    # Calculate reflect
    reflectRay = nearestObject.reflect(nearestIntersectionPoint, ray)
    # Compute reflected color
    reflectColor = traceRay(nearestIntersectionPoint, reflectRay, depth-1)
    # Combine local and reflected colors
    returnColor = [0,0,0]
    for i in range(3):
        returnColor[i] = localColor[i]*localWeight + reflectColor[i]*reflectWeight
    return returnColor

# ********************************* In Shadow **********************************
# Determines if a point is in a shadow by tracing a ray back to the light source
def inShadow(startObject, startPoint):
    ray = computeUnitVector(startPoint, lightSource)
    for object in scene:
        t, intersectPoint = object.intersect(startPoint, ray)
        if startObject != object and t != [] and t > 0.001:
            return True
    return False

# ******* TriColorHexCode *******
# From the render20Spheres method
def RGBColorHexCode(color):
    red = colorHexCode(color[0])
    green = colorHexCode(color[1])
    blue = colorHexCode(color[2])
    colorString = "#"+red+green+blue
    return colorString

# ******** ColorHexCode *********
def colorHexCode(intensity):
    hexString = str(hex(round(255*intensity)))
    if hexString[0] == "-":
        trimmedHexString = "00"
    else:
        trimmedHexString = hexString[2:]
        if len(trimmedHexString) == 1:
            trimmedHexString = "0"+trimmedHexString
        elif len(trimmedHexString) > 2:
            trimmedHexString = "FF"
    return trimmedHexString

# ********************** Render Image Method ***********************
# Iterates over each pixel of the image, one row of pixels at a time
def renderImage():
    global L
    global lightSource
    global illuminationSaturationCounter
    illuminationSaturationCounter = 0
    L = normalize(lightSource)
    top = round(canvasHeight/2)
    bottom = round(-canvasHeight/2)
    left = round(-canvasWidth/2)
    right = round(canvasWidth/2)
    for y in range(top, bottom, -1):
        for x in range(left, right):
            ray = computeUnitVector(centerOfProjection, [x,y,0])
            color = traceRay(centerOfProjection, ray, 4)
            w.create_line(right+x, top-y, right+x+1, top-y, fill=RGBColorHexCode(color))
    overSat = illuminationSaturationCounter / (canvasWidth*canvasHeight) * 100
    #print(illuminationSaturationCounter, " pixel color values were oversaturated: ", overSat, "#.")

# ******************************************************
# Everything below is just interface and rendering calls
root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=canvasWidth, height=canvasHeight)
renderImage()
w.pack()
