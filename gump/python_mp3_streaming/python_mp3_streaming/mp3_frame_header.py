from dataclasses import dataclass

from python_mp3_streaming.mp3_frame_header_spec import *


@dataclass
class MP3FrameHeader:
    sync_word: int
    version: int
    layer: int
    protection_bit: int
    bitrate_index: int
    sampling_rate: int
    padding_bit: int
    private_bit: int
    channel_mode: int
    mode_extension: int
    copyright: int
    original: int
    emphasis: int

    @property
    def is_valid_frame(self):
        return (
                self.sync_word == SYNC_WORD
                and self.version == MPEG_VERSION_ONE
                and self.layer == LAYER_THREE
        )

    def __repr__(self):
        return f"MP3FrameHeader(sync_word={self.sync_word}, version={self.version}, layer={self.layer}, " \
               f"protection_bit={self.protection_bit}, bitrate_index={self.bitrate_index}, " \
               f"sampling_rate={self.sampling_rate}, padding_bit={self.padding_bit}, private_bit={self.private_bit}, " \
               f"channel_mode={self.channel_mode}, mode_extension={self.mode_extension}, copyright={self.copyright}, " \
               f"original={self.original}, emphasis={self.emphasis})"

    def __str__(self):
        version_desc = VERSION_ITEMS.get(self.version, "Unknown")
        layer_desc = LAYER_ITEMS.get(self.layer, "Unknown")
        protection_bit_desc = PROTECTION_BIT_ITEMS.get(self.protection_bit, "Unknown")
        bitrate_desc = BITRATE_ITEMS.get(self.bitrate_index, "Unknown")
        sampling_rate_desc = SAMPLING_RATE_ITEMS.get(self.sampling_rate, "Unknown")
        padding_bit_desc = PADDING_BIT_ITEMS.get(self.padding_bit, "Unknown")
        channel_mode_desc = CHANNEL_MODE_ITEMS.get(self.channel_mode, "Unknown")
        copyright_desc = COPYRIGHT_ITEMS.get(self.copyright, "Unknown")
        original_desc = ORIGINAL_ITEMS.get(self.original, "Unknown")
        emphasis_desc = EMPHASIS_ITEMS.get(self.emphasis, "Unknown")

        field_width = 20
        return f"{"-" * (field_width * 2)}\n" \
               f"{'Field':<{field_width}} {'Value':<{field_width}}\n" \
               f"{"-" * (field_width * 2)}\n" \
               f"{'Sync Word':<{field_width}} {self.sync_word:b}\n" \
               f"{'Version':<{field_width}} {version_desc}\n" \
               f"{'Layer':<{field_width}} {layer_desc}\n" \
               f"{'Protection bit':<{field_width}} {protection_bit_desc}\n" \
               f"{'Bitrate Index':<{field_width}} {bitrate_desc}\n" \
               f"{'Sampling Rate':<{field_width}} {sampling_rate_desc}\n" \
               f"{'Padding Bit':<{field_width}} {padding_bit_desc}\n" \
               f"{'Private Bit':<{field_width}} {self.private_bit}\n" \
               f"{'Channel Mode':<{field_width}} {channel_mode_desc}\n" \
               f"{'Mode Extension':<{field_width}} {self.mode_extension}\n" \
               f"{'Copyright':<{field_width}} {copyright_desc}\n" \
               f"{'Original':<{field_width}} {original_desc}\n" \
               f"{'Emphasis':<{field_width}} {emphasis_desc}\n" \
               f"{"-" * (field_width * 2)}\n"
