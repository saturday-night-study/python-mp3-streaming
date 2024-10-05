from enum import Enum
from dataclasses import dataclass
from bitstring import ConstBitStream

FRAME_SYNC_BITS = 0x7FF

class FileStreamNotLoadedError(Exception):
    def __init__(self):
        super().__init__('MP3 파일이 로드 되지않았습니다.')
        
class InvalidFrameSyncError(Exception):
    def __init__(self):
        super().__init__('유효하지 않은 FrameSync 값 입니다.')

class MP3Version(Enum):
    MPEG_2_5 = 0
    RESERVED = 1
    MPEG_2 = 2
    MPEG_1 = 3

class MP3Layer(Enum):
    RESERVED = 0
    LAYER_III = 1
    LAYER_II = 2
    LAYER_I = 3

class MP3Protection(Enum):
    PROTECTED_BY_CRC = 0
    NOT_PROTECTED = 1

class MP3PaddingBit(Enum):
    NOT_PADDED = 0
    PADDED = 1

class MP3ChannelMode(Enum):
    STEREO = 0
    JOINT_STEREO = 1
    DUAL_MONO_CAHNNEL = 2
    SINGLE_MONO_CHANNEL = 3

class MP3Copyright(Enum):
    NOT_COPYRIGHTED = 0
    COPYRIGHTED = 1

class MP3Original(Enum):
    COPY = 0
    ORIGINAL = 1

class MP3Emphasis(Enum):
    NONE = 0
    E_50_15_MS = 1  # 50/15µs emphasis
    RESERVED = 2
    CCIT_J_17 = 3

@dataclass
class MP3File:
    frameSync: int = 0
    version: MP3Version = MP3Version.MPEG_2_5
    layer: MP3Layer = MP3Layer.RESERVED
    protection: MP3Protection = MP3Protection.PROTECTED_BY_CRC
    bitrate: int = 0
    samplingRateFreq: int = 0
    paddingBit: MP3PaddingBit = MP3PaddingBit.NOT_PADDED
    privateBit: int = 0
    channelMode: MP3ChannelMode = MP3ChannelMode.STEREO
    modeExtension: int = 0
    copyright: MP3Copyright = MP3Copyright.NOT_COPYRIGHTED
    original: MP3Original = MP3Original.COPY
    emphasis: MP3Emphasis = MP3Emphasis.NONE

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

        # Read paddingBit: 1bit
        readFrame = self.mp3_file_stream.read(1).uint

        mp3_file.paddingBit = readFrame

        # Read privateBit: 1bit
        readFrame = self.mp3_file_stream.read(1).uint

        mp3_file.privateBit = readFrame

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
