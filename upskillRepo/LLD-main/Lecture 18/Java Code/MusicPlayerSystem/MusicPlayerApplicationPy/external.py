class WiredSpeakerAPI:
    def play_sound_via_cable(self, data):
        print(f"[WiredSpeaker] Playing: {data}")

class HeadphonesAPI:
    def play_sound_via_jack(self, data):
        print(f"[Headphones] Playing: {data}")

class BluetoothSpeakerAPI:
    def play_sound_via_bluetooth(self, data):
        print(f"[BluetoothSpeaker] Playing: {data}")
