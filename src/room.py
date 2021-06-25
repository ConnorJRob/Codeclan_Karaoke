import pdb

class Room:
    def __init__(self,room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.guests_in_room = []
        self.soundtrack = []

    def check_in_guest(self,guest):
        self.guests_in_room.append(guest)