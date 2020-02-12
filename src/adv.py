from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
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

player = Player('Conrad', room['outside'])
print(f'Hello {player.name}! You are currently located at {player.current_room.location}')

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


while True:
    
    movement = input(" \n Please input n, s, e, or w to move or press q to quit ~~> ")

    if(movement == "n"):
        if (player.current_room.n_to is not None):
            player.current_room = player.current_room.n_to
            print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n')
        elif(player.current_room.m_to is None):
            print("\n There is no room in that direction \n")
    
    if(movement == 's'):
        if(player.current_room.s_to is not None):
            player.current_room = player.current_room.s_to
            print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n')
        elif(player.current_room.s_to is None):
            print("\n There is no room in that direction \n")

    if(movement == 'e'):
        if(player.current_room.e_to is not None):
            player.current_room = player.current_room.e_to
            print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n') 
        elif(player.current_room.e_to is None):
            print("\n There is no room in that direction \n")
    
    if(movement == 'w'):
        if(player.current_room.w_to is not None):
            player.current_room = player.current_room.w_to
            print(f'\n {player.name} is in the {player.current_room.location}. {player.current_room.description} \n')
        elif(player.current_room.w_to is None):
            print("\n There is no room in that direction \n")

    if (movement == "q"):
        print("good bye")
        exit()

    else:
        print("Please press n, s, e, or w to continue playing. Press q to quit.")