from .parser import MP3File

class MP3FileTrimmer:
    def __init__(self, mp3file:MP3File):
        self.mp3_file = mp3file

    def trim(self, start:int, end:int) -> MP3File:
        trimmed_mp3_file = self.mp3_file

        return trimmed_mp3_file
