from managers import DeviceManager, PlaylistManager
from strategy_manager import StrategyManager
from strategies import PlayStrategy
from models import Song, Playlist
from enums import DeviceType, PlayStrategyType

class AudioEngine:
    def __init__(self):
        self.current_song_title = None
    def play(self, device, song):
        device.play_audio(song)
        self.current_song_title = song.get_title()
    def pause(self):
        print(f"Paused: {self.current_song_title}")
    def get_current_song_title(self):
        return self.current_song_title

class MusicPlayerFacade:
    _instance = None
    def __init__(self):
        self.audio_engine = AudioEngine()
        self.loaded_playlist = None
        self.play_strategy = None
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = MusicPlayerFacade()
        return cls._instance
    def connect_device(self, device_type):
        DeviceManager.get_instance().connect(device_type)
    def set_play_strategy(self, strategy_type):
        self.play_strategy = StrategyManager.get_instance().get_strategy(strategy_type)
    def load_playlist(self, name):
        self.loaded_playlist = PlaylistManager.get_instance().get_playlist(name)
        if self.play_strategy is None:
            raise Exception("Play strategy not set before loading.")
        self.play_strategy.set_playlist(self.loaded_playlist)
    def play_song(self, song):
        if not DeviceManager.get_instance().has_output_device():
            raise Exception("No audio device connected.")
        device = DeviceManager.get_instance().get_output_device()
        self.audio_engine.play(device, song)
    def pause_song(self, song):
        if self.audio_engine.get_current_song_title() != song.get_title():
            raise Exception(f"Cannot pause '{song.get_title()}'; not currently playing.")
        self.audio_engine.pause()
    def play_all_tracks(self):
        if self.loaded_playlist is None:
            raise Exception("No playlist loaded.")
        while self.play_strategy.has_next():
            next_song = self.play_strategy.next()
            device = DeviceManager.get_instance().get_output_device()
            self.audio_engine.play(device, next_song)
        print(f"Completed playlist: {self.loaded_playlist.get_playlist_name()}")
    def play_next_track(self):
        if self.loaded_playlist is None:
            raise Exception("No playlist loaded.")
        if self.play_strategy.has_next():
            next_song = self.play_strategy.next()
            device = DeviceManager.get_instance().get_output_device()
            self.audio_engine.play(device, next_song)
        else:
            print(f"Completed playlist: {self.loaded_playlist.get_playlist_name()}")
    def play_previous_track(self):
        if self.loaded_playlist is None:
            raise Exception("No playlist loaded.")
        if self.play_strategy.has_previous():
            prev_song = self.play_strategy.previous()
            device = DeviceManager.get_instance().get_output_device()
            self.audio_engine.play(device, prev_song)
        else:
            print(f"Completed playlist: {self.loaded_playlist.get_playlist_name()}")
    def enqueue_next(self, song):
        self.play_strategy.add_to_next(song)
