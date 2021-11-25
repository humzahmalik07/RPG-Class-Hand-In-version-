# valid directions and actions to move

valid_actions = ["forward", "backward", "left", "right", "quit"]


# valid action or hint for Batman


valid_actions_2 = ["goggles"]

# valid action or hint for Green Lantern


valid_hint = ["ring"]


def menu():
    """ Prints out the menu for all the possible valid actions """
    print("""Choose an action:
    """)
    for action in valid_actions:
        print(f"* {action}")



def menu_2():
    """This defines the menu for the hint for Batman"""
    try:
      for action in valid_actions_2:
        print(f"* {action}")
    except IndexError:
      print("Error")
      menu_2()

def menu_3():
    """This defines the menu for the hint for Green Lantern"""
    try:
      for action in valid_hint:
        print(f"* {action}")
    except IndexError:
      print("Error")
      menu_3()

def end_script():
    """This function prints out the ending message of the game"""
    print("""
    You have successfully escaped out of the temple and
    you have completed the game.
    """)


def action_1():
    """ Prints out the menu for input action to move in the map
    at Level 1 for Batman """
    print("""
      LEVEL 1
      """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Wall ahead ")
        action_1()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_1()
    if action_input.lower() in valid_actions[2]:
        print(f" You are turning to the left side of the temple")
        action_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_1()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for your next direction.
            The direction is left. Enter left when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_1()


def action_2():
    """ Prints out the menu for input action to move in the map
    at Level 2 for Batman"""
    print("""
        LEVEL 2
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead ")
        action_3()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_2()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_2()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_2()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_2()


def action_3():
    """ Prints out the menu for input action to move in the map
    at Level 3 for Batman"""
    print("""
        LEVEL 3
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead")
        action_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_3()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_3()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_3()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_3()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_3()


def action_4():
    """ Prints out the menu for input action to move in the map
    at Level 4 for Batman"""
    print("""
        LEVEL 4
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Dead end ")
        action_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_4()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_4()
    if action_input.lower() in valid_actions[3]:
        print(f" Turn right to walk towards the exit ")
        action_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_4()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_4()


def action_5():
    """ Prints out the menu for input action to move in the map
    at Level 5 for Batman"""
    print("""
        LEVEL 5
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        action_6()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_5()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_5()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_5()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_5()


def action_6():
    """ Prints out the menu for input action to move in the map
    at Level 6 for Batman"""
    print("""
        LEVEL 6
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        action_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_6()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_6()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_6()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_6()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_6()


def action_7():
    """ Prints out the menu for input action to move in the map
    at Level 7 for Batman"""
    print("""
        LEVEL 7
        """)
    menu()
    menu_2()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        action_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_7()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_7()
    if action_input.lower() in valid_actions[3]:
        print(f" turn right towards the exit ")
        action_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_7()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_7()


def action_8():
    """ Prints out the menu for input action to move in the map
    at Level 8 for Batman"""
    print("""
        LEVEL 8
        """)
    menu()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Go forward ")
        action_9()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_8()
    if action_input.lower() in valid_actions[2]:
        print(f" wall ahead")
        action_8()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_8()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_8()


def action_9():
    """ Prints out the menu for input action to move in the map
    at Level 9 for Batman"""
    print("""
        LEVEL 9
        """)
    menu()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f""" Go forward. You are getting closer! """)
        action_10()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_9()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        action_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_9()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward.
            Enter forward when the menu restarts."""
              )
        action_9()
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_9()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_9()


def action_10():
    """ Prints out the menu for input action to move in the map
    at Level 10 for Batman"""
    print("""
        LEVEL 10
        """)
    menu()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" You found the exit!! ")
        end_script()
        quit()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        action_10()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead ")
        action_10()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        action_10()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_actions_2[0]:
        print(f""" You have chosen to use the Night Vision Goggles.
            This gives you a hint for you next direction.
            The direction is forward. Enter forward when the menu restarts.""")
    if action_input.lower not in valid_actions_2:
        print("Invalid direction!")
        action_10()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        action_10()


def actions_1():
    """ Prints out the menu for input action to move in the map
    at Level 1 for Green Lantern """
    print("""
      LEVEL 1
      """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Wall ahead ")
        actions_1()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_1()
    if action_input.lower() in valid_actions[2]:
        print(f" You are turning to the left side of the temple")
        actions_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_1()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used as a flashlight
      and gives you a hint for you next direction.
            The direction is left. Enter left when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_1()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_1()


def actions_2():
    """ Prints out the menu for input action to move in the map
    at Level 2 for Green Lantern """
    print("""
        LEVEL 2
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead ")
        actions_3()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_2()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_2()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_2()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used as a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_2()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_2()


def actions_3():
    """ Prints out the menu for input action to move in the map
    at Level 3 for Green Lantern """
    print(""""
        LEVEL 3
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking ahead")
        actions_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_3()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_3()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_3()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Power Ring.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_3()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_3()


def actions_4():
    """ Prints out the menu for input action to move in the map
    at Level 4 for Green Lantern """
    print("""
        LEVEL 4
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Dead end ")
        actions_4()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_4()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_4()
    if action_input.lower() in valid_actions[3]:
        print(f" Turn right to walk towards the exit ")
        actions_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_4()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_4()


def actions_5():
    """ Prints out the menu for input action to move in the map
    at Level 5 for Green Lantern """
    print("""
        LEVEL 5
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        actions_6()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_5()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_5()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_5()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_5()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_5()


def actions_6():
    """ Prints out the menu for input action to move in the map
    at Level 6 for Green Lantern """
    print("""
        LEVEL 6
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Keep walking")
        actions_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_6()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_6()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_6()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_6()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_6()


def actions_7():
    """ Prints out the menu for input action to move in the map
    at Level 7 for Green Lantern """
    print("""
        LEVEL 7
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" wall ahead ")
        actions_7()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_7()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_7()
    if action_input.lower() in valid_actions[3]:
        print(f" turn right towards the exit ")
        actions_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
            The direction is right. Enter right when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_7()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_7()


def actions_8():
    """ Prints out the menu for input action to move in the map
    at Level 8 for Green Lantern """
    print("""
        LEVEL 8
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f" Go forward ")
        actions_9()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_8()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_8()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_8()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
      The direction is forward.
      Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_8()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_8()


def actions_9():
    """ Prints out the menu for input action to move in the map
    at Level 9 for Green Lantern """
    print("""
        LEVEL 9
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f""" Go forward. You are getting closer """)
        actions_10()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_9()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_9()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_9()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_9()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_9()


def actions_10():
    """ Prints out the menu for input action to move in the map
    at Level 10 for Green Lantern """
    print("""
        LEVEL 10
        """)
    menu()
    menu_3()
    action_input = input("Action: ")
    if action_input.lower() in valid_actions[0]:
        print(f""" You have found the exit!! """)
        end_script()
        quit()
    if action_input.lower() in valid_actions[1]:
        print(f" Wrong way! ")
        actions_10()
    if action_input.lower() in valid_actions[2]:
        print(f" Wall ahead")
        actions_10()
    if action_input.lower() in valid_actions[3]:
        print(f" Wall ahead ")
        actions_10()
    if action_input.lower() in valid_actions[4]:
        print(" You have quit the game ")
        quit()
    if action_input.lower() in valid_hint[0]:
        print("""You have chosen to use the Night Vision Goggles.
      This ring is used a flashlight
      and gives you a hint for you next direction.
    The final direction is forward. Enter forward when the menu restarts. """)
    if action_input.lower not in valid_hint:
        print("Invalid direction!")
        actions_10()
    elif action_input.lower not in valid_actions:
        print("Invalid direction!")
        actions_10()
