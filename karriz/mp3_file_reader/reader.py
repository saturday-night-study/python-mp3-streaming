from dataclasses import dataclass
from bitstring import ConstBitStream

@dataclass
class MP3File:
    frameSync: any

class FileStreamNotLoadedError(Exception):
    def __init__(self):
        super().__init__('MP3 파일이 로드 되지않았습니다.')

class MP3FileReader:
    def __init__(self, filename:str):
        self.mp3_file_stream = ConstBitStream(filename)

    def read(self) -> None:
        if self.mp3_file_stream is None:
            raise FileStreamNotLoadedError

        frameSync = self.mp3_file_stream.read(11)

        print(frameSync)

        
        