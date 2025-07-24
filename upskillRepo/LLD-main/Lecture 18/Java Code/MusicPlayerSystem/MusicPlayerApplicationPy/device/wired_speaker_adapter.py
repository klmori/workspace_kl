from device.iaudio_output_device import IAudioOutputDevice

class WiredSpeakerAdapter(IAudioOutputDevice):
    def __init__(self, wired_api):
        self.wired_api = wired_api
    def play_audio(self, song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.wired_api.play_sound_via_cable(payload)
