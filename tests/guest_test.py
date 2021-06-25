import unittest
from src.room import *
from src.guest import *
from src.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Loki", 15.00, "It's my life")

    def test_song_has_name(self):
        #This test checks that given the Guest object created above, the guest.name property has been correctly setup matching "Loki"
        self.assertEqual("Loki", self.guest_1.name)

    def test_guest_has_wallet(self):
        #This test checks that given the Guest object created above, the guest.wallet property has been correctly setup matching 15.00
        self.assertEqual(15.00, self.guest_1.wallet)

    def test_guest_has_favourite_song(self):
        #This test checks that given the Guest object created above, the guest.favourite_song property has been correctly setup matching "It's my life"
        self.assertEqual(15.00, self.guest_1.wallet)

    def test_guest_pays_entry_fee(self):
        self.room_1 = Room(1, 6, 4.00)
        self.guest_1.guest_pay_entry_fee(self.room_1)
        self.assertEqual(11.00, self.guest_1.wallet)
        
        