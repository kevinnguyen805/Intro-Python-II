from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("sword", "bfs"), Item("dagger", "the one Arya Stark used, but kind of dull") ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("wand", "magical, but also a good dog chewtoy"), Item("talking hat", "sassier than the one in Harry Potter")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("bow", "unlimited ammo"), Item("crossbow", "lethal arrows")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("throwing stars", "how good of a throwing arm do you have?"), Item("apron", "healing powers")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("body armor", "you'll become an unmovable force"), Item("shield", "blocks damage")]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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

""" function to print out each item individually from the list """
def print_items(visible_items):
    for item in visible_items:
        print(f'In the room, you see a {item.item}. {item.item_description}')


""" initial character rendering """ 
player = Player('Conrad', room['outside'], [])
# player = Player(input('What is your name?', room['outside']))
print(f' \nHello {player.name}! You are currently located at {player.current_room.location}.')
print_items(player.current_room.items_in_room)


while True:
    
    movement = input(" \n Please input n, s, e, or w to move or press q to quit ~~>")
    # action = input("Take any items in the room by typing take item_name  ~~> ")

    if(len(movement.split())) > 1:
        print(movement.split())            # returns a list of each string input
        # if length of list is greater than 1 - that means it is a verb command
        if (movement.split()[0] == 'take' or movement.split()[0] == 'get'):
            action = movement.split()[1:]         #grabbing the item we want  - where are we grabbing the item?
            print(" ".join(action))                # "space between each word".join(method)
            player.take_item(" ".join(action))     # we have to grab 1: because talking hat is two words

        if(movement.split()[0] == 'drop'):
            action = movement.split()[1:]
            print(" ".join(action))
            player.drop_item(" ".join(action))
        # if length of list is 1 - that is a directional command 
    elif(movement == "i" or movement == 'inventory'):
        for item in player.items_in_inventory:
            print(f'In your inventory, you have a {item.item}')

    elif(movement == "n"):
        if (player.current_room.n_to is not None):
            player.current_room = player.current_room.n_to
            print(f'\n {player.name} is in the {player.current_room.location}. \n {player.current_room.description} \n')
            print_items(player.current_room.items_in_room)
        elif(player.current_room.m_to is None):
            print("\n There is no room in that direction \n")
    
    elif(movement == 's'):
        if(player.current_room.s_to is not None):
            player.current_room = player.current_room.s_to
            print(f'\n {player.name} is in the {player.current_room.location}. \n {player.current_room.description} \n')
            print_items(player.current_room.items_in_room)
        elif(player.current_room.s_to is None):
            print("\n There is no room in that direction \n")

    elif(movement == 'e'):
        if(player.current_room.e_to is not None):
            player.current_room = player.current_room.e_to
            print(f'\n {player.name} is in the {player.current_room.location}. \n {player.current_room.description} \n')
            print_items(player.current_room.items_in_room)
        elif(player.current_room.e_to is None):
            print("\n There is no room in that direction \n")
    
    elif(movement == 'w'):
        if(player.current_room.w_to is not None):
            player.current_room = player.current_room.w_to
            print(f'\n {player.name} is in the {player.current_room.location}. \n {player.current_room.description} \n')
            print_items(player.current_room.items_in_room)
        elif(player.current_room.w_to is None):
            print("\n There is no room in that direction \n")

    elif (movement == "q"):
        print("good bye")
        exit()

    else:
        print("Please press n, s, e, or w to continue playing. Press q to quit.")





# INITIATE REPL (read, evaluate, print, loop)
# while True:
    
#     movement = input(" \n Please input n, s, e, or w to move or press q to quit ~~> ")

#     if(movement == "n"):
#         if (player.current_room.n_to != None):
#             player.current_room = player.current_room.n_to
#             print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n')
#         elif(player.current_room.m_to == None):
#             print("\n There is no room in that direction \n")
    
#     if(movement == 's'):
#         if(player.current_room.s_to != None):
#             player.current_room = player.current_room.s_to
#             print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n')
#         elif(player.current_room.s_to == None):
#             print("\n There is no room in that direction \n")

#     if(movement == 'e'):
#         if(player.current_room.e_to != None):
#             player.current_room = player.current_room.e_to
#             print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n') 
#         elif(player.current_room.e_to == None):
#             print("\n There is no room in that direction \n")
    
#     if(movement == 'w'):
#         if(player.current_room.w_to != None):
#             player.current_room = player.current_room.w_to
#             print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n')
#         elif(player.current_room.w_to == None):
#             print("\n There is no room in that direction \n")

#     if (movement == "q"):
#         print("good bye")
#         exit()

#     else:
#         print("Please press n, s, e, or w to continue playing. Press q to quit.")