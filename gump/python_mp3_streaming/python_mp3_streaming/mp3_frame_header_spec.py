from typing import Final, NamedTuple

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
