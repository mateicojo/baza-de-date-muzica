class Record:
    def __init__(self, id_record, key, bpm, genre, is_major, beats_per_bar, name, producer, artist, album, has_feat):
        self.__id_record = id_record
        self.__key = key
        self.__bpm = bpm
        self.__genre = genre
        self.__is_major = is_major
        self.__beats_per_bar = beats_per_bar
        self.__name = name
        self.__producer = producer
        self.__artist = artist
        self.__album = album
        self.__has_feat = has_feat

    def __str__(self):
        return f"The record is called {self.__name}, produced by {self.__producer} from the {self.__album} album, bpm: {self.__bpm}"

    def set_bpm(self, new_bpm):
        self.__bpm = new_bpm

    def get_bpm(self):
        return self.__bpm

    def set_genre(self, new_genre):
        if new_genre.upper() in ["HOUSE", "TECHNO", "TRANCE", "TECH-HOUSE"]:
            self.__genre = new_genre

    def get_genre(self):
        return self.__genre

    def get_id_record(self):
        return self.__id_record


class Album:
    def __init__(self, id_album, name, artist):
        self.__id_album = id_album
        self.__name = name
        self.__artist = artist
        self.__records = {}

    def add_song(self, add_song):
        if add_song.get_id_record() in self.__records.keys():
            return
        self.__records[add_song.get_id_record()] = add_song

    def get_records(self):
        return self.__records


new_song = Record(1, "C", 130, "house", False, 4, "Sunset", "Alex", "", "Alex EP", False)
new_song2 = Record(2, "D", 130, "techno", False, 4, "Everyday", "Marcu", "", "Marcu LP", False)
new_song3 = Record(2, "E", 130, "techno", False, 4, "", "sit", "", "Marcu LP", False)
print(new_song)
new_song.set_bpm(150)
print(new_song)
print(new_song.get_bpm())
new_song.set_genre("tech-house")
print(new_song.get_genre())

new_album = Album(0, "FIFA", "EARGASM GOD")
new_album.add_song(new_song)
new_album.add_song(new_song2)
new_album.add_song(new_song3)
for song in new_album.get_records().values():
    print(song)
