import unittest
from src.room import *
from src.guest import *
from src.song import *

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song_1 = Song("The Eye of the Tiger")

    def test_song_has_name(self):
        #This test checks that given the Room object created above, the room.name property has been correctly setup matching "The Eye of the Tiger"
        self.assertEqual("The Eye of the Tiger", self.song_1.song_name)