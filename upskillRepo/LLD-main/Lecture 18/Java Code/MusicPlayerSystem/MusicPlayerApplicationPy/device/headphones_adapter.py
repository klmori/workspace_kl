from .iaudio_output_device import IAudioOutputDevice

class HeadphonesAdapter(IAudioOutputDevice):
    def __init__(self, headphones_api):
        self.headphones_api = headphones_api
    def play_audio(self, song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.headphones_api.play_sound_via_jack(payload)
