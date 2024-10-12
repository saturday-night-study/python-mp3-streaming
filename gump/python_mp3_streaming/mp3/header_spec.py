from typing import Final, NamedTuple, Dict

FRAME_HEADER_SIZE: Final = 4


class FrameHeaderRange(NamedTuple):
    offset: int
    length: int


SYNC_WORD_RANGE = FrameHeaderRange(0, 11)
VERSION_RANGE = FrameHeaderRange(11, 2)
LAYER_RANGE = FrameHeaderRange(13, 2)
PROTECTION_BIT_RANGE = FrameHeaderRange(15, 1)
BITRATE_INDEX_RANGE = FrameHeaderRange(16, 4)
SAMPLING_RATE_RANGE = FrameHeaderRange(20, 2)
PADDING_BIT_RANGE = FrameHeaderRange(22, 1)
PRIVATE_BIT_RANGE = FrameHeaderRange(23, 1)
CHANNEL_MODE_RANGE = FrameHeaderRange(24, 2)
MODE_EXTENSION_RANGE = FrameHeaderRange(26, 2)
COPYRIGHT_RANGE = FrameHeaderRange(28, 1)
ORIGINAL_RANGE = FrameHeaderRange(29, 1)
EMPHASIS_RANGE = FrameHeaderRange(30, 2)

SYNC_WORD: Final[int] = 0b11111111111
MPEG_VERSION_ONE: Final[int] = 0b11
MPEG_VERSION_ONE_MULTIPLIER: Final[int] = 144
LAYER_THREE: Final[int] = 0b01
LAYER_THREE_SAMPLES: Final[int] = 1152

VERSION_ITEMS: Final[Dict[int, str]] = {
    0b00: "MPEG 2.5",
    0b01: "Reserved",
    0b10: "MPEG 2",
    0b11: "MPEG 1"
}

LAYER_ITEMS: Final[Dict[int, str]] = {
    0b00: "Reserved",
    0b01: "Layer III",
    0b10: "Layer II",
    0b11: "Layer I"
}

PROTECTION_BIT_ITEMS: Final[Dict[int, str]] = {
    0: "Protected by CRC",
    1: "Not protected"
}

BITRATE_ITEMS: Final[Dict[int, int]] = {
    0b0000: 0,
    0b0001: 32,
    0b0010: 40,
    0b0011: 48,
    0b0100: 56,
    0b0101: 64,
    0b0110: 80,
    0b0111: 96,
    0b1000: 112,
    0b1001: 128,
    0b1010: 160,
    0b1011: 192,
    0b1100: 224,
    0b1101: 256,
    0b1110: 320,
    0b1111: -1
}

SAMPLING_RATE_ITEMS: Final[Dict[int, int]] = {
    0b00: 44100,
    0b01: 48000,
    0b10: 32000,
    0b11: -1
}

PADDING_BIT_ITEMS: Final[Dict[int, str]] = {
    0: "Frame is not padded",
    1: "Frame is padded with one extra slot"
}

CHANNEL_MODE_ITEMS: Final[Dict[int, str]] = {
    0b00: "Stereo",
    0b01: "Joint Stereo",
    0b10: "Dual Channel(DualMono)",
    0b11: "Single Channel(Mono)"
}

COPYRIGHT_ITEMS: Final[Dict[int, str]] = {
    0: "Audio is not copyrighted",
    1: "Audio is copyrighted"
}

ORIGINAL_ITEMS: Final[Dict[int, str]] = {
    0: "Copy of original media",
    1: "Original media"
}

EMPHASIS_ITEMS: Final[Dict[int, str]] = {
    0b00: "none",
    0b01: "50/15 ms",
    0b10: "reserved",
    0b11: "CCIT J.17"
}
