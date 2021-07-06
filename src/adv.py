from src.room import Room
from src.player import Player
from src.item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside to the Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# items
item = {
    "Longsword": Item("Sword", "A rune laden silver long sword lodged into a stone..still..."),

    "Flask": Item("Flask", "You cannot get ye flask..."),

    "Torch": Item("Torch", "A lit torch sits nicely on the wall."),

    "RustyKey": Item("RustyKey", "Rusty key, it's probably important..."),
}

room['outside'].get_item(item['Longsword'])
room['foyer'].get_item(item['Torch'])
room['overlook'].get_item(item['RustyKey'])
room['treasure'].get_item(item['Flask'])
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player = Player("You are currently ", room["outside"])

while True:

    player.current_room
    print("\n You are currently in the", player.current_room.name)
    print("\n", player.current_room.description)
    print("\n What do you do next? \n Proceed N, S, E, or W. Or search...")

    cmd = input(
        " Please enter your instructions. or enter q to quit on your adventure.").split(
        " ")
    command = cmd[0]

    if command == "q":
        print(
            "\n The adventure was too much for you. Try again once you're feeling                         adventurous.")
        break

    if command == "n":
        print("\n You proceed north... \n")
        if player.current_room.n_to is None:
            print("you cannot proceed that way, please try a different direction.")
        else:
            player.current_room = player.current_room.n_to

    elif command == "s":
        print("\n You venture south... \n")
        if player.current_room.s_to is None:
            print("you cannot proceed that way, please try a different direction.")
        else:
            player.current_room = player.current_room.s_to
    elif command == "w":
        print("\n You press on to the west...")
        if player.current_room.w_to is None:
            print("you cannot proceed that way, please try a different direction.")
        else:
            player.current_room = player.current_room.w_to

    elif command == "e":
        print("\n You journey east... \n")
        if player.current_room.e_to is None:
            print("you cannot proceed that way, please try a different direction.")
        else:
            player.current_room = player.current_room.e_to

    # ITEMS
    if command == "i":
        player.inventory()

    if command == "search":
        for item in player.current_room.items:
            print(f"\n You see a {item.name}, \n {item.description}")

            inv = player.current_room.items
            if len(inv) == 0:
                print(f"\n there it nothing of worth in this room.")

    if len(cmd) == 2:
        command = cmd[0]
        artifact = cmd[1]
        inv = player.current_room.items

        if command == "get":
            for item in inv:
                if artifact == getattr(item, "name"):
                    player.get_item(item)
                    player.current_room.drop_item(item)
                    print(f"\n You pick up the {artifact}")

                else:
                    print(f"\n You have already looted this room")

        if command == "drop":
            if len(player.items) > 0:
                for item in player.items:
                    if artifact == getattr(item, "name"):
                        player.drop_item(item)
                        print(f"\n You have removed {artifact} from your inventory")

else:
    print("\n THAT IS FORBIDDEN, MORTAL!")
