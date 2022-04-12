####################################################################################################################
# Name: James Brooks                                                                                               #
# Date: 8/12/2020                                                                                                  #
# Description: Using the Fractals module provided, improves the Chaos Game by allowing new Fractals to be created. #
####################################################################################################################
# imports the Fractals module
from Fractals import *

# imports libraries
from Tkinter import *
from math import sqrt, sin, cos, pi as PI
from random import randint

# the Chaos Game class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    def __init__(self, master):
        Canvas.__init__(self, master, bg="white")
        self.pack(fill=BOTH, expand=1)

    # the make function
    def make(self, f):
        # retrieves variables to assemble a dictionary
        dimensions = { "min_x" : MIN_X, "max_x" : MAX_X, "min_y" : MIN_Y, "max_y" : MAX_Y, "mid_x" : MID_X, "mid_y" : MID_Y }

        # creates the Sierpinski Triangle
        if (f == "SierpinskiTriangle"):
            # creates an instance of the Sierpinski Triangle class
            instance = SierpinskiTriangle(dimensions)
            # variable for the vertices list
            trivert = instance.vertices
            # plots the vertices
            for i in range(0, len(trivert)):
                self.plotVertices(trivert[i])
            # sets up a random initial point
            p = Point(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y))
            # repeat for that class' number of points
            for i in range(0, instance.num_points):
                # plots the most recent selected point
                self.plotPoints(p)
                # randomly selects a corner vertex
                corner = randint(0, 2)
                # sets a point at the intermediate point between the current point and the
                # randomly selected corner vertex
                if corner == 0:
                    p = p.interpt(trivert[0], instance.r)
                if corner == 1:
                    p = p.interpt(trivert[1], instance.r)
                if corner == 2:
                    p = p.interpt(trivert[2], instance.r)
                # code loops around and plots the chosen points until the number has been reached.

        # creates the Sierpinski Carpet
        if (f == "SierpinskiCarpet"):
            # creates an instance of the Sierpinski Carpet class
            instance = SierpinskiCarpet(dimensions)
            # variable for the vertices list
            carpvert = instance.vertices
            # plots the vertices
            for i in range(0, len(carpvert)):
                self.plotVertices(carpvert[i])
            # sets up a random initial point
            p = Point(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y))
            # repeat for that class' number of points
            for i in range(0, instance.num_points):
                # plots the most recent selected point
                self.plotPoints(p)
                # randomly selects a corner vertex
                corner = randint(0, 7)
                # sets a point at the intermediate point between the current point and the randomly selected
                # corner vertex
                if corner == 0:
                    p = p.interpt(carpvert[0], instance.r)
                if corner == 1:
                    p = p.interpt(carpvert[1], instance.r)
                if corner == 2:
                    p = p.interpt(carpvert[2], instance.r)
                if corner == 3:
                    p = p.interpt(carpvert[3], instance.r)
                if corner == 4:
                    p = p.interpt(carpvert[4], instance.r)
                if corner == 5:
                    p = p.interpt(carpvert[5], instance.r)
                if corner == 6:
                    p = p.interpt(carpvert[6], instance.r)
                if corner == 7:
                    p = p.interpt(carpvert[7], instance.r)
                # code loops around and plots the chosen points until the number of points has been reached

        # creates the Pentagon
        if (f == "Pentagon"):
            # creates an instance of the Pentagon class
            instance = Pentagon(dimensions)
            # variable for the vertices list
            pentvert = instance.vertices
            # plots the vertices
            for i in range(0, len(pentvert)):
                self.plotVertices(pentvert[i])
            # sets up a random initial point
            p = Point(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y))
            # repeat for that class' number of points
            for i in range(0, instance.num_points):
                # plots the most recent selected point
                self.plotPoints(p)
                # randomly selects a corner vertex
                corner = randint(0, 4)
                # sets a point at the intermediate point between the current point and the randomly selected
                # corner vertex
                if corner == 0:
                    p = p.interpt(pentvert[0], instance.r)
                if corner == 1:
                    p = p.interpt(pentvert[1], instance.r)
                if corner == 2:
                    p = p.interpt(pentvert[2], instance.r)
                if corner == 3:
                    p = p.interpt(pentvert[3], instance.r)
                if corner == 4:
                    p = p.interpt(pentvert[4], instance.r)
                # code loops around and plots the chosen points until the number of points has been reached

        # creates the Hexagon
        if (f == "Hexagon"):
            # creates an instance of the Hexagon class
            instance = Hexagon(dimensions)
            # variable for the vertices list
            hexvert = instance.vertices
            # plots the vertices
            for i in range(0, len(hexvert)):
                self.plotVertices(hexvert[i])
            # sets up a random initial point
            p = Point(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y))
            # repeat for that class' number of points
            for i in range(0, instance.num_points):
                # plots the most recent selected point
                self.plotPoints(p)
                # randomly selects a corner vertex
                corner = randint(0, 5)
                # sets a point at the intermediate point between the current point and the randomly selected
                # corner vertex
                if corner == 0:
                    p = p.interpt(hexvert[0], instance.r)
                if corner == 1:
                    p = p.interpt(hexvert[1], instance.r)
                if corner == 2:
                    p = p.interpt(hexvert[2], instance.r)
                if corner == 3:
                    p = p.interpt(hexvert[3], instance.r)
                if corner == 4:
                    p = p.interpt(hexvert[4], instance.r)
                if corner == 5:
                    p = p.interpt(hexvert[5], instance.r)
                # code loops around and plots the chosen points until the number of points has been reached

        # creates the Octagon
        if (f == "Octagon"):
            # creates an instance of the Octagon class
            instance = Octagon(dimensions)
            # variable for the vertices list
            octvert = instance.vertices
            # plots the vertices
            for i in range(0, len(octvert)):
                self.plotVertices(octvert[i])
            # sets up a random initial point
            p = Point(randint(MIN_X, MAX_X), randint(MIN_Y, MAX_Y))
            # repeat for that class' number of points
            for i in range(0, instance.num_points):
                # plots the most recent selected point
                self.plotPoints(p)
                # randomly selects a corner vertex
                corner = randint(0, 7)
                # sets a point at the intermediate point between the current point and the randomly selected
                # corner vertex
                if corner == 0:
                    p = p.interpt(octvert[0], instance.r)
                if corner == 1:
                    p = p.interpt(octvert[1], instance.r)
                if corner == 2:
                    p = p.interpt(octvert[2], instance.r)
                if corner == 3:
                    p = p.interpt(octvert[3], instance.r)
                if corner == 4:
                    p = p.interpt(octvert[4], instance.r)
                if corner == 5:
                    p = p.interpt(octvert[5], instance.r)
                if corner == 6:
                    p = p.interpt(octvert[6], instance.r)
                if corner == 7:
                    p = p.interpt(octvert[7], instance.r)
                # code loops around and plots the chosen points until the number of points has been reached
        
                
    # This function plots the vertices in the color red with radius 2
    def plotVertices(self, p):
        POINT_COLORS = ["red"]
        POINT_RADIUS = 2
        color = "red"
        # ovals interpret the x and y from the 2D point instance
        self.create_oval(p.x, p.y, p.x + POINT_RADIUS * 2, p.y + POINT_RADIUS * 2, outline=color)

    # This function plots the points in the color black with radius 0
    def plotPoints(self, p):
        #POINT_COLORS = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        POINT_COLORS = ["black"]
        POINT_RADIUS = 0
        color = "black"
        # ovals interpret the x and y from the 2D point instance
        self.create_oval(p.x, p.y, p.x + POINT_RADIUS * 2, p.y + POINT_RADIUS * 2, outline=color)
    
############################
# MAIN PART OF THE PROGRAM #
############################

# the default size of the canvas is 600x520
# sets up variables used in dimensions dictionary
WIDTH = 600
HEIGHT = 520
MIN_X = 10
MAX_X = (WIDTH - 10)
MIN_Y = 10
MAX_Y = (HEIGHT - 10)
MID_X = (MIN_X + MAX_X)/2
MID_Y = (MIN_Y + MAX_Y)/2

# the implemented fractals
FRACTALS = [ "SierpinskiTriangle", "SierpinskiCarpet", "Pentagon", "Hexagon", "Octagon" ]

#create the fractals in individual windows
for f in FRACTALS:
        print ("Generating " + f + "...")
        window = Tk()
        window.geometry("{}x{}".format(WIDTH, HEIGHT))
        window.title("The Chaos Game...Reloaded")
        #create the game as a Tkinter canvas inside the window
        s = ChaosGame(window)
        #make the current fractal
        s.make(f)
        #wait for the window to close
        window.mainloop()

print ("All done!")
        
