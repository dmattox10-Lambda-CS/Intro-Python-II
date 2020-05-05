# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room, items={}):
        self.name = name
        self.current_room = current_room
        self.items = items

    def AddItem(self, item):
        self.items.append(item)
        print(f'Got item {item.name}!')

    def Drop(self, item, room):
        if item in self.items:
            self.items.remove(item)
            room.AddItemToRoom(item)

    def HasLight(self):
        if 'torch' in self.items:
            return True
        else:
            return False

    def Move(self, room):
        self.current_room = room

    def Location(self):
        return self.current_room.name

    def Surroundings(self):
        return self.current_room.description

    def __str__(self):
        return self.name