# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, location, description, n_to=None, e_to=None, s_to=None, w_to=None):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.e_to = e_to
        self.s_to = s_to
        self.w_to = w_to
        self.doors = []
        
    def Doors(self):
        if self.n_to is not None:
            self.doors.append('n')
            print(f'Room {self.name} has a door to the N')
        if self.e_to is not None:
            self.doors.append('e')
            print(f'Room {self.name} has a door to the E')
        if self.s_to is not None:
            self.doors.append('s')
            print(f'Room {self.name} has a door to the S')
        if self.w_to is not None:
            self.doors.append('w')
            print(f'Room {self.name} has a door to the W')
        return self.doors

    def __str__(self):
        return f'current location: {self.name}, {self.description}'