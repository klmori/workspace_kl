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
