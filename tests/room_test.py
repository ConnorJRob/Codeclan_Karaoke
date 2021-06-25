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
        guest_1 = Guest("Loki")
        guest_2 = Guest("Thor")
        self.room1.check_in_guest(guest_1)
        self.room1.check_in_guest(guest_2)
        self.assertEqual(2, len(self.room1.guests_in_room))
        self.assertEqual("Loki", self.room1.guests_in_room[0].name)
        self.assertEqual("Thor", self.room1.guests_in_room[1].name)

    def test_room_can_add_songs_to_soundtrack(self):
        #This test checks that add_song_to_room_soundtrack() function is working correctly, by appending a song object onto the soundtrack list
        song_1 = Song("The Eye of the Tiger")
        song_2 = Song("It's my life")
        self.room1.add_song_to_room_soundtrack(song_1)
        self.room1.add_song_to_room_soundtrack(song_2)
        self.assertEqual(2, len(self.room1.soundtrack))
        self.assertEqual("The Eye of the Tiger", self.room1.soundtrack[0].song_name)
        self.assertEqual("It's my life", self.room1.soundtrack[1].song_name)

    def test_find_guest_by_name_in_room(self):
        #This test checks the function find_guest_by_name_in_room which will be called by other functions, the function should take a string and if this matches a guest.name property that is
        ##curretly in the room.guests_in_room[] list then it returns that guest object
        guest_1 = Guest("Loki")
        guest_2 = Guest("Thor")
        self.room1.check_in_guest(guest_1)
        self.room1.check_in_guest(guest_2)
        searched_guest = self.room1.find_guest_by_name_in_room("Thor")
        self.assertEqual("Thor", searched_guest.name)