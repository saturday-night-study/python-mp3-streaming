from typing import Optional

from python_mp3_streaming.file_io import FileIO
from python_mp3_streaming.mp3_frame_header import MP3FrameHeader
from python_mp3_streaming.mp3_frame_header_spec import *


class MP3Reader:

    def __init__(self, file_io: FileIO):
        self.__fio: FileIO = file_io

    def read_nth_frame_header(self, n: int) -> Optional[MP3FrameHeader]:
        if not isinstance(n, int):
            print(f"입력 파라미터 타입 오류: n{type(n)}=[{n}]")
            return None
        elif n < 0:
            print(f"입력 파라미터 범위 오류: n{type(n)}=[{n}]")
            return None

        data = self.__fio.read(FRAME_HEADER_SIZE)
        header = MP3FrameHeader(
            sync_word=self.__get_bits_from_bytes(data, SYNC_WORD_RANGE),
            version=self.__get_bits_from_bytes(data, VERSION_RANGE),
            layer=self.__get_bits_from_bytes(data, LAYER_RANGE),
            protection_bit=self.__get_bits_from_bytes(data, PROTECTION_BIT_RANGE),
            bitrate_index=self.__get_bits_from_bytes(data, BITRATE_INDEX_RANGE),
            sampling_rate=self.__get_bits_from_bytes(data, SAMPLING_RATE_RANGE),
            padding_bit=self.__get_bits_from_bytes(data, PADDING_BIT_RANGE),
            private_bit=self.__get_bits_from_bytes(data, PRIVATE_BIT_RANGE),
            channel_mode=self.__get_bits_from_bytes(data, CHANNEL_MODE_RANGE),
            mode_extension=self.__get_bits_from_bytes(data, MODE_EXTENSION_RANGE),
            copyright=self.__get_bits_from_bytes(data, COPYRIGHT_RANGE),
            original=self.__get_bits_from_bytes(data, ORIGINAL_RANGE),
            emphasis=self.__get_bits_from_bytes(data, EMPHASIS_RANGE)
        )

        return header

    @staticmethod
    def __get_bits_from_bytes(data: bytes, range: FrameHeaderRange) -> int:
        int_data = int.from_bytes(data, byteorder='big')
        total_bits = len(data) * 8
        shift_length = total_bits - range.offset - range.length
        mask = (1 << range.length) - 1

        return (int_data >> shift_length) & mask
