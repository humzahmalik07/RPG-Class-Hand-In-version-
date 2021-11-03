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
    """ This object uses the main class to make a child object"""
    class Green_Lantern(Character):
        green_lantern = Character("Green Lantern", "power ring", "Coast City")
        green_lantern.introduction()
        green_lantern.power_birthplace()

def batman_class():
    """ This object uses the main class to make a child object"""
    class Batman(Character):
        batman = Character("Batman", "High Intelligence", "Gotham City")
        batman.introduction()
        batman.power_birthplace()

def Batman_inventory():
    """ Prints out a statement about Batman's inventory """
    print("This is Batman's inventory:")


def Green_lantern_inventory():
    """ Prints out a statement about Green Lantern's inventory """
    print("This is Green Lantern's inventory:")


def character_intro():
    """ Prints out the introduction for Batman """
    print("""
  ####################################################

  You have chosen Batman as your character.
  You will use Batman to get out of this maze.
  You can use a hint to complete a level.
  Now Batman will introduce himself.
  """)


def character_intro_2():
    """ Prints out the introduction for Green Lantern """
    print("""
    #####################################################

     You have chosen Green Lantern as your character.
     You will use Green Lantern to get out of this maze.
     You can use a hint to complete a level.
     Now Green Lantern will introduce himself.
    """)
