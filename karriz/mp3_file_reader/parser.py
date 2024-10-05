from dataclasses import dataclass
from bitstring import ConstBitStream

from enum import MP3Version, MP3Layer, MP3Protection, MP3PaddingBit, MP3ChannelMode ,MP3Copyright ,MP3Original, MP3Emphasis
from error import FileStreamNotLoadedError, InvalidFrameSyncError, VersionNotMatchedError, LayerNotMatchedError

FRAME_SYNC_BITS = 0x7FF

@dataclass
class MP3File:
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

    def __parseBitrate(self) -> int:
        return self.mp3_file_stream.read(4).uint

    def __parseSamplingRateFrequency(self) -> int:
        return self.mp3_file_stream.read(2).uint

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

        mp3_file = MP3File()

        # check frameSync is valid
        self.__checkSyncBits()

        # Parse version: 2bits
        mp3_file.version = self.__parseVersion()

        if mp3_file.version != MP3Version.MPEG_1:
            raise VersionNotMatchedError
            

        # Parse layer: 2bits
        mp3_file.layer = self.__parseLayer()
        
        if mp3_file.layer != MP3Layer.LAYER_III:
            raise LayerNotMatchedError
        
        # Parse protection: 1bit
        mp3_file.protection = self.__parseProtection()

        # Parse bitrate: 4bits
        mp3_file.bitrate = self.__parseBitrate()

        # Parse samplingRateFreq: 2bits
        mp3_file.samplingRateFreq = self.__parseSamplingRateFrequency()

        # Parse paddingBit: 1bit
        mp3_file.paddingBit = self.__parsePaddingBit()

        # Read privateBit: 1bit
        mp3_file.privateBit = self.__parsePrivateBit()

        # Read channelMode: 2bits
        mp3_file.channelMode = self.__parseChannelMode()

        # Read modeExtension: 2bits
        mp3_file.modeExtension = self.__parseModeExtension()

        # Read copyright: 1bit
        mp3_file.copyright = self.__parseCopyright()

        # Read original: 1bit
        mp3_file.original = self.__parseOriginal()

        # Read emphasis: 2bits
        mp3_file.emphasis = self.__parseEmphasis()

        return mp3_file
