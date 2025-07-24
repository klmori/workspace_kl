import os 
import sys

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, os.path.join(base_dir, 'MusicPlayerApplicationPy'))

from models.playlist import Playlist
from models.song import Song

class PlaylistManager:
    _instance = None
    def __init__(self):
        self.playlists = {}
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = PlaylistManager()
        return cls._instance
    def create_playlist(self, name):
        if name in self.playlists:
            raise Exception(f"Playlist \"{name}\" already exists.")
        self.playlists[name] = Playlist(name)
    def add_song_to_playlist(self, playlist_name, song):
        if playlist_name not in self.playlists:
            raise Exception(f"Playlist \"{playlist_name}\" not found.")
        self.playlists[playlist_name].add_song_to_playlist(song)
    def get_playlist(self, name):
        if name not in self.playlists:
            raise Exception(f"Playlist \"{name}\" not found.")
        return self.playlists[name]
