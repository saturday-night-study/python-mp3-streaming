from dataclasses import dataclass


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
        return self.sync_word == 0b11111111111 and self.version == 0b11 and self.layer == 0b01

    def __repr__(self):
        return f"MP3FrameHeader(sync_word={self.sync_word}, version={self.version}, layer={self.layer}, " \
               f"protection_bit={self.protection_bit}, bitrate_index={self.bitrate_index}, " \
               f"sampling_rate={self.sampling_rate}, padding_bit={self.padding_bit}, private_bit={self.private_bit}, " \
               f"channel_mode={self.channel_mode}, mode_extension={self.mode_extension}, copyright={self.copyright}, " \
               f"original={self.original}, emphasis={self.emphasis})"

    def __str__(self):
        field_width = 20
        return f"{"-" * (field_width * 2)}\n" \
               f"{'Field':<{field_width}} {'Value':<{field_width}}\n" \
               f"{"-" * (field_width * 2)}\n" \
               f"{'Sync Word':<{field_width}} {self.sync_word:b}\n" \
               f"{'Version':<{field_width}} {self.version}\n" \
               f"{'Protection bit':<{field_width}} {self.protection_bit}\n" \
               f"{'Bitrate Index':<{field_width}} {self.bitrate_index}\n" \
               f"{'Sampling Rate':<{field_width}} {self.sampling_rate}\n" \
               f"{'Padding Bit':<{field_width}} {self.padding_bit}\n" \
               f"{'Private Bit':<{field_width}} {self.private_bit}\n" \
               f"{'Channel Mode':<{field_width}} {self.channel_mode}\n" \
               f"{'Mode Extension':<{field_width}} {self.mode_extension}\n" \
               f"{'Copyright':<{field_width}} {self.copyright}\n" \
               f"{'Original':<{field_width}} {self.original}\n" \
               f"{'Emphasis':<{field_width}} {self.emphasis}\n" \
               f"{"-" * (field_width * 2)}\n"
