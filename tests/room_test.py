import unittest
from src.room import *
from src.guest import *
from src.song import *

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room1 = Room(1, 6, 4.00)
        self.room2 = Room(1, 3, 5.00)
 
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
        guest_1 = Guest("Loki", 15.00)
        guest_2 = Guest("Thor", 20.00)
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
        guest_1 = Guest("Loki", 15.00)
        guest_2 = Guest("Thor", 20.00)
        self.room1.check_in_guest(guest_1)
        self.room1.check_in_guest(guest_2)
        searched_guest = self.room1.find_guest_by_name_in_room("Thor")
        self.assertEqual("Thor", searched_guest.name)

    def test_check_out_guest(self):
        #This test checks that the check_out_guest function is working correctly, when given a name string it uses the find_guest_by_name_in_room function to locate a matching guest, then removes them from
        ## the guests_in_room list
        guest_1 = Guest("Loki", 15.00)
        guest_2 = Guest("Thor", 20.00)
        self.room1.check_in_guest(guest_1)
        self.room1.check_in_guest(guest_2)
        self.room1.check_out_guest("Thor")
        self.assertEqual(1, len(self.room1.guests_in_room))

    def test_check_out_all_guests_in_room(self):
        #This test checks that the check_out_all_guests_in_room() function is working correctly, when this is called for a room, it clears the entire guests_in_room list
        guest_1 = Guest("Loki", 15.00)
        guest_2 = Guest("Thor", 20.00)
        guest_3 = Guest("Odin", 19.00)
        self.room1.check_in_guest(guest_1)
        self.room1.check_in_guest(guest_2)
        self.room1.check_in_guest(guest_3)
        self.room1.check_out_all_guests_in_room()
        self.assertEqual(0, len(self.room1.guests_in_room))

    def test_room_will_not_go_over_capacity(self):
        #This test checks that the updated "check_in_guest" functionality is working - t checks if the room is at the established capacity, if so it returns a string and does not append the guest
        guest_1 = Guest("Loki", 15.00)
        guest_2 = Guest("Thor", 20.00)
        guest_3 = Guest("Odin", 19.00)
        guest_4 = Guest("Tyr", 13.00)
        self.room2.check_in_guest(guest_1)
        self.room2.check_in_guest(guest_2)
        self.room2.check_in_guest(guest_3)
        self.room2.check_in_guest(guest_4)
        self.assertEqual(3, len(self.room2.guests_in_room))
        self.assertEqual("I'm sorry, this room is at full capacity", self.room2.check_in_guest(guest_4))

    def test_check_guest_in_and_take_payment(self):
        guest_1 = Guest("Loki", 15.00)
        self.room2.check_in_guest(guest_1)
        self.assertEqual(10, guest_1.wallet)

    def test_deny_guest_check_in_due_to_insufficient_funds(self):
        guest_1 = Guest("Thor", 4.00)
        self.assertEqual("I'm sorry, you do not have sufficient funds to pay the entry fee", self.room2.check_in_guest(guest_1))
