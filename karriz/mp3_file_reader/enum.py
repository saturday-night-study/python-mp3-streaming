from enum import Enum

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