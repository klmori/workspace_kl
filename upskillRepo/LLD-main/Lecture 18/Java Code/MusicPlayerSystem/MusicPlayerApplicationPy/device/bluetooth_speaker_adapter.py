from .iaudio_output_device import IAudioOutputDevice

class BluetoothSpeakerAdapter(IAudioOutputDevice):
    def __init__(self, bluetooth_api):
        self.bluetooth_api = bluetooth_api
    def play_audio(self, song):
        payload = f"{song.get_title()} by {song.get_artist()}"
        self.bluetooth_api.play_sound_via_bluetooth(payload)
