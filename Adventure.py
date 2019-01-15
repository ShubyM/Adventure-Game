class Room:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

    

class Person:
    hitWall = False

    def __init__(self, inventory, xPos , yPos):
        self.inventory = inventory
        self.xPos = xPos
        self.yPos = yPos


    def initalPosition(self, Room):
        self.xPos = (Room.width + 1) / 2
        self.yPos = 0

    def move(self, direction, Room):
        if (direction.lower() == 'forward'):
            self.yPos = self.yPos + 1 

        if (direction.lower() == 'back'):
            self.yPos = self.yPos - 1 

        if (direction.lower() == 'left'):
            self.xPos = self.xPos - 1 

        if (direction.lower() == 'right'):
            self.xPos = self.xPos + 1
        
        if ((self.xPos < 0 or self.xPos > Room.width) or (self.yPos < 0 or self.yPos > Room.height)):
            

firstRoom = Room(3, 3, "firstRoom")
mainCharacter = Person([], 0, 0)

while(1 == 1):
    mainCharacter.move(input("Enter in the direction you wanna go!"), firstRoom)
    print(mainCharacter.yPos)










    
