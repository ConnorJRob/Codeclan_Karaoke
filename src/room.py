import pdb

class Room:
    def __init__(self,room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.guests_in_room = []