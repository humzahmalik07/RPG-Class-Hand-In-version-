# Course: CS 30
# Period: 2
# Date created: 19/09/21
# Date last modified: 21/09/21
# Name: Humzah Zahid Malik
# Description: Batman x Green Lantern - Temple Escape


import Characters
import os
import sys
import intro
import class_functions
import main_inventory
import maps

# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """ Use the Night Vision Goggles to see
                        in the dark and find your way """, }},
             "Green Lantern": {"Power Ring":
                               {"description":
                                "Use it as a flashlight to find their way", }}}

character_choice = input("Enter Batman or Green Lantern: ")
if character_choice == "Batman":
    intro.introduction_part_1()
    intro.introduction_part_2()
    maps.main_map()
    Characters.character_intro()
    Characters.batman_class()
    Characters.Batman_inventory()
    class_functions.firstTiles()
    main_inventory.player_inventory("Batman", inventory)
if character_choice == "Green Lantern":
    intro.introduction_part_1()
    intro.introduction_part_2()
    maps.main_map()
    Characters.character_intro_2()
    Characters.green_lantern_class()
    Characters.Green_lantern_inventory()
    main_inventory.player_inventory("Green Lantern", inventory)
    class_functions.firstTiles()
