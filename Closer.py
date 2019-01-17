class Room:
    def __init__(self, width, height, name, door, backDoor, item):
        self.width = width
        self.height = height
        self.name = name
        self.door = door
        self.backDoor = backDoor
        self.item = item

class Person:
    def __init__(self, inventory, xPos , yPos):
        self.inventory = inventory
        self.xPos = xPos
        self.yPos = yPos

    def initalPosition(self, Room):
        self.xPos = (Room.width + 1) / 2
        self.yPos = 1
        
    def currentLocation(self):
        print(self.xPos, self.yPos)

    def move(self, direction, Room):
        print(Room.name)
        print(mainCharacter.xPos, mainCharacter.yPos)
        if (direction.lower() == 'up'):
            storeYPos = self.yPos
            self.yPos = self.yPos + 1 

        if (direction.lower() == 'down'):
            storeYPos = self.yPos
            self.yPos = self.yPos - 1 

        if (direction.lower() == 'left'):
            storeXPos = self.xPos
            self.xPos = self.xPos - 1 

        if (direction.lower() == 'right'):
            storeXPos = self.xPos 
            self.xPos = self.xPos + 1
        
        if (self.xPos <= 0 or self.xPos > Room.width):
            print("Your next to a wall")
            self.xPos = storeXPos
        
        if (self.yPos <= 0 or self.yPos > Room.height):
            print("Your next to a wall")
            self.yPos = storeYPos

# End of classes, moving on to room functionality

mainCharacter = Person([], 0, 0)

# def checkForDoorHallways(Person, Room):
#     xFirst = Room.door[0]
#     yFirst = Room.door[1]

#     xSecond = Room.door[2]
#     ySecond = Room.door[3]

#     if Person.xPos == (xFirst or xSecond) and Person.yPos == (yFirst or ySecond):
#         print("There is a door in front of you do you wish to proceed. (Types yes or no)")
#         if Person.xPos == xFirst:
#             print("This is the door from the room you are in")
#             return 1
#         else:
#             return 2
        

# def hallWay():
#     global mainCharacter 
#     HALLWAY = Room(1,3, "HALLWAY", [1,1,1,3], None)
#     mainCharacter.initalPosition(HALLWAY)

#     while(True):
#         mainCharacter.move(input(), hallWay)

#         if checkForDoorHallways(mainCharacter, HALLWAY) == 1:
#             return 1

#         else:
#             return 2

'''Potential code for hallways in the future'''
'''Code can also be very easily modified for others to build there own game'''
'''Creating rooms using a constructor and objects makes this very easy'''


def checkForDoorRooms(Person, Room):
    xForDoor = Room.door[0]
    yForDoor = Room.door[1]
    if (Person.xPos == xForDoor and Person.yPos == yForDoor):
        return True

def roomOne(): 
    global mainCharacter
    firstRoom = Room(3, 3, "firstRoom", [2,3], None, None)
    mainCharacter.initalPosition(firstRoom)

    while (True):
        mainCharacter.move(input(), firstRoom)
        if checkForDoorRooms(mainCharacter, firstRoom):
            if (input("There is a portal in front of you do you wish to proceed. (Types yes or no)") == 'yes' or 'Yes'):
                roomTwo()
                break

def test():
    print('hello')

def roomTwo(): 
    global mainCharacter
    secondRoom = Room(5,5, "secondRoom", [5, 3], [5,6], None)
    mainCharacter.initalPosition(secondRoom)

    while(True):
        mainCharacter.move(input(), secondRoom)
        if checkForDoorRooms(mainCharacter, secondRoom):
            if (input("There is a portal in front of you do you wish to proceed. (Types yes or no)") == 'yes' or 'Yes'):
                test()
                break




def startGame():
    roomOne()

startGame()
