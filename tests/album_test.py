import unittest
from models.album import Album

class TestAlbum(unittest.TestCase):
    def setUp(self):
        self.album = Album ("Ride the Lightning", "Metal")

    def test_album_has_title(self):
        self.assertEqual("Ride the Lightning", self.album.title)

    def test_album_has_genre(self):
        self.assertEqual("Metal", self.album.genre)

    def test_album_id_starts_as_none(self):
        self.assertEqual(None, self.album.id)