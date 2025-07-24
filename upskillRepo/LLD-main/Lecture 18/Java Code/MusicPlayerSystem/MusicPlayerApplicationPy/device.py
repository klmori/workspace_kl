from models import Song

class IAudioOutputDevice:
    def play_audio(self, song: Song):
        raise NotImplementedError

class WiredSpeakerAdapter(IAudioOutputDevice):
    def __init__(self, wired_api):
        self.wired_api = wired_api
    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.wired_api.play_sound_via_cable(payload)

class HeadphonesAdapter(IAudioOutputDevice):
    def __init__(self, headphones_api):
        self.headphones_api = headphones_api
    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.headphones_api.play_sound_via_jack(payload)

class BluetoothSpeakerAdapter(IAudioOutputDevice):
    def __init__(self, bluetooth_api):
        self.bluetooth_api = bluetooth_api
    def play_audio(self, song: Song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.bluetooth_api.play_sound_via_bluetooth(payload)
