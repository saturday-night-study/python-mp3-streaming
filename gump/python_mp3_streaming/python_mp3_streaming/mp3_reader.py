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

        header = self.__read_frame_header()

        return header

    def __read_frame_header(self) -> Optional[MP3FrameHeader]:
        if self.__fio.closed:
            raise IOError()

        # TODO: 현재 파일 포인터 위치를 모르기 때문에 파일 포인터 위치를 초기화 한 후 읽어야 함
        # TODO: 4바이트를 읽는 것이 아니라 1바이트씩 이동하면서 찾아야 함

        position = self.__fio.current_position
        data = self.__fio.read(FRAME_HEADER_SIZE)
        if len(data) < FRAME_HEADER_SIZE:
            raise EOFError()

        header = MP3FrameHeader(
            position=position,
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
