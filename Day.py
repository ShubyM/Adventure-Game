class Room:
    def __init__(self, width, height, name, specialPlace):
        self.width = width
        self.height = height
        self.name = name
    
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.name = name

    

class Person:
    def __init__(self, inventory, xPos , yPos):
        self.inventory = inventory
        self.xPos = xPos
        self.yPos = yPos


    def initalPosition(self, Room):
        self.xPos = (Room.width + 1) / 2
        self.yPos = 1

    def move(self, direction, Room):
    
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
            print("You hit a wall")
            self.xPos = storeXPos
        
        if (self.yPos <= 0 or self.yPos > Room.height):
            print("You hit a wall")
            self.yPos = storeYPos
            

firstRoom = Room(3, 3, "firstRoom", [1,3])
mainCharacter = Person([], 0, 0)
mainCharacter.initalPosition(firstRoom)

while(1 == 1):
    mainCharacter.move(input("Enter in the direction you wanna go!"), firstRoom)
    print(mainCharacter.xPos, mainCharacter.yPos)
    
