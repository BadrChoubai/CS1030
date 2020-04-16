import random


class Playlist():

    def __init__(self, title: str, description=None, tracks=None):
        self.description = description
        self.title = title
        self.tracks = tracks

        if not description:
            self.description = ""

        if not tracks:
            self.tracks = []

    def add_tracks(self, new_tracks):
        if type(new_tracks) is list:
            self.tracks.extend(new_tracks)
        else:
            self.tracks.extend([new_tracks])

    def set_description(self, new_description):
        self.description = new_description

    def __repr__(self):
        return "Playlist('{}', '{}', '{}')".format(self.title, self.description, self.tracks)

    def __str__(self):
        return f"title: {self.title}\ndescription: {self.description}\ntrack list: {list(str(track) for track in self.tracks)}"


class Track():
    def __init__(self, album: str, artist: str, title: str, duration: int):
        self.album = album
        self.artist = artist
        self.title = title
        self.duration = duration

    def __repr__(self):
        return "Track('{}', '{}', '{}', '{}')".format(self.album, self.artist, self.title, self.duration)

    def __str__(self):
        return f"{self.title} - {self.artist} - {self.album}"


single_song = Track('Be the Cowbow', 'Mitski', 'Nobody', 193)
multiple_songs = [Track('Cardinal', 'Pinegrove', 'Aphasia', 271), Track(
    'Can\'t Wake Up', 'Shakey Grave', 'Climb On the Cross', 249)]


playlist = Playlist('Songs I Like')
playlist.add_tracks(multiple_songs)
playlist.add_tracks(single_song)

print(str(playlist))
