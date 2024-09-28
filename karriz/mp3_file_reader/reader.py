from dataclasses import dataclass
from bitstring import ConstBitStream

FRAME_SYNC_BITS = 0x7FF

@dataclass
class MP3File:
    frameSync: any

class FileStreamNotLoadedError(Exception):
    def __init__(self):
        super().__init__('MP3 파일이 로드 되지않았습니다.')
        
class InvalidFrameSyncError(Exception):
    def __init__(self):
        super().__init__('유효하지 않은 FrameSync 값 입니다.')
                

class MP3FileReader:
    def __init__(self, filename:str):
        self.mp3_file_stream = ConstBitStream(filename=filename)

    def read(self) -> None:
        if self.mp3_file_stream is None:
            raise FileStreamNotLoadedError

        # Read freamSync: 11bits
        readFrame = self.mp3_file_stream.read(11).uint

        if readFrame != FRAME_SYNC_BITS:
            raise InvalidFrameSyncError
