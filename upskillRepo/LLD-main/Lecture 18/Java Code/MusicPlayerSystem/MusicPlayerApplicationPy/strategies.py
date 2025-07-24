from models import Playlist, Song
import random
from collections import deque

class PlayStrategy:
    def set_playlist(self, playlist: Playlist):
        raise NotImplementedError
    def next(self):
        raise NotImplementedError
    def has_next(self):
        raise NotImplementedError
    def previous(self):
        raise NotImplementedError
    def has_previous(self):
        raise NotImplementedError
    def add_to_next(self, song: Song):
        pass

class SequentialPlayStrategy(PlayStrategy):
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

class RandomPlayStrategy(PlayStrategy):
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

class CustomQueueStrategy(PlayStrategy):
    def __init__(self):
        self.current_playlist = None
        self.current_index = -1
        self.next_queue = deque()
        self.prev_stack = []
    def set_playlist(self, playlist: Playlist):
        self.current_playlist = playlist
        self.current_index = -1
        self.next_queue.clear()
        self.prev_stack.clear()
    def has_next(self):
        return (self.current_index + 1) < self.current_playlist.get_size()
    def next(self):
        if self.current_playlist is None or self.current_playlist.get_size() == 0:
            raise Exception("No playlist loaded or playlist is empty.")
        if self.next_queue:
            s = self.next_queue.popleft()
            self.prev_stack.append(s)
            for i, song in enumerate(self.current_playlist.get_songs()):
                if song == s:
                    self.current_index = i
                    break
            return s
        return self.next_sequential()
    def next_sequential(self):
        if self.current_playlist.get_size() == 0:
            raise Exception("Playlist is empty.")
        self.current_index += 1
        return self.current_playlist.get_songs()[self.current_index]
    def has_previous(self):
        return (self.current_index - 1) > 0
    def previous(self):
        if self.current_playlist is None or self.current_playlist.get_size() == 0:
            raise Exception("No playlist loaded or playlist is empty.")
        if self.prev_stack:
            s = self.prev_stack.pop()
            for i, song in enumerate(self.current_playlist.get_songs()):
                if song == s:
                    self.current_index = i
                    break
            return s
        return self.previous_sequential()
    def previous_sequential(self):
        if self.current_playlist.get_size() == 0:
            raise Exception("Playlist is empty.")
        self.current_index -= 1
        return self.current_playlist.get_songs()[self.current_index]
    def add_to_next(self, song: Song):
        if song is None:
            raise Exception("Cannot enqueue null song.")
        self.next_queue.append(song)
