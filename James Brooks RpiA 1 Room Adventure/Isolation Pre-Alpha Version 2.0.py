#########################################################################################################################################################################################################################################################################################################################################################
# Name: James Brooks                                                                                                                                                                                                                                                                                                                                    #
# Date: 7/27/20                                                                                                                                                                                                                                                                                                                                         #
# Description: An expansion and improvement over the Room Adventure Source Code, including a new room description that provides more narration, usable items, more rooms, more items, use item puzzles, 3 dimensional rooms, item descriptions that change when you grab an item, a score system, and much more! Now including a GUI with dynamic maps! #
#########################################################################################################################################################################################################################################################################################################################################################

###########
# CSC 131 #
###########
# Hey there! And welcome to my version of the Room Adventure activity, known as Isolation!
# I've always been a fan of text-adventures on the computer (such as Zork and Hitchhiker's Guide to the Galaxy), so this was a fun assignment for me!
# Of the suggested improvements, I implemented the following:
#   -Item description being updated when you grab an item (e.g., the key is no longer on the table).
#   -Way more rooms and items, including starting in a whole new room and exploring a forest with different locations.
#   -The mansion has a secret attic that you must unlock to go up to!
#   -The use function! Several puzzles that you must use items to solve! At least two are required for you to beat the game, and there are a couple others for bonus points!
#   -A score system that increases as you solve puzzles!
#   -A new room description in the status that lets me give more narration to new rooms!
#   -Much more, including a subtle story that gives context for exploring the area!
# I'll try to mark my improvements and additions as best I can, look out for a double hashtag and NEW CODE to see new code, like this:
## NEW CODE ##
# At the bottom of this code, I will also include a strategy/cheat guide in comments for getting the high score in this game.
# If you see any lines of code that are commented off (mainly in createRooms()), those are for future additions, as I will try to continue to work on this outside of the assignment
# to make into a full game!
# Have fun!

###########
# CSC 132 #
###########
# Hello! Once again this is my version of the Room Adventure activity.
# As stated above, I love text based adventures, so hearing that we'd be revisiting the
# Room Adventure really excited me.
# Listed above were the improvements I made the first time, like the use function and so forth.
# This time around I have included the following:
#   -The required dictionary improvements
#   -The required GUI windows
#   -Custom map images (I'm not an art major, but they get the job done!)
#   -Dynamic map images that change as you take and use items
#   -Additional dynamic text as you take and use items
#   -Many more improvements
# I'll try to mark these new additions with:
## NEWER CODE ##
# But I made so many I'm sure I've missed some.
# At the bottom of this code is still a working strategy/cheat guide.
# Have fun!

## NEWER CODE ##
# Tkinter import.
# Also moved variables used for scoring up here.
from Tkinter import *
score = 0
firstusetinder = 0
firstusenote = 0
secondusetinder = 0

# the blueprint for a room
class Room(object):
    # the constructor
    ## NEW CODE ##
    # I've added roomDesc. This will allow me to add an additional line of text that will give more narrative description of the room that you are in.
    ## NEWER CODE ##
    # Image is added, dictionaries are implemented.
    def __init__(self, name, roomDesc, image):
        # rooms have a name, a narrative description, exits (e.g., south), exit locations (e.g., to the south is room n), items (e.g., table), item descriptions (for each item), grabbables (things that can be taken into inventory), and an image
        self.name = name
        self.roomDesc = roomDesc
        self.image = image
        self.exits = {}
        self.items = {}
        self.grabbables = []
        
    # getters and setters for the instance variables
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
        
    @property
    def roomDesc(self):
        return self._roomDesc
    
    @roomDesc.setter
    def roomDesc(self, value):
        self._roomDesc = value

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, value):
        self._image = value
        
    @property
    def exits(self):
        return self._exits
    
    @exits.setter
    def exits(self, value):
        self._exits = value
        
    @property
    def items(self):
        return self._items
    
    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables
    
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value

    # adds an exit to the room
    # the exit is a string (e.g., north)
    # the room is an instance of a room
    def addExit(self, exit, room):
        # append the exit and room to the appropriate lists
        self._exits[exit] = room

    # adds an item to the room
    # the item is a string (e.g., table)
    # the desc is a string that describes the item (e.g., it is made of wood)
    def addItem(self, item, desc):
        # append the item and description to the appropriate lists
        self._items[item] = desc

    ## NEW CODE ##
    # delItem() is primarily used when I want to change an item when you grab a grabbable.
    # For instance, when you grab the key off the table, the code quickly deletes the table item and then adds a new table item with a new description,
    # showing the key is no longer there.
    def delItem(self, item):
        self._items.pop(item)
        
    # adds a grabbable item to the room
    # the item is a string (e.g., key)
    def addGrabbable(self, item):
        # append the item to the list
        self._grabbables.append(item)

    # removes a grabbable item from the room
    # the item is a string (e.g., key)
    def delGrabbable(self, item):
        # remove the item from the list
        self._grabbables.remove(item)
        
    # returns a string description of the room
    def __str__(self):
        # first, the room name
        s = "You are in {}.\n".format(self.name)
        s += "{}\n".format(self.roomDesc)

        # items in the room
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n"

        # next, the exits from the room
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "

        return s

