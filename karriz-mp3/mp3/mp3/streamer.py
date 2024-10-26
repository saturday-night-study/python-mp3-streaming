from .const import KB

from . import model

class MP3Streamer:
    def __init__(self, mp3:model.MP3):
        self.__mp3 = mp3

    def streaming(self):
        with open(self.__mp3.file_path, "rb") as file:
            while chunk := file.read(50 * KB):
                yield chunk
