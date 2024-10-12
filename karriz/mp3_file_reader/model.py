from dataclasses import dataclass

from .enum import MP3Version, MP3Layer, MP3Protection, MP3PaddingBit, MP3ChannelMode ,MP3Copyright ,MP3Original, MP3Emphasis

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
class MP3:
    total_duration: float = 0.0
    