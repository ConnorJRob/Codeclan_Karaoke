import pdb

class Room:
    def __init__(self,room_number, capacity, entry_fee):
        self.room_number = room_number
        self.capacity = capacity
        self.guests_in_room = []
        self.soundtrack = []
        self.entry_fee = entry_fee

    def check_in_guest(self,guest):
        if guest.wallet < self.entry_fee:
            return "I'm sorry, you do not have sufficient funds to pay the entry fee"
        elif len(self.guests_in_room) == self.capacity:
            return "I'm sorry, this room is at full capacity"
        else:
            self.guests_in_room.append(guest)
            guest.guest_pay_entry_fee(self)

    def add_song_to_room_soundtrack(self,song):
        self.soundtrack.append(song)

    def find_guest_by_name_in_room(self,guest_name):
        for guest in self.guests_in_room:
            if guest.name == guest_name:
                return guest

    def check_out_guest(self, guest_name):
        self.guests_in_room.remove(self.find_guest_by_name_in_room(guest_name))

    def check_out_all_guests_in_room(self):
        self.guests_in_room.clear()
