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

    'A1': Room('A1', "Room A1", """On the floor in the center of the room is an engraving: A1. There is passage to the East """),
    'B1': Room('B1', "Room B1", """On the floor in the center of the room is an engraving: B1. There is a passage to the West, North, and East """),
    'C1': Room('C1', "Room C1", """On the floor in the center of the room is an engraving: C1. There is a passage to the West, and East """),
    'D1': Room('D1', "Room D1", """On the floor in the center of the room is an engraving: D1. There is a passage to the West, and East """),
    'E1': Room('E1', "Room E1", """On the floor in the center of the room is an engraving: E1. There is a passage to the West """),
    'A2': Room('A2', "Room A2", """On the floor in the center of the room is an engraving: A2. There is a passage to the East """),
    'B2': Room('B2', "Room B2", """On the floor in the center of the room is an engraving: B2. There is a passage in all four directions """),
    'C2': Room('C2', "Room C2", """On the floor in the center of the room is an engraving: C2. There is a passage to the West, and East """),
    'D2': Room('D2', "Room D2", """On the floor in the center of the room is an engraving: D2. There is a passage to the West """),
    'E2': Room('E2', "Room E2", """On the floor in the center of the room is an engraving: E2. There is a passage to the North """),
    'A3': Room('A3', "Room A3", """On the floor in the center of the room is an engraving: A3. There is a passage to the East"""),
    'B3': Room('B3', "Room B3", """On the floor in the center of the room is an engraving: B3. There is a passage to the West, East, and South """),
    'C3': Room('C3', "Room C3", """On the floor in the center of the room is an engraving: C3. There is a passage to the West, North, and East """),
    'D3': Room('D3', "Room D3", """On the floor in the center of the room is an engraving: D3. There is a passage to the West, and East """),
    'E3': Room('E3', "Room E3", """On the floor in the center of the room is an engraving: E3. There is a passage to the West, and South """),
    'A4': Room('A4', "Room A4", """On the floor in the center of the room is an engraving: A4. There is a passage to the East """),
    'B4': Room('B4', "Room B4", """On the floor in the center of the room is an engraving: B4. There is a passage to the West, and East """),
    'C4': Room('C4', "Room C4", """On the floor in the center of the room is an engraving: C4. There is a passage to the West, East, and South"""),
    'D4': Room('D4', "Room D4", """On the floor in the center of the room is an engraving: D4. There is a passage to the West, and East"""),
    'E4': Room('E4', "Room E4", """On the floor in the center of the room is an engraving: E4. There is a passage to the West, and North"""),
    'E5': Room('E5', "Room E5", """You've exited the maze!""")
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

room['A1'].e_to = room['B1']
room['B1'].w_to = room['A1']
room['B1'].n_to = room['B2']
room['B1'].e_to = room['C1']
room['C1'].w_to = room['B1']
room['C1'].e_to = room['D1']
room['D1'].w_to = room['C1']
room['D1'].e_to = room['E1']
room['E1'].w_to = room['D1']
room['A2'].e_to = room['B2']
room['B2'].w_to = room['A2']
room['B2'].n_to = room['B3']
room['B2'].e_to = room['C2']
room['B2'].s_to = room['B1']
room['C2'].w_to = room['B2']
room['C2'].e_to = room['D2']
room['D2'].w_to = room['C2']
room['E2'].n_to = room['E3']
room['A3'].e_to = room['B3']
room['B3'].w_to = room['A3']
room['B3'].e_to = room['C3']
room['B3'].s_to = room['B2']
room['C3'].w_to = room['B3']
room['C3'].n_to = room['C4']
room['C3'].e_to = room['D3']
room['D3'].w_to = room['C3']
room['D3'].e_to = room['E3']
room['E3'].w_to = room['D3']
room['E3'].s_to = room['E2']
room['A4'].e_to = room['B4']
room['B4'].w_to = room['A4']
room['B4'].e_to = room['C4']
room['C4'].w_to = room['B4']
room['C4'].e_to = room['D4']
room['C4'].s_to = room['C3']
room['D4'].w_to = room['C4']
room['D4'].e_to = room['E4']
room['E4'].n_to = room['E5']
# Create Items (works)

item = {
    'torch': Item('torch', 'Lights the way!'),
    'test': Item('test', 'Tests the system!')
}

# Add Items to rooms (works)

room['foyer'].AddItemToRoom(item['torch'])
room['A1'].AddItemToRoom(item['torch'])
room['A1'].AddItemToRoom(item['test'])

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
#player = Player(name, room['outside'])
player = Player(name, room['A1'])
print('[q] to quit, [n,e,s,w] to move, [help] for more')
while True:
    cmd = input(f'{player}, enter a command... ').split(' ')

    if len(cmd) == 1:
        if cmd[0] == 'q':
            exit(0)
        if cmd[0] == 'n':
            if player.current_room.n_to:
                player.current_room = player.current_room.n_to
                print(f'{player.current_room.description}')
            else:
                print('There is no path in that direction!')
        if cmd[0] == 'e':
            if player.current_room.e_to:
                player.current_room = player.current_room.e_to
                print(f'{player.current_room.description}')
            else:
                print('There is no path in that direction!')
        if cmd[0] == 's':
            if player.current_room.s_to:
                player.current_room = player.current_room.s_to
                print(f'{player.current_room.description}')
            else:
                print('There is no path in that direction!')
        if cmd[0] == 'w':
            if player.current_room.w_to:
                player.current_room = player.current_room.w_to
                print(f'{player.current_room.description}')
            else:
                print('There is no path in that direction!')
        if cmd[0] == 'help':
            print('[use $ITEM] to use an item\n[drop $ITEM] to drop item\n[take $ITEM] to take item\n[use $ITEM] to use item')
        if cmd[0] == 'cheat':
            pass
        if cmd[0] == 'look':
            if item['torch'] in player.Items():
                room[Player.Location(player)].ListItems()
            else:
                print('Good luck finding anything in the dark!')
        else:
            pass

    if len(cmd) == 2:
        itemcmd = cmd[1]
        if cmd[0] == 'take':
            if item['torch'] in player.Items():
                if item[itemcmd] in player.current_room.Items():
                    player.current_room.AddItemToPlayer(item[itemcmd], player)
                else:
                    print(f'Didnt find {itemcmd}')
            elif itemcmd == 'torch':
                #print(room[Player.Location(player)].Items()) # Prints OBJECT
                if item[itemcmd] in player.current_room.Items():
                    #print(room[Player.Location(player)].Items()) # Prints nothing
                    player.current_room.AddItemToPlayer(item[itemcmd], player)
            else:
                print('Good Luck finding that in the dark!')
        elif cmd[0] == 'drop':
            pass
        elif cmd[0] == 'use':
            if item in player.items:
                if item.name == 'torch':
                    player.current_room.listItems()
                else:
                    pass
        else:
            pass