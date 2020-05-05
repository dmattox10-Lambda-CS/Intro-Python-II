class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'You are holding a/an {self.name}, it {self.description}'

class Key(Item):
    def __init__(self, name, description, door):
        super().__init__(name, description)
        self.door = door