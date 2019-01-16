class Room:
    def __init__(self, width, height, name, specialPlace, item):
        self.width = width
        self.height = height
        self.name = name
        self.door = specialPlace
        self.item = item

    
class Person:
    def __init__(self, inventory, xPos , yPos):
        self.inventory = inventory
        self.xPos = xPos
        self.yPos = yPos

    def initalPosition(self, Room):
        self.xPos = (Room.width + 1) / 2
        self.yPos = 1

    def move(self, direction, Room):
        print(Room.name)
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
            print("You next to a wall")
            self.yPos = storeYPos
            
def gameLoop():
    hasKey = False

    firstRoom = Room(3, 3, "firstRoom", [3,3], None)
    mainCharacter = Person([], 0, 0)
    mainCharacter.initalPosition(firstRoom)

    print("Hello and welcome to Save the King, a python based, text based adventure game!")
    print("The objective of the game is to find a key in one of the rooms, unlock a door, and get treasure")
    print("You can move around by typing up, down, left, or right")
    print("You can also check the items in your inventory by typing inventory!")

    while(hasKey == False):
        mainCharacter.move(input("Enter the direction you wanna go!\n"), firstRoom)
        if (mainCharacter.xPos == firstRoom.door[0] and mainCharacter.yPos == firstRoom.door[1]):
            print("You have found a key!")
            print("It has been added to your inventory!")

gameLoop()
        
        
    
    

