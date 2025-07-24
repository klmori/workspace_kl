from models import Song
from managers import PlaylistManager
from enums import DeviceType, PlayStrategyType
from music_player_facade import MusicPlayerFacade

class MusicPlayerApplication:
    _instance = None
    def __init__(self):
        self.song_library = []
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MusicPlayerApplication()
        return cls._instance
    def create_song_in_library(self, title, artist, path):
        new_song = Song(title, artist, path)
        self.song_library.append(new_song)
    def find_song_by_title(self, title):
        for s in self.song_library:
            if s.get_title() == title:
                return s
        return None
    def create_playlist(self, playlist_name):
        PlaylistManager.get_instance().create_playlist(playlist_name)
    def add_song_to_playlist(self, playlist_name, song_title):
        song = self.find_song_by_title(song_title)
        if song is None:
            raise Exception(f"Song '{song_title}' not found in library.")
        PlaylistManager.get_instance().add_song_to_playlist(playlist_name, song)
    def connect_audio_device(self, device_type):
        MusicPlayerFacade.get_instance().connect_device(device_type)
    def select_play_strategy(self, strategy_type):
        MusicPlayerFacade.get_instance().set_play_strategy(strategy_type)
    def load_playlist(self, playlist_name):
        MusicPlayerFacade.get_instance().load_playlist(playlist_name)
    def play_single_song(self, song_title):
        song = self.find_song_by_title(song_title)
        if song is None:
            raise Exception(f"Song '{song_title}' not found.")
        MusicPlayerFacade.get_instance().play_song(song)
    def pause_current_song(self, song_title):
        song = self.find_song_by_title(song_title)
        if song is None:
            raise Exception(f"Song '{song_title}' not found.")
        MusicPlayerFacade.get_instance().pause_song(song)
    def play_all_tracks_in_playlist(self):
        MusicPlayerFacade.get_instance().play_all_tracks()
    def play_previous_track_in_playlist(self):
        MusicPlayerFacade.get_instance().play_previous_track()
    def queue_song_next(self, song_title):
        song = self.find_song_by_title(song_title)
        if song is None:
            raise Exception(f"Song '{song_title}' not found.")
        MusicPlayerFacade.get_instance().enqueue_next(song)
