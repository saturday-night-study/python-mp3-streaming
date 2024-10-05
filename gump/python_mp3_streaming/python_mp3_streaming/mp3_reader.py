from typing import Optional

from python_mp3_streaming.end_of_mp3_frame_error import EndOfMP3FrameError
from python_mp3_streaming.file_io import FileIO
from python_mp3_streaming.mp3_frame_header import MP3FrameHeader
from python_mp3_streaming.mp3_frame_header_spec import *


class MP3Reader:
    def __init__(self, file_io: FileIO):
        self.__fio: FileIO = file_io

    def __read_frame_header(self) -> Optional[MP3FrameHeader]:
        if self.__fio.closed:
            raise IOError()

        # Sync Word를 찾을 때까지 1바이트씩 이동
        while True:
            position = self.__fio.current_position
            data = self.__fio.read(FRAME_HEADER_SIZE)
            if len(data) < FRAME_HEADER_SIZE:
                raise EndOfMP3FrameError()

            header = MP3Reader.__parse_header(position, data)
            if header.is_valid_frame:
                break

            self.__fio.skip(-(FRAME_HEADER_SIZE - 1))

        return header

    @staticmethod
    def __parse_header(position: int, data: bytes) -> Optional[MP3FrameHeader]:
        return MP3FrameHeader(
            position=position,
            sync_word=MP3Reader.__get_bits_from_bytes(data, SYNC_WORD_RANGE),
            version=MP3Reader.__get_bits_from_bytes(data, VERSION_RANGE),
            layer=MP3Reader.__get_bits_from_bytes(data, LAYER_RANGE),
            protection_bit=MP3Reader.__get_bits_from_bytes(data, PROTECTION_BIT_RANGE),
            bitrate_index=MP3Reader.__get_bits_from_bytes(data, BITRATE_INDEX_RANGE),
            sampling_rate=MP3Reader.__get_bits_from_bytes(data, SAMPLING_RATE_RANGE),
            padding_bit=MP3Reader.__get_bits_from_bytes(data, PADDING_BIT_RANGE),
            private_bit=MP3Reader.__get_bits_from_bytes(data, PRIVATE_BIT_RANGE),
            channel_mode=MP3Reader.__get_bits_from_bytes(data, CHANNEL_MODE_RANGE),
            mode_extension=MP3Reader.__get_bits_from_bytes(data, MODE_EXTENSION_RANGE),
            copyright=MP3Reader.__get_bits_from_bytes(data, COPYRIGHT_RANGE),
            original=MP3Reader.__get_bits_from_bytes(data, ORIGINAL_RANGE),
            emphasis=MP3Reader.__get_bits_from_bytes(data, EMPHASIS_RANGE)
        )

    @staticmethod
    def __get_bits_from_bytes(data: bytes, frame_header_range: FrameHeaderRange) -> int:
        int_data = int.from_bytes(data, byteorder='big')
        total_bits = len(data) * 8
        shift_length = total_bits - frame_header_range.offset - frame_header_range.length
        mask = (1 << frame_header_range.length) - 1

        return (int_data >> shift_length) & mask

    # TODO: 새로운 이터레이터를 반환하지 않고 있어서 1회만 사용 가능함. 반복해서 사용할 수 있도로 새로운 이터레이터 객체를 반환할 수 있어야 함.
    @property
    def headers(self) -> 'MP3Reader':
        return self

    def __iter__(self):
        return self

    def __next__(self):
        while self.__fio.has_remain_bytes:
            try:
                header = self.__read_frame_header()
            except IOError:
                break

            self.__fio.skip(header.audio_data_length)

            return header

        raise StopIteration()
