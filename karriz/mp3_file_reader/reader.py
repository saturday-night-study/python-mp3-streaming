from dataclasses import dataclass
from bitstring import ConstBitStream

FRAME_SYNC_BITS = 0x7FF

class FileStreamNotLoadedError(Exception):
    def __init__(self):
        super().__init__('MP3 파일이 로드 되지않았습니다.')
        
class InvalidFrameSyncError(Exception):
    def __init__(self):
        super().__init__('유효하지 않은 FrameSync 값 입니다.')

@dataclass
class MP3File:
    frameSync: int = 0
    version: int = 0 # 0 = MPEG 2.5, 1 = reserved, 2 = MPEG 2, 3 = MPEG 1
    layer: int = 0 # 0 = reserved, 1 = layer III, 2 = layer II, 3 = layer I
    protection: int = 0 # 0 = protected by CRC, 1 = not protected
    bitrate: int = 0
    samplingRateFreq: int = 0
    padding: int = 0
    private: int = 0
    channelMode: int = 0
    copyright: int = 0
    original: int = 0
    emphasis: int = 0

class MP3FileReader:
    def __init__(self, filename:str):
        self.mp3_file = None
        self.mp3_file_stream = ConstBitStream(filename=filename)

    def parse(self) -> MP3File:
        if self.mp3_file_stream is None:
            raise FileStreamNotLoadedError

        mp3_file = MP3File()

        # Read freamSync: 11bits
        readFrame = self.mp3_file_stream.read(11).uint

        if readFrame != FRAME_SYNC_BITS:
            raise InvalidFrameSyncError

        mp3_file.frameSync = readFrame
        
        # Read version: 2bits
        readFrame = self.mp3_file_stream.read(2).uint

        mp3_file.version = readFrame

        # Read layer: 2bits
        readFrame = self.mp3_file_stream.read(2).uint

        mp3_file.layer = readFrame

        # Read protection: 1bit
        readFrame = self.mp3_file_stream.read(1).uint

        mp3_file.protection = readFrame

        # Read bitrate: 4bits
        readFrame = self.mp3_file_stream.read(4).uint

        mp3_file.bitrate = readFrame

        # Read samplingRateFreq: 2bits
        readFrame = self.mp3_file_stream.read(2).uint

        mp3_file.samplingRateFreq = readFrame

        # Read padding: 1bit
        readFrame = self.mp3_file_stream.read(1).uint

        mp3_file.padding = readFrame

        # Read private: 1bit
        readFrame = self.mp3_file_stream.read(1).uint

        mp3_file.private = readFrame

        # Read channelMode: 2bits
        readFrame = self.mp3_file_stream.read(2).uint

        mp3_file.channelMode = readFrame

        # Read modeExtension: 2bits
        readFrame = self.mp3_file_stream.read(2).uint

        mp3_file.modeExtension = readFrame

        # Read copyright: 1bit
        readFrame = self.mp3_file_stream.read(1).uint

        mp3_file.copyright = readFrame

        # Read original: 1bit
        readFrame = self.mp3_file_stream.read(1).uint

        mp3_file.original = readFrame

        # Read emphasis: 2bits
        readFrame = self.mp3_file_stream.read(2).uint

        mp3_file.emphasis = readFrame

        return mp3_file
