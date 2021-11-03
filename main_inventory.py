# This inventory is paired with specific characters
inventory = {"Batman": {"Night Vision Goggles":
                        {"description": """ Use the Night Vision Goggles to see
                        in the dark and find your way """, }},
             "Green Lantern": {"Power Ring":
                               {"description":
                                "Use it as a flashlight to find their way", }}}

# This dictionary includes the descriptions of Batman


character = {"Batman":
             {"description":
              """I am a vigilante and my real name is Bruce Wayne!
              """}}

# This dictionary includes the description of Green Lantern


character_2 = {"Green Lantern":
               {"description":
                "My name is Hal Jordan. I come from the Planet Mogo"}}


def player_inventory(player, inventory):
    """Print out the inventory for the choosen character"""
    for item in inventory[player]:
        description = inventory[player][item]["description"]
        print(f"{player}'s {item} - {description}")


def character_inventory(player, character):
    """ prints out the description for Batman """
    for item in character[player]:
        description = character[player]["description"]
        print(f"{player}'s {item} - {description}")


def character_inventory_2(player_2, character_2):
    """ prints out the description for Green Lantern """
    for item in character_2[player_2]:
        description_2 = character_2[player_2]["description"]
        print(f"{player_2}'s {item} - {description_2}")
