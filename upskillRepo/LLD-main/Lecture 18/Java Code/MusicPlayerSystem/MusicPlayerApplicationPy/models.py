class Song:
    def __init__(self, title, artist, file_path):
        self.title = title
        self.artist = artist
        self.file_path = file_path
    def get_title(self):
        return self.title
    def get_artist(self):
        return self.artist
    def get_file_path(self):
        return self.file_path

class Playlist:
    def __init__(self, name):
        self.playlist_name = name
        self.song_list = []
    def get_playlist_name(self):
        return self.playlist_name
    def get_songs(self):
        return self.song_list
    def get_size(self):
        return len(self.song_list)
    def add_song_to_playlist(self, song):
        if song is None:
            raise Exception("Cannot add null song to playlist.")
        self.song_list.append(song)
