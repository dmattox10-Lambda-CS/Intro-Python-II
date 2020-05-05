from room import Room
from player import Player
from item import Item, Key
# Declare all the rooms

room = {
    'outside':  Room('outside', "Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room('foyer', "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room('overlook', "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room('narrow', "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room('treasure', "Treasure Chamber", """You've found the long-lost treasure
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

# Create Items (works)

item = {
    'torch': Item('torch', 'Lights the way!')
}

# Add Items to rooms (works)

room['foyer'].AddItemToRoom(item['torch'])

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

name = input('Enter your name... ')
player = Player(name, room['outside'])
print('[q] to quit, [n,e,s,w] to move, [help] for more')
while True:
    output = player.Surroundings()
    print(f'{output}')

    cmd = input(f'{player}, enter a command... ').split(' ')

    if len(cmd) == 1:
        if cmd[0] == 'q':
            exit(0)
        if cmd[0] == 'n':
            if 'n' in room[Player.Location(player)].Doors():
                player.Move(room[Player.Location(player)].n_to)
        if cmd[0] == 'e':
            if 'e' in room[Player.Location(player)].Doors():
                player.Move(room[Player.Location(player)].e_to)
        if cmd[0] == 's':
            if 's' in room[Player.Location(player)].Doors():
                player.Move(room[Player.Location(player)].s_to)
        if cmd[0] == 'w':
            if 'w' in room[Player.Location(player)].Doors():
                player.Move(room[Player.Location(player)].w_to)
        if cmd[0] == 'help':
            print('[use $ITEM] to use an item\n[drop $ITEM] to drop item\n[take $ITEM] to take item\n[use $ITEM] to use item')
        if cmd[0] == 'cheat':
            room[Player.Location(player)].ListItems()
            room[Player.Location(player)].ListDoors()
        else:
            pass

    if len(cmd) == 2:
        item = cmd[1]
        if cmd[0] == 'take':
            if player.HasLight():
                pass
            elif item == 'torch':
                print(room[Player.Location(player)].Items()) # Prints OBJECT
                if item in room[Player.Location(player)].Items():
                    print(room[Player.Location(player)].Items()) # Prints nothing
                    room[Player.Location(player)].AddItemToPlayer(item[item])
            else:
                print('Good Luck finding that in the dark!')
        elif cmd[0] == 'drop':
            pass
        elif cmd[0] == 'use':
            if item in player.items:
                if item.name == 'torch':
                    room[Player.Location(player)].listItems()
                    room[Player.Location(player)].listDoors()
                else:
                    pass
        else:
            pass