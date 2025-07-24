from models import Playlist, Song
from enums import PlayStrategyType, DeviceType
from factories import DeviceFactory

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

class DeviceManager:
    _instance = None
    def __init__(self):
        self.current_output_device = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DeviceManager()
        return cls._instance
    def connect(self, device_type):
        self.current_output_device = DeviceFactory.create_device(device_type)
        if device_type == DeviceType.BLUETOOTH:
            print("Bluetooth device connected")
        elif device_type == DeviceType.WIRED:
            print("Wired device connected")
        elif device_type == DeviceType.HEADPHONES:
            print("Headphones connected")
    def get_output_device(self):
        if self.current_output_device is None:
            raise Exception("No output device is connected.")
        return self.current_output_device
    def has_output_device(self):
        return self.current_output_device is not None
