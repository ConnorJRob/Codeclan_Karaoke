import pdb

class Room:
    def __init__(self,room_number, capacity):
        self.room_number = room_number
        self.capacity = capacity
        self.guests_in_room = []
        self.soundtrack = []

    def check_in_guest(self,guest):
        self.guests_in_room.append(guest)

    def add_song_to_room_soundtrack(self,song):
        self.soundtrack.append(song)

    def find_guest_by_name_in_room(self,guest_name):
        for guest in self.guests_in_room:
            if guest.name == guest_name:
                return guest

    def check_out_guest(self, guest_name):
        self.guests_in_room.remove(self.find_guest_by_name_in_room(guest_name))

    def check_out_all_guests_in_room(self, room):
        self.guests_in_room.clear()