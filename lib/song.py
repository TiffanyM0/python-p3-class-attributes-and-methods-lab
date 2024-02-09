class Song:
    pass
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}


    def __init__(self, name, artist, genre) -> None:
        pass
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_to_genres(self.genre)
        Song.add_song_to_count(artist)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)



    @classmethod
    def add_song_to_count(cls, artist):
        pass
        Song.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        pass
        Song.genres.append(genre)

    
    @classmethod
    def add_to_artists(cls, artist):
        pass
        if artist not in Song.artists:
            Song.artists.append(artist)
        
    @classmethod
    def add_to_genre_count(cls, genre):
        pass
        if Song.genre_count.get(genre) is not None:
            new_num = Song.genre_count[genre] + 1
            Song.genre_count.update({genre : new_num})
        else:
            Song.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        pass
        if Song.artist_count.get(artist) is not None:
            new_num = Song.artist_count[artist] + 1
            Song.artist_count.update({artist : new_num})
        else:
            Song.artist_count[artist] = 1
        
        