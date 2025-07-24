from models.playlist import Playlist
from models.song import Song

class SequentialPlayStrategy:
    def __init__(self):
        self.current_playlist = None
        self.current_index = -1
    def set_playlist(self, playlist: Playlist):
        self.current_playlist = playlist
        self.current_index = -1
    def has_next(self):
        return (self.current_index + 1) < self.current_playlist.get_size()
    def next(self):
        if self.current_playlist is None or self.current_playlist.get_size() == 0:
            raise Exception("No playlist loaded or playlist is empty.")
        self.current_index += 1
        return self.current_playlist.get_songs()[self.current_index]
    def has_previous(self):
        return (self.current_index - 1) > 0
    def previous(self):
        if self.current_playlist is None or self.current_playlist.get_size() == 0:
            raise Exception("No playlist loaded or playlist is empty.")
        self.current_index -= 1
        return self.current_playlist.get_songs()[self.current_index]
