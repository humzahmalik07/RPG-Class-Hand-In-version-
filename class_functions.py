import actions
import intro
import main_inventory
import maps

# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """ Use the Night Vision Goggles to see
                        in the dark and find your way """, }},
             "Green Lantern": {"Power Ring":
                               {"description":
                                "Use it as a flashlight to find their way", }}}

class Character(object):
    """ This object gives attributes to each character """
    def __init__(self, name, special_power, birthplace):
        self.name = name
        self.special_power = special_power
        self.birthplace = birthplace
        self.location = 'start'

    def introduction(self):
      print('Hi, my name is ', self.name)
      print("I have been chosen by you for this mission. Here are some of my qualitites and background:") 

    def power_birthplace(self):
      print("My special power is my", self.special_power)
      print("My birthplace is", self.birthplace)
      print('\n')


def green_lantern_class():
    """ Prints out some description for Green Lantern """
    class Green_Lantern(Character):
        green_lantern = Character("Green Lantern", "power ring", "Coast City")
        green_lantern.introduction()
        green_lantern.power_birthplace()


def batman_class():
    """ Prints out some description for Batman """
    class Batman(Character):
        batman = Character("Batman", "High Intelligence", "Gotham City")
        batman.introduction()
        batman.power_birthplace()


class MapTile:
    """ This Map uses x and y coordinates to print out location"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def location(self):
        print("your current location is ", self.x, self.y)

valid_actions = ["forward", "backward", "left", "right"]


def menu():
    """ Prints out the menu for the actions """
    print("""Choose an action:  
     """)
    for action in valid_actions:
        print(f"* {action}")


def firstTiles():
    """Prints out the menu and the current location for movement in the map """
    main_inventory.player_inventory("Batman", inventory)
    class firstTile(MapTile):
        print("""
        ###################################################

        You are at the start. enter direction to go
        """)
        Tile = MapTile(1, 0)
        Tile.location()
    menu()
    direction = input("Where do you want to go: ")
    if direction.lower() == "forward":
            print(" You are going forward")
            fourthTiles()
    if direction.lower() == "backward":
            print("wrong way")
            firstTile()
    if direction.lower() == "left":
            print("wall ahead")
            firstTile()
    if direction.lower() == "right":
        print("You are going right to the second Tile")
        secondTiles()


def secondTiles():
    """Prints out the menu and the current location for movement in the map """
    class secondTile(MapTile):
        print("""
        You are at the second tile. enter direction to go
        """)
        Tile_2 = MapTile(2, 0)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the fifth Tile")
            fifthTiles()
        if direction.lower() == "backward":
            print("dead end")
            secondTiles()
        if direction.lower() == "left":
            print("You are going right to the third Tile")
            firstTiles()
        if direction.lower() == "right":
            print("You are going right to the third Tile")
            thirdTiles()


def thirdTiles():
    """Prints out the menu and the current location for movement in the map """
    class thirdTile(MapTile):
        print("""
        You are at the third tile. enter direction to go
        """)
        Tile_2 = MapTile(3, 0)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the sixth Tile")
            sixthTiles()
        if direction.lower() == "backward":
            print("Dead end")
            thirdTiles()
        if direction.lower() == "left":
            print("You are going left back to the second Tile")
            secondTiles()
        if direction.lower() == "right":
            print("Wall ahead")
            thirdTiles()


def fourthTiles():
    """Prints out the menu and the current location for movement in the map """
    class fourthTile(MapTile):
        print("""
        You are at the fourth tile. enter direction to go
        """)
        Tile_2 = MapTile(1, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the seventh Tile")
            seventhTiles()
        if direction.lower() == "backward":
            print("You are going back to the first Tile")
            firstTiles()
        if direction.lower() == "left":
            print("Dead End")
            fourthTiles()
        if direction.lower() == "right":
            print("You are going right to the fifth Tile")
            fifthTiles()


def fifthTiles():
    """Prints out the menu and the current location for movement in the map """
    class fifthTile(MapTile):
        print("""
        You are at the fifth tile. enter direction to go
        """)
        Tile_2 = MapTile(2, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the eighth Tile")
            eighthTiles()
        if direction.lower() == "backward":
            print("You are going back to the second Tile")
            secondTiles()
        if direction.lower() == "left":
            print("You are going left to the fourth Tile")
            fourthTiles()
        if direction.lower() == "right":
            print("You are going right to the sixth Tile")
            sixthTiles()


def sixthTiles():
    """Prints out the menu and the current location for movement in the map """
    class sixthTile(MapTile):
        print("""
        You are at the sixth tile. enter direction to go
        """)
        Tile_2 = MapTile(3, 1)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("You are going forward to the ninth Tile")
            ninthTiles()
        if direction.lower() == "backward":
            print("You are going back to the third Tile")
            thirdTiles()
        if direction.lower() == "left":
            print("You are going left to the fifth Tile")
            fifthTiles()
        if direction.lower() == "right":
            print("Dead End")
            sixthTiles()


def seventhTiles():
    """Prints out the menu and the current location for movement in the map """
    class seventhTile(MapTile):
        print("""
        You are at the seventh tile. enter direction to go
        """)
        Tile_2 = MapTile(1, 2)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("Wall ahead")
            seventhTiles()
        if direction.lower() == "backward":
            print("You are going back to the fourth Tile")
            fourthTiles()
        if direction.lower() == "left":
            print("Dead End")
            seventhTiles()
        if direction.lower() == "right":
            print("You are going right to the eighth Tile")
            eighthTiles()


def eighthTiles():
    """Prints out the menu and the current location for movement in the map """
    class eighthTile(MapTile):
        print("""
        You are at the eighth tile. enter direction to go
        """)
        Tile_2 = MapTile(2, 2)
        Tile_2.location()
        print(""" Congratulations!!!. You have found the treasure.
                  You will now move to the next round, where you have
                  to escape the enemies with the treasure. """)
        intro.introduction_part_3()
        maps.map_temple()
        actions.action_1()


def ninthTiles():
    """Prints out the menu and the current location for movement in the map """
    class ninthTile(MapTile):
        print("""
        You are at the ninth tile. enter direction to go
        """)
        Tile_2 = MapTile(3, 2)
        Tile_2.location()
        menu()
        direction = input("Where do you want to go: ")
        if direction.lower() == "forward":
            print("Wall ahead")
            ninthTiles()
        if direction.lower() == "backward":
            print("You are going back to the sixth Tile")
            sixthTiles()
        if direction.lower() == "left":
            print("You are going left to the eighth Tile")
            eighthTiles()
        if direction.lower() == "right":
            print("Dead end")
            ninthTiles()