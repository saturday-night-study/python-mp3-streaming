from . import model

class MP3FileTrimmer:
    def __init__(self, mp3_file:model.MP3File):
        self.mp3_file = mp3_file

    def trim(self, start:int, end:int) -> model.MP3File:
        trimmed_mp3 = self.mp3_file

        return trimmed_mp3
