from dataclasses import dataclass

from app.mp3.header_spec import *


@dataclass(frozen=True)
class MP3FrameHeader:
    position: int
    sync_word: int
    version: int
    layer: int
    protection_bit: int
    bitrate_index: int
    sampling_rate_index: int
    padding_bit: int
    private_bit: int
    channel_mode: int
    mode_extension: int
    copyright: int
    original: int
    emphasis: int

    @property
    def is_valid_frame(self) -> bool:
        return (
                self.sync_word == SYNC_WORD
                and self.version == MPEG_VERSION_ONE
                and self.layer == LAYER_THREE
                and self.sampling_rate > 0
        )

    @property
    def sampling_rate(self) -> int:
        return SAMPLING_RATE_ITEMS.get(self.sampling_rate_index, 0)

    @property
    def bitrate(self) -> int:
        return BITRATE_ITEMS.get(self.bitrate_index, 0) * 1000

    @property
    def frame_length(self) -> int:
        # http://mpgedit.org/mpgedit/mpeg_format/mpeghdr.htm
        # FrameLengthInBytes = 144 * BitRate / SampleRate + Padding
        return int(MPEG_VERSION_ONE_MULTIPLIER * self.bitrate / self.sampling_rate) + self.padding_bit

    @property
    def audio_data_length(self) -> int:
        return self.frame_length - FRAME_HEADER_SIZE

    @property
    def audio_data_duration(self) -> float:
        # Duration = Layer 3 Samples(1152) / SampleRate
        return LAYER_THREE_SAMPLES / self.sampling_rate

    def __str__(self):
        version_desc = VERSION_ITEMS.get(self.version, "Unknown")
        layer_desc = LAYER_ITEMS.get(self.layer, "Unknown")
        protection_bit_desc = PROTECTION_BIT_ITEMS.get(self.protection_bit, "Unknown")
        padding_bit_desc = PADDING_BIT_ITEMS.get(self.padding_bit, "Unknown")
        channel_mode_desc = CHANNEL_MODE_ITEMS.get(self.channel_mode, "Unknown")
        copyright_desc = COPYRIGHT_ITEMS.get(self.copyright, "Unknown")
        original_desc = ORIGINAL_ITEMS.get(self.original, "Unknown")
        emphasis_desc = EMPHASIS_ITEMS.get(self.emphasis, "Unknown")

        field_width = 20
        return (
            f"{"-" * (field_width * 2)}\n"
            f"{'Field':<{field_width}} {'Value':<{field_width}}\n"
            f"{"-" * (field_width * 2)}\n"
            f"{'Sync Word':<{field_width}} {self.sync_word:b}\n"
            f"{'Version':<{field_width}} {version_desc}\n"
            f"{'Layer':<{field_width}} {layer_desc}\n"
            f"{'Protection bit':<{field_width}} {protection_bit_desc}\n"
            f"{'Bitrate Index':<{field_width}} {self.bitrate}\n"
            f"{'Sampling Rate':<{field_width}} {self.sampling_rate}\n"
            f"{'Padding Bit':<{field_width}} {padding_bit_desc}\n"
            f"{'Private Bit':<{field_width}} {self.private_bit}\n"
            f"{'Channel Mode':<{field_width}} {channel_mode_desc}\n"
            f"{'Mode Extension':<{field_width}} {self.mode_extension}\n"
            f"{'Copyright':<{field_width}} {copyright_desc}\n"
            f"{'Original':<{field_width}} {original_desc}\n"
            f"{'Emphasis':<{field_width}} {emphasis_desc}\n"
            f"{"-" * (field_width * 2)}\n"
            f"{'Position':<{field_width}} {self.position}\n"
            f"{'Frame Length':<{field_width}} {self.frame_length}\n"
            f"{'Audio Data Length':<{field_width}} {self.audio_data_length}\n"
            f"{'Audio Data Duration':<{field_width}} {self.audio_data_duration}\n"
            f"{"-" * (field_width * 2)}\n"
        )

    # 데이타 클래스를 사용할때 __repr__ 메서드는 자동 생성되기 때문에 아래 코드를 주석 처리
    # 학습 목적을 위해서 주석을 남겨 놓음
    # def __repr__(self):
    #     return (
    #         f"MP3FrameHeader(sync_word={self.sync_word}, version={self.version}, layer={self.layer}, "
    #         f"protection_bit={self.protection_bit}, bitrate_index={self.bitrate_index}, "
    #         f"sampling_rate={self.sampling_rate}, padding_bit={self.padding_bit}, private_bit={self.private_bit}, "
    #         f"channel_mode={self.channel_mode}, mode_extension={self.mode_extension}, copyright={self.copyright}, "
    #         f"original={self.original}, emphasis={self.emphasis})"
    #     )
