from dataclasses import dataclass
from bitstring import ConstBitStream

from .enum import MP3Version, MP3Layer, MP3Protection, MP3PaddingBit, MP3ChannelMode ,MP3Copyright ,MP3Original, MP3Emphasis
from .error import FileStreamNotLoadedError, InvalidFrameSyncError, VersionNotMatchedError, LayerNotMatchedError, BadBitrateError, InvalidFrequencyError

FRAME_SYNC_BITS = 0b11111111111
BAD_BITRATE = 0b1111
RESERVED_FREQ = 0b11

BITRATE_TABLE = [
    [
        [0],                                                                        # Reserved
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2.5 Layer 3
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2.5 Layer 2
        [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256],        # MPEG-2.5 Layer 1
    ],
    [
        # Reserved
        [0],    
        [0],    
        [0],    
        [0],    
    ],
    [
        [0],                                                                        # Reserved
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2 Layer 3
        [0, 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160],             # MPEG-2 Layer 2
        [0, 32, 48, 56, 64, 80, 96, 112, 128, 144, 160, 176, 192, 224, 256]         # MPEG-2 Layer 1
    ],
    [
        [0],                                                                        # Reserved
        [0, 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320],         # MPEG-1 Layer 3
        [0, 32, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320, 384],        # MPEG-1 Layer 2
        [0, 32, 64, 96, 128, 160, 192, 224, 256, 288, 320, 352, 384, 416, 448]      # MPEG-1 Layer 1
    ]
]

SAMPLE_RATE_TABLE = [
    [11025, 12000, 8000],   # MPEG2.5
    [0, 0, 0],              # Reserved
    [22050, 24000, 16000],  # MPEG2
    [44100, 48000, 32000],  # MPEG1
]

@dataclass
class MP3FrameHeader:
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

@dataclass
class MP3File:
    totalDuration: int = 0

class MP3FileParser:
    def __init__(self, filepath:str):
        self.mp3_file = None
        self.mp3_file_stream = ConstBitStream(filename=filepath)

    def __checkSyncBits(self):
        readFrame = self.mp3_file_stream.read(11).uint

        if readFrame != FRAME_SYNC_BITS:
            raise InvalidFrameSyncError

    def __parseVersion(self) -> MP3Version:
        return MP3Version(self.mp3_file_stream.read(2).uint)

    def __parseLayer(self) -> MP3Layer:
        return MP3Layer(self.mp3_file_stream.read(2).uint)

    def __parseProtection(self) -> MP3Protection:
        return MP3Protection(self.mp3_file_stream.read(1).uint)

    def __parseBitrate(self, version:int, layer:int) -> int:
        readBitrate = self.mp3_file_stream.read(4).uint

        if readBitrate is BAD_BITRATE:
            raise BadBitrateError

        return BITRATE_TABLE[version][layer][readBitrate] * 1000

    def __parseSamplingRateFrequency(self, version:int) -> int:
        readFreq = self.mp3_file_stream.read(2).uint

        if readFreq is RESERVED_FREQ:
            raise InvalidFrequencyError

        return SAMPLE_RATE_TABLE[version][readFreq]

    def __parsePaddingBit(self) -> MP3PaddingBit:
        return MP3PaddingBit(self.mp3_file_stream.read(1).uint)

    def __parsePrivateBit(self) -> int:
        return self.mp3_file_stream.read(1).uint

    def __parseChannelMode(self) -> MP3ChannelMode:
        return MP3ChannelMode(self.mp3_file_stream.read(2).uint)

    def __parseModeExtension(self) -> int:
        return self.mp3_file_stream.read(2).uint

    def __parseCopyright(self) -> MP3Copyright:
        return MP3Copyright(self.mp3_file_stream.read(1).uint)
        
    def __parseOriginal(self) -> MP3Original:
        return MP3Original(self.mp3_file_stream.read(1).uint)

    def __parseEmphasis(self) -> MP3Emphasis:
        return MP3Emphasis(self.mp3_file_stream.read(2).uint)

    def parse(self) -> MP3File:
        if self.mp3_file_stream is None:
            raise FileStreamNotLoadedError

        total_duration = 0

        while self.mp3_file_stream.pos + 32 <= self.mp3_file_stream.len:
            frameheader = MP3FrameHeader()
            
            # check frameSync is valid
            self.__checkSyncBits()

            # Parse version: 2bits
            frameheader.version = self.__parseVersion()

            if frameheader.version != MP3Version.MPEG_1:
                raise VersionNotMatchedError
                
            # Parse layer: 2bits
            frameheader.layer = self.__parseLayer()
            
            if frameheader.layer != MP3Layer.LAYER_III:
                raise LayerNotMatchedError
            
            # Parse protection: 1bit
            frameheader.protection = self.__parseProtection()

            # Parse bitrate: 4bits
            frameheader.bitrate = self.__parseBitrate(frameheader.version.value, frameheader.layer.value)

            # Parse samplingRateFreq: 2bits
            frameheader.samplingRateFreq = self.__parseSamplingRateFrequency(frameheader.version.value)

            # Parse paddingBit: 1bit
            frameheader.paddingBit = self.__parsePaddingBit()

            # Read privateBit: 1bit
            frameheader.privateBit = self.__parsePrivateBit()

            # Read channelMode: 2bits
            frameheader.channelMode = self.__parseChannelMode()

            # Read modeExtension: 2bits
            frameheader.modeExtension = self.__parseModeExtension()

            # Read copyright: 1bit
            frameheader.copyright = self.__parseCopyright()

            # Read original: 1bit
            frameheader.original = self.__parseOriginal()

            # Read emphasis: 2bits
            frameheader.emphasis = self.__parseEmphasis()

            frame_length = 144 * frameheader.bitrate // frameheader.samplingRateFreq + frameheader.paddingBit.value
            frame_duration = 1152 / frameheader.samplingRateFreq
            
            print(frame_length * 8)
            print(frame_duration)

            self.mp3_file_stream.pos += frame_length * 8
            total_duration += frame_duration

        mp3_file = MP3File()
        mp3_file.totalDuration = total_duration

        return mp3_file

    def play_time(self):
        pass

