from .model import MP3

class MP3FileTrimmer:
    def __init__(self, mp3:MP3):
        self.mp3 = mp3

    def trim(self, start:int, end:int) -> MP3:
        trimmed_mp3 = self.mp3

        return trimmed_mp3