## NEWER CODE ##
# New game class
class Game(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

    ## NEW CODE ##
    # Lots and lots of new rooms and items!
    # The naming convention for the rooms outside of the house works like a coordinate plane, with the starting room being r0_0 and the exit to the northeast being r1_1.
    # There are occasional exceptions to this when a room is unique, such as rDock and rDR (Dark Room).
    #creates the rooms
    def createRooms(self):
        # r1 through r4 are the four rooms in the mansion
        # currentRoom is the room the player is currently in (which can be one of r1 through r4)
        # since it needs to be changed in the main part of the program,
        # it must be global
        global currentRoom
        # create the rooms and give them meaningful names
        ## NEW CODE ##
        # Additional global rooms were added for those that have their exits or other properties adjusted outside of this function.
        ## NEWER CODE ##
        # Adds an image to the created room as well
        global r1
        global r5
        global rforesttemple
        r1 = Room("the foyer", "An old foyer decorated only with only a chair and table left. The air is thick with dust and \nregret.", "images/r1.gif")
        r2 = Room("The living room", "The wood creaks beneath your feet as you enter \nthe living room. Despite the generally unkempt \natmosphere of the home, the fireplace has fresh \nashes in it. Someone has been here.", "images/r2.gif")
        r3 = Room("the sun room", "A cozy sun room, were it not for the cobwebs. \nSomeone's done a lot of reading here.", "images/r3.gif")
        r4 = Room("the kitchen", "A sad excuse for a kitchen, really. The smell in the air is a strange combination of hot gruel and something else emanating from the brewed liquids.\nOh, and there's a spike pit to the south. Watch \nyour step!", "images/r4.gif")
        r5 = Room("the attic", "A secret attic! There's plenty of treasure here. There's also a closet.", "images/r5.gif")
        rDR = Room("the dark room", "This is the dark room you woke up in.\nThe room would be pitch black were it not for the light creeping through a part to the north.", "images/rDR.gif")
        r0_0 = Room("the central clearing in the forest", "Birds tweet in the tree tops and sun beams break through the branches. The dark room in the hut \nthat you woke up in is to the south. There's a \nmailbox here.", "images/r0_0.gif")
        #rn1_0 = Room("the west path", "The path here is a little rocky. There is the sound of running water to the west.")
        r1_0 = Room("the clearing outside the house", "A quaint, old house stands amidst the trees.", "images/r1_0.gif")
        r0_1 = Room("the north clearing", "You stand in a mostly empty clearing. A tall, \nunique tree stands in the middle of the clearing. A large bird's nest sits high above in the \nbranches. There's also a rock here.", "images/r0_1.gif")
        rDock = Room("the rickety old dock", "There's a crate on the dock, but the dock is not stable and is above shark infested waters. Watch your step!", "images/rdock.gif")
        r1_1 = Room("the northeast junction", "A golden gate sits before you. There are berry \nbushes lining the path to the gate.", "images/r1_1.gif")
        rforesttemple = Room ("the forest temple", "A huge, blocky pyramid like structure sits before you. A staircase leads up to its peak, \nchallenging you to delve inside.", "images/rforesttemple.gif")
        # add properties to room 1
        r1.addExit("east", r2) # -> to the east of room 1 is room 2
        r1.addExit("south", r3)
        r1.addExit("west", r1_0)
        r1.addGrabbable("key")
        r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
        r1.addItem("table", "It is made of oak. A golden key rests on it.")
        # add properties to room 2
        r2.addExit("west", r1)
        r2.addExit("south", r4)
        r2.addItem("rug", "It is nice and Indian. It also needs to be \nvacuumed.")
        r2.addItem("fireplace", "It is full of ashes.")
        # add properties to room 3
        r3.addExit("north", r1)
        r3.addExit("east", r4)
        r3.addGrabbable("book")
        r3.addItem("bookshelf", "It's empty. Go figure.")
        r3.addItem("statue", "There is nothing special about it.")
        r3.addItem("desk", "The statue is resting on it. So is a book.")
        # add properties to room 4
        r4.addExit("north", r2)
        r4.addExit("west", r3)
        r4.addExit("south", None) # DEATH!
        r4.addGrabbable("6-pack")
        r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on \nthe brew rig. A 6-pack is resting beside it.")
        #add properties to room 5
        r5.addExit("down", r3)
        r5.addItem("closet", "Inside the closet is a ladder and a skeleton.")
        r5.addGrabbable("ladder")
        r5.addGrabbable("treasure")
        # add properties to the dark room
        rDR.addExit("north", r0_0)
        rDR.addGrabbable("tinderbox")
        rDR.addItem("sleeping_pad", "You woke up in this pad with no recollection of \nhow you got there.")
        rDR.addItem("hearth", "A circular hearth in the center of the dark room. It is currently unlit.\nA tinderbox sits next to the hearth.")
        # add properties to the hub
        #r0_0.addExit("west", rn1_0)
        r0_0.addExit("south", rDR)
        r0_0.addExit("east", r1_0)
        r0_0.addExit("north", r0_1)
        r0_0.addItem("mailbox", "A small note sits inside the mailbox.")
        r0_0.addGrabbable("note")
        # add properties to the clearing outside the house
        r1_0.addExit("west", r0_0)
        r1_0.addExit("south", rDock)
        r1_0.addExit("north", r1_1)
        r1_0.addItem("house", "This quaint old house seems familiar... The \nentrance is boarded up.")
        r1_0.addItem("boards", "All the windows and the front door are boarded \nup. If only you had something to remove it...")
        # add properties to the dock
        rDock.addExit("north", r1_0)
        rDock.addExit("east", None) # DEATH!
        rDock.addExit("south", None) # DEATH!
        rDock.addExit("west", None) # DEATH!
        rDock.addItem("crate", "You make your way carefully down the dock to the crate. Inside is a crowbar with a note on it that reads:\nYou might need this. -Freeman")
        rDock.addGrabbable("crowbar")
        # add properties to the junction
        r1_1.addExit("south", r1_0)
        r1_1.addExit("west", r0_1)
        r1_1.addItem("bush", "A berry bush. You can pluck the berries right \noff! Sure hope they aren't poisonous...")
        r1_1.addItem("gate", "A closed golden gate blocks your path to the \neast. It is locked with a large golden lock.")
        r1_1.addGrabbable("berries")
        # add properties to the northern clearing
        r0_1.addExit("south", r0_0)
        r0_1.addExit("east", r1_1)
        r0_1.addItem("nest", "Something shimmers in the bird's nest high above you. If only you could see what it was...")
        r0_1.addItem("rock", "It's just a rock. It's crazy how ordinary this \nrock is.")
        # add properties to the forest temple
        # set room 1 as the current room at the beginning of the game
        Game.currentRoom = rDR
        # setup inventory
        Game.inventory = []

    ## NEWER CODE ##
    # GUI setup
    def setupGUI(self):
        self.pack(fill=BOTH, expand=1)

        # setup the player input at the bottom of the GUI
        # Tkinter Entry
        # background is white and bind return key to process
        # push to bottom and horizontal
        # focus so player does not have to click on it
        # the widget is a Tkinter Entry
        # set its background to white and bind the return key to the
        # function process in the class
        # push it to the bottom of the GUI and let it fill
        # horizontally
        # give it focus so the player doesn't have to click on it
        Game.player_input = Entry(self, bg="white")
        Game.player_input.bind("<Return>", self.process)
        Game.player_input.pack(side=BOTTOM, fill=X)
        Game.player_input.focus()

        # setup the image to the left of the GUI
        # the widget is a Tkinter Label
        # don't let the image control the widget's size
        img = None
        Game.image = Label(self, width=WIDTH / 2, image=img)
        Game.image.image = img
        Game.image.pack(side=LEFT, fill=Y)
        Game.image.pack_propagate(False)

        # setup the text to the right of the GUI
        # first, the frame in which the text will be placed
        text_frame = Frame(self, width=WIDTH / 2)
        # the widget is a Tkinter Text
        # disable it by default
        # don't let the widget control the frame's size
        Game.text = Text(text_frame, bg="lightgrey", state=DISABLED)
        Game.text.pack(fill=Y, expand=1)
        text_frame.pack(side=RIGHT, fill=Y)
        text_frame.pack_propagate(False)

    ## NEWER CODE ##
    # Sets the room image
    def setRoomImage(self):
        if (Game.currentRoom == None):
            # if dead, set the skull image
            Game.img = PhotoImage(file="images/skull.gif")
        else:
            # otherwise grab the image for the current room
            Game.img = PhotoImage(file=Game.currentRoom.image)

        # display the image on the left of the GUI
        Game.image.config(image=Game.img)
        Game.image.image = Game.img

    ## NEWER CODE ##
    # Sets up the status
    def setStatus(self, status):
        # enable the text widget, clear it, set it, and disabled it
        Game.text.config(state=NORMAL)
        Game.text.delete("1.0", END)
        if (Game.currentRoom == None):
            # if dead, let the player know
            Game.text.insert(END, "You are dead. The only thing you can do now is \nquit.\n")
        elif (Game.currentRoom == rforesttemple):
            # if you reach the forest temple, end the game
            Game.text.insert(END, "You made it to the end of this demo!\nThanks for playing!\nAll you can do now is quit.")
        else:
            # otherwise, display the appropriate status
            Game.text.insert(END, str(Game.currentRoom) +\
            "\nYou are carrying: " + str(Game.inventory) +\
            "\nScore: {}".format(score) +\
            "\n\n" + status)
        Game.text.config(state=DISABLED)

    ## NEWER CODE ##
    # Runs functions
    def play(self):
        self.createRooms()
        self.setupGUI()
        self.setRoomImage()
        self.setStatus("")

    ## NEWER CODE ##
    # All verb functions are moved here, in addition to the new GUI setups
    def process(self, event):
        ## NEW CODE ##
        # The score variable that gets modified when completing puzzles.
        # The "firstuse" variables are to keep track of whether a certain action with an item has been done before or not,
        # to prevent performing the same action over and over to get infinite points.
        global score
        global firstusetinder
        global firstusenote
        global secondusetinder
        # grab the player's input from the input at the bottom of
        # the GUI
        action = Game.player_input.get()
        # set the user's input to lowercase to make it easier to compare
        # the verb and noun to known values
        action = action.lower()
        # set a default response
        response = "I don't understand. Try verb noun. Valid verbs are go, look, take, and use."

        # exit the game if the player wants to leave (supports quit, exit, and bye)
        if (action == "quit" or action == "exit" or action == "bye" or action == "sayonara!"):
            exit(0)
        # if the player is dead
        if (Game.currentRoom == None):
            # clear input
            Game.player_input.delete(0, END)
            return

        # split the user input into words (words are separated by spaces)
        words = action.split()

        # the game only understands two word inputs
        if (len(words) == 2):
            # isolate the verb and noun
            verb = words[0]
            noun = words[1]

            # the verb is: go
            if (verb == "go"):
                # set a default response
                response = "Invalid exit."

                # check for valid exits in the current room
                if (noun in Game.currentRoom.exits):
                    # a valid exit is found
                    # change the current room to the one that is
                    # associated with the specified exit
                    Game.currentRoom = Game.currentRoom.exits[noun]
                    # set the response (success)
                    response = "Room changed."
                    # no need to check any more exits
                    #break

            # the verb is: look
            elif (verb == "look"):
                # set a default response
                response = "I don't see that item."

                # check for valid items in the current room
                if (noun in Game.currentRoom.items):
                    # a valid item is found
                    # set the response to the item's description
                    response = Game.currentRoom.items[noun]
                    # no need to check any more items
                    #break

            # the verb is: take
            elif (verb == "take"):
                # set a default response
                response = "I don't see that item, or you cannot take that."

                # check for valid grabbable items in the current room
                for grabbable in Game.currentRoom.grabbables:
                    # a valid grabbable item is found
                    if (noun == grabbable):
                        # add the grabbable item to the player's inventory
                        Game.inventory.append(grabbable)
                        # remove the grabbable item from the room
                        Game.currentRoom.delGrabbable(grabbable)
                        # set the response (success)
                        response = "Item grabbed."
                        # no need to check any more grabbable items

                        ## NEW CODE ##
                        # This code is used when you grab a grabbable that was mentioned in an item's description.
                        # The old item is deleted, and a new one with a new description is made.

                        ## NEWER CODE ##
                        # Taking certain items changes the map image to reflect the item
                        # being taken!
                        if (noun == "tinderbox"):
                            Game.currentRoom.delItem("hearth")
                            Game.currentRoom.addItem("hearth", "A circular hearth in the center of the dark room. It is currently unlit.")
                            Game.currentRoom.image = ("images/rDRtaken.gif")
                        if (noun == "key"):
                            Game.currentRoom.delItem("table")
                            Game.currentRoom.addItem("table", "It is made of oak. There is a dusty imprint in /nthe shape of a key on it.")
                            Game.currentRoom.image = ("images/r1taken.gif")
                        if (noun == "note"):
                            Game.currentRoom.delItem("mailbox")
                            Game.currentRoom.addItem("mailbox", "The mailbox is empty.")
                            Game.currentRoom.image = ("images/r0_0open.gif")
                        if (noun == "crowbar"):
                            Game.currentRoom.delItem("crate")
                            Game.currentRoom.addItem("crate", "The crate is empty now. Quit messing around! This dock is about to collapse into the shark infested waters!")
                            Game.currentRoom.image = ("images/rdockopen.gif")
                        if (noun == "berries"):
                            Game.currentRoom.delItem("bush")
                            Game.currentRoom.addItem("bush", "Many berries have been picked from the bush.")
                        if (noun == "book"):
                            Game.currentRoom.delItem("desk")
                            Game.currentRoom.addItem("desk", "Only the statue sits on it now.")
                            Game.currentRoom.image = ("images/r3taken.gif")
                        if (noun == "6-pack"):
                            Game.currentRoom.delItem("brew_rig")
                            Game.currentRoom.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig.")
                            Game.currentRoom.image = ("images/r4taken.gif")
                        if (noun == "ladder"):
                            Game.currentRoom.delItem("closet")
                            Game.currentRoom.addItem("closet", "Just a skeleton in the closet!")
                            Game.currentRoom.image = ("images/r5taken.gif")
                        #break

            ## NEW CODE ##
            # The brand new use function!
            # First, the code checks if you even have the noun in your inventory.
            # If so, then it proceeds.
            # Most use items can only be used in very specific spots, so it checks if a certain item in the currentRoom is present.
            # If so, the item is used, which can result in opening new paths, gaining points, and other things.
            # Any use items that can be used more than once in any place have a variable to make sure the points they give aren't abused.
            # Some use items even give unique responses if you try to use them in the wrong spot!

            ## NEWER CODE ##
            # Using certain items changes the map image to reflect the item being used!
            elif (verb == "use"):
                response = "You don't have that item to use."
                if noun in Game.inventory:
                    response = "You can't use that here."
                    if(noun == "tinderbox"):
                        if "hearth" in Game.currentRoom.items:
                            response = "You use the tinderbox to spark the hearth in the dark room, and flames burst to life.\nYou are filled with hope."
                            if (firstusetinder < 1):
                                score += 100
                                firstusetinder += 1
                                Game.currentRoom.image = ("images/rDRfire.gif")
                                Game.currentRoom.delItem("hearth")
                                Game.currentRoom.addItem("hearth", "A circular hearth in the center of the dark room. The flames continue to roar.")
                        elif "fireplace" in Game.currentRoom.items:
                            response = "You use the tinderbox to spark a fire in the fireplace. Smoke billows up the chimney."
                            if (secondusetinder < 1):
                                score += 250
                                secondusetinder += 1
                                Game.currentRoom.image = ("images/r2fire.gif")
                        else:
                            response = "You can't use that here, unless you're trying to set the whole forest on fire!"
                    elif(noun == "note"):
                        response = "You read the note. It says:\n\nSalutations.\nYou now live in a world of Isolation.\nIf you wish to leave, heed my words.\nSalvation lies in the Artifacts.\nYou must find the Temples of Architects Ancient.\nThe elements of this land have been corrupted.\nYou must find a way."
                        if (firstusenote < 1):
                            score += 50
                            firstusenote += 1
                    elif(noun == "crowbar"):
                        if "boards" in Game.currentRoom.items:
                            response = "You use the crowbar to remove the boards from the house's front door. With the boards gone, you can now go east to enter the house!"
                            Game.currentRoom.image = ("images/r1_0open.gif")
                            Game.currentRoom.delItem("boards")
                            Game.currentRoom.delItem("house")
                            Game.currentRoom.addItem("house", "This quaint old house seems familiar...")
                            Game.currentRoom.addExit("east", r1)
                            score += 100
                    elif(noun == "book"):
                        if "bookshelf" in Game.currentRoom.items:
                            response = "You casually place the book on the bookshelf \nand... suddenly the bookshelf rotates into the wall!\nYou hear the sound of whirring machinery, and a staircase pops out of the wall that leads upwards! You can now go up the stairs!"
                            Game.currentRoom.image = ("images/r3stairs.gif")
                            Game.inventory.remove("book")
                            Game.currentRoom.delItem("bookshelf")
                            Game.currentRoom.addExit("up", r5)
                            score += 250
                    elif(noun == "ladder"):
                        if "nest" in Game.currentRoom.items:
                            response = "You plant the ladder in the dirt and begin the climb. When you reach the bird's nest, you finally find what was shimmering in the nest... an egg \nmade of pure gold and gilded with diamonds!\nYou climb back down, pleased with your loot."
                            Game.currentRoom.delItem("nest")
                            Game.currentRoom.addItem("nest", "The now empty bird's nest sits quietly in the \nbranches above.")
                            Game.inventory.append("golden_egg")
                            Game.inventory.remove("ladder")
                            score += 1000
                            Game.currentRoom.image = ("images/r0_1ladder.gif")
                        else:
                            response = "Nowhere to climb to."
                    elif(noun == "berries"):
                        response = "You eat the berries. They are juicy and sweet! \nYou feel satisfied and invigorated."
                        Game.inventory.remove("berries")
                        score += 50
                    elif(noun == "6-pack"):
                        response = "You chug the whole 6-pack. The whole thing. You \nregret it afterwards, but it was pretty cool."
                        Game.inventory.remove("6-pack")
                        score += 250
                    elif(noun == "key"):
                        if "gate" in Game.currentRoom.items:
                            response = "You take the key and slot it into the golden \nlock. It's a perfect fit. As you twist it, the key and the lock burst in a flash of magical light.\nThe gate swings open, revealing the exit to the \neast!"
                            Game.inventory.remove("key")
                            Game.currentRoom.delItem("gate")
                            Game.currentRoom.addItem("gate", "The golden gate leading to the east is wide open.")
                            Game.currentRoom.addExit("east", rforesttemple)
                            score += 500
                            Game.currentRoom.image = ("images/r1_1open.gif")
        ## NEWER CODE ##
        # Response is sent to the setStatus function
        # display the response
        self.setStatus(response)
        self.setRoomImage()
        Game.player_input.delete(0, END)

## NEW CODE ##
# A victory function that plays when you make your way past the gate in the northeast and exit.
# It displays some story text and then displays the player's final score.
#def victory():
    #print "You make your way past the golden gate and up the bushy path. When you emerge into another clearing, you are in awe of what you see.\nA massive, blocky, pyramid-like structure sits before you right here in the forest.\nOn its front side, a staircase leading to its peak challenges you to climb it and delve inside.\nCould this be a temple the note mentioned?\nWhat dangers lie inside?\nIs there any way to escape this Isolation?\nTO BE CONTINUED!\n\nThanks for playing!\n\nFINAL SCORE: {}".format(score)
## NEWER CODE ##
# victory() function has been condensed and moved further up.


##############
# GAME START #
##############

## NEW CODE ##
# Once again inspired by classic text-adventure games and the death function included, I made this:
# It prints out a sign that states the title of the game "ISOLATION" with each letter being made up of its own letter.
# A silly copyright screen is also printed, as well as the introductory text for the game.
print (" " + "_" * 67)
print ("|" + " " + " " + "_" * 63 + " " + " " + "|")
print ("|" + " " + "|" + " " * 63 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 63 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 5 + "I" * 5 + " " + "S" * 5 + " " * 2 + "O" * 3 + " " * 2 + "L" + " " * 6 + "A" * 3 + " " * 2 + "T" * 5 + " " + "I" * 5 + " " * 2 + "O" * 3 + " " * 2 + "N" + " " * 3 + "N" + " " * 5 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 7 + "I" + " " * 3 + "S" + " " * 5 + "O" * 2 + " " + "O" * 2 + " " + "L" + " " * 5 + "A" * 2 + " " + "A" * 2 + " " * 3 + "T" + " " * 5 + "I" + " " * 3 + "O" * 2 + " " + "O" * 2 + " " + "N" * 2 + " " * 2 + "N" + " " * 5 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 7 + "I" + " " * 3 + "S" * 5 + " " + "O" + " " * 3 + "O" + " " + "L" + " " * 5 + "A" * 5 + " " * 3 + "T" + " " * 5 + "I" + " " * 3 + "O" + " " * 3 + "O" + " " + "N" + " " + "N" + " " + "N" + " " * 5 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 7 + "I" + " " * 7 + "S" + " " + "O" * 2 + " " + "O" * 2 + " " + "L" + " " * 5 + "A" + " " * 3 + "A" + " " * 3 + "T" + " " * 5 + "I" + " " * 3 + "O" * 2 + " " + "O" * 2 + " " + "N" + " " * 2 + "N" * 2 + " " * 5 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 5 + "I" * 5 + " " + "S" * 5 + " " * 2 + "O" * 3 + " " * 2 + "L" * 5 + " " + "A" + " " * 3 + "A" + " " * 3 + "T" + " " * 3 + "I" * 5 + " " * 2 + "O" * 3 + " " * 2 + "N" + " " * 3 + "N" + " " * 5 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 63 + "|" + " " + "|")
print ("|" + " " + "|" + " " * 63 + "|" + " " + "|")
print ("\_/" * 23)
print (" ")
print ("(c) Copyright 2020 Raincoat Brotherhood Games. Some rights reserved.")
print ("Release Pre=Alpha Version 2.0")
print ("Welcome to Isolation!\n\nYou come to consciousness in a dark room with no recollection of how you got /nthere.\nYou can't remember your own name or anything from your past.\n")

## NEWER CODE ##
# Further sets up the Tkinter window
WIDTH = 800
HEIGHT = 600

window = Tk()
window.title("Room Adventure")

g = Game(window)
g.play()

window.mainloop()

print ("Bye!")

############################
# STRATEGY AND CHEAT GUIDE #
############################

# When you first load into the dark room, you can take the tinderbox right away.
# Taking the tinderbox will change the description of the hearth if you look at it.
# Using the tinderbox in the dark room will light the hearth, getting you some points.
# If you go north, you'll emerge from the dark room.
# You can take a note from the mailbox. If you do so, it changes the desription of the mailbox if you look at it.
# If you use the note, you'll read it, and get some points.
# Go east, and you'll find yourself outside of a familiar house. The house is boarded up though, and you'll need to get the boards off.
# If you go south, you'll find yourself on a rickety dock above shark infested waters.
# You can take the crowbar from the crate on the dock, which will change the description of the crate.
# ONLY GO NORTH. If you go any other direction, you'll slip off the dock and die.
# Use the crowbar to remove the boards off the house. This removes boards from the item list and changes the description of the house.
# Go east to enter the foyer. The key is on the table. Take the key and the description of the table will change.
# Go east into the living room. You can use the tinderbox to light another fire in the fireplace to get some more points.
# Go south to the kitchen. Take the 6-pack that is there, and use it to chug the whole thing to get some points. Taking the 6-pack will change the description of the brew_rig.
# DON'T GO SOUTH AGAIN or you'll fall into a pit of spikes.
# Go west into the sun room. Take the book and use it to put it in the bookshelf. This will cause the bookshelf to rotate into the wall, and a staircase will appear.
# Go up the staircase to go to the secret attic treasure room. You can take some treasure for yourself, and also take the ladder from the closet.
# Go back down, then north, then west to exit the mansion.
# Go west then north to get to the north clearing.
# Once there, use the ladder. You will climb up and take a golden egg from the bird's nest. This gives you the most points in the game!
# Go west. Take berries from the bush.
# Use the berries for some more points.
# Finally, use the key to open the gate. Then go east to exit and finish the game!
