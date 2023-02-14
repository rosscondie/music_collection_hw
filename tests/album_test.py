import unittest
from models.album import Album

class TestAlbum(unittest. TestCase):
    def setUp(self):
        self.album = Album ("Ride the Lightning", "Metal")

    def test_album_has_title(self):
        self.assertEqual("Ride the Lightning", self.album.title)