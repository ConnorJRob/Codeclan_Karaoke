import unittest
from src.room import *
from src.guest import *
from src.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room(1, 6)

    def test_room_has_number(self):
        #This test checks that given the Room object created above, the room.name property has been correctly setup matching 1
        self.assertEqual(1, self.room.room_number)

    def test_room_has_capacity(self):
        #This test checks that given the Room object created above, the room.cpacity property has been correctly setup matching 6
        self.assertEqual(6, self.room.capacity)

    def test_room_starts_with_0_guest(self):
        #This test checks that given the Room object created above, the room.guests_in_room property has been correctly setup as an empty list
        self.assertEqual([], self.room.guests_in_room)