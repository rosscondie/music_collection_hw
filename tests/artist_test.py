import unittest
from models.artist import Artist

class TestArtist(unittest.TestCase):
    def setUp(self):
        self.artist = Artist("James", "Hetfield")

    def test_artist_has_first_name(self):
        self.assertEqual("James", self.artist.first_name)

    def test_artist_has_last_name(self):
        self.assertEqual("Hetfield", self.artist.last_name)

    def test_artist_id_starts_as_none(self):
        self.assertEqual(None, self.artist.id)
