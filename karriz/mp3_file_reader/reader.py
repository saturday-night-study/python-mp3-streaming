from dataclasses import dataclass

@dataclass
class MP3File:
    frameSync: any

class NotThreeMultipleError(Exception):
    def __init__(self):
        super().__init__('3의 배수가')

class MP3FileReader:
    def __init__(self, filePath:str):
        self.mp3_file = open(filePath, 'rb')
