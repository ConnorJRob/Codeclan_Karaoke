import pdb

class Room:
    def __init__(self,room_number, capacity, entry_fee):
        self.room_number = room_number
        self.capacity = capacity
        self.guests_in_room = []
        self.soundtrack = []
        self.entry_fee = entry_fee

    def check_in_guest(self,guest):
        #Function checks if the value of the guest.wallet property is sufficient to pay the entry fee, returning a string and processing no further if not
        if guest.wallet < self.entry_fee:
            return "I'm sorry, you do not have sufficient funds to pay the entry fee"
        #If guest has sufficient funds, it then checks if the room is at capacity or not, returning a string if not and progressing no further if so
        elif len(self.guests_in_room) == self.capacity:
            return "I'm sorry, this room is at full capacity"
        else:
        #If the guest had sufficient funds and there was space in the room for them, they are added to the room list and their entry fee is taken
            self.guests_in_room.append(guest)
            guest.guest_pay_entry_fee(self)

    def add_song_to_room_soundtrack(self,song):
        #The song specified is added to the rooms soundtrack
        self.soundtrack.append(song)

    def find_guest_by_name_in_room(self,guest_name):
        #The function searches through the guests in the room for a guest.name matching the string provided, returning the guest object if so
        for guest in self.guests_in_room:
            if guest.name == guest_name:
                return guest

    def check_out_guest(self, guest_name):
        #Function uses the find guest by name function to locate the guest within the list using the string name given and then removes their object from the list
        self.guests_in_room.remove(self.find_guest_by_name_in_room(guest_name))

    def check_out_all_guests_in_room(self):
        #Function checks all guests out of the room by calling the .clear() method on the guests_in_room list
        self.guests_in_room.clear()
