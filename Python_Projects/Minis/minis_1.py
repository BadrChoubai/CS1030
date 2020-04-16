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
