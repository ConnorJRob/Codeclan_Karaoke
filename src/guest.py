import pdb

class Guest:
    def __init__(self,name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song

    def guest_pay_entry_fee(self, room):
        self.wallet -= room.entry_fee