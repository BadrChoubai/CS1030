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

    def add_tracks(self, new_tracks: list):
        self.tracks.append(new_tracks)


class Album():
    def __init__(self, title: str, artist: str, tracks: list):
        self.artist = artist
        self.title = title
        self.tracks = tracks


class Track():
    def __init__(self, artist: str, title: str, duration: int):
        self.artist = artist
        self.title = title
        self.duration = duration
