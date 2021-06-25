import unittest
from src.room import *
from src.guest import *
from src.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(1, 6)

    def test_room_has_number(self):
        #This test checks that given the Room object created above, the room.name property has been correctly setup matching 1
        self.assertEqual(1, self.room1.room_number)

    def test_room_has_capacity(self):
        #This test checks that given the Room object created above, the room.cpacity property has been correctly setup matching 6
        self.assertEqual(6, self.room1.capacity)

    def test_room_starts_with_0_guest(self):
        #This test checks that given the Room object created above, the room.guests_in_room property has been correctly setup as an empty list
        self.assertEqual([], self.room1.guests_in_room)

    def test_room_starts_with_no_songs_in_track(self):
        #This test checks that given the Room object created above, the room.guests_in_room property has been correctly setup as an empty list
        self.assertEqual([], self.room1.soundtrack)

    def test_room_can_check_in_guests(self):
        #This test checks that the check_in_guest() function is working correctly, by appending a guest object onto the guests in room list
        Guest_1 = Guest("Loki")
        Guest_2 = Guest("Thor")
        self.room1.check_in_guest(Guest_1)
        self.room1.check_in_guest(Guest_2)
        self.assertEqual(2, len(self.room1.guests_in_room))
        self.assertEqual("Loki", self.room1.guests_in_room[0].name)
        self.assertEqual("Thor", self.room1.guests_in_room[1].name)