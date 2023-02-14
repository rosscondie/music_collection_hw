import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Elvis", "Presley")
artist_repository.save(artist_1)


album_1 = Album("Jailhouse Rock", "Rock")
album_repository.save(album_1)


result = album_repository.select_all()

for album in result:
    print(album.__dict__)

pdb.set_trace()