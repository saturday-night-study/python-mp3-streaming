from .model import MP3
from .error import FileStreamNotLoadedError

class MP3FileReader:
    def __init__(self, file_path:str):
        self.mp3_file = open(file_path, 'rb')

    def read(self) -> MP3:
        if self.mp3_file is None:
            raise FileStreamNotLoadedError
        pass