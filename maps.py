# This defines the layout of the temple
# Level 1 is where the user starts in the game
# Level 10 is where the game finishes


def map_temple():
    """ Prints out the map for the second part of the game """
    temple_map = [
      ["Blank", "Blank", "Blank", "Level 10", "Blank"],
      ["Blank", "Blank", "Blank", "Level 9", "Blank"],
      ["Blank", "Blank", "Level 7", "Level 8", "Blank"],
      ["Blank", "Blank", "Level 6", "Blank", "Blank"],
      ["Blank", "Level 4", "Level 5", "Blank", "Blank"],
      ["Blank", "Level 3", "Blank", "Blank", "Blank"],
      ["Blank", "Level 2", "Level 1", "Blank", "Blank"], ]
    print(temple_map)


def main_map():
    """ Prints out the map for the first part of the game """
    gamemap_2 = [
            ["seventhTile=(1, 2)", "eighthTile=(2, 2)", "ninthTile=(3, 2)", ],
            ["fourthTile=(1, 1)", "fifthTile=(2, 1)", "sixthTile=(3, 1)", ],
            ["firstTile=(1, 0)", "secondTile=(2, 0)", "thirdTile=(3, 0)", ],
                ]
    print("""All the locations of the map with their x-y coordinates
    are printed below:
    """)
    print(gamemap_2)

def main_map_2():
  try:
    main_map()
  except ImportError:
    print("There is an error with importing the file")
    main_map()

def main_map_3():
  try:
    map_temple()
  except ImportError:
    print("There is an error with importing the file")
    map_temple()