import unittest
from src.room import *
from src.guest import *
from src.song import *

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Loki", 15.00)

    def test_song_has_name(self):
        #This test checks that given the Guest object created above, the guest.name property has been correctly setup matching "Loki"
        self.assertEqual("Loki", self.guest_1.name)

    def test_guest_has_wallet(self):
        self.assertEqual(15.00, self.guest_1.wallet)

    def test_guest_pays_entry_fee(self):
        self.room_1 = Room(1, 6, 4.00)
        self.guest_1.guest_pay_entry_fee(self.room_1)
        self.assertEqual(11.00, self.guest_1.wallet)
        
        