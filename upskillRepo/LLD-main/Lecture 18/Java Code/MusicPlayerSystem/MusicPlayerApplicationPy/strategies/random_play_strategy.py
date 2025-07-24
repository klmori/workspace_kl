from models.playlist import Playlist
from models.song import Song
import random

class RandomPlayStrategy:
    def __init__(self):
        self.current_playlist = None
        self.remaining_songs = []
        self.history = []
    def set_playlist(self, playlist: Playlist):
        self.current_playlist = playlist
        if self.current_playlist is None or self.current_playlist.get_size() == 0:
            return
        self.remaining_songs = list(self.current_playlist.get_songs())
        self.history = []
    def has_next(self):
        return self.current_playlist is not None and len(self.remaining_songs) > 0
    def next(self):
        if self.current_playlist is None or self.current_playlist.get_size() == 0:
            raise Exception("No playlist loaded or playlist is empty.")
        if not self.remaining_songs:
            raise Exception("No songs left to play")
        idx = random.randint(0, len(self.remaining_songs) - 1)
        selected_song = self.remaining_songs.pop(idx)
        self.history.append(selected_song)
        return selected_song
    def has_previous(self):
        return len(self.history) > 0
    def previous(self):
        if not self.history:
            raise Exception("No previous song available.")
        return self.history.pop()
