from typing import Optional, AsyncIterable

from app.mp3.errors import EndOfMP3FrameError
from app.mp3.fileio import FileIO
from app.mp3.header import MP3FrameHeader
from app.mp3.header_spec import *


class MP3Reader:
    def __init__(self, fio: FileIO):
        self.__fio: FileIO = fio

    def __read_frame_header(self) -> Optional[MP3FrameHeader]:
        if self.__fio.closed:
            raise EndOfMP3FrameError()

        # Sync Word를 찾을 때까지 1바이트씩 이동
        while True:
            try:
                header_bytes = self.__find_sync_word() + self.__fio.read(FRAME_HEADER_SIZE - 2)
            except EOFError:
                raise EndOfMP3FrameError()

            if len(header_bytes) < FRAME_HEADER_SIZE:
                raise EndOfMP3FrameError()

            header: Optional[MP3FrameHeader] = MP3Reader.__parse_header(header_bytes)
            if header.is_valid_frame:
                header.audio_data = self.__fio.read(header.audio_data_length)
                return header

            self.__fio.skip(-2)

    # 재귀 함수로 만들고 싶었지만 파이썬에서는 재귀 함수의 깊이 제한이 있어서 RecursionError를 발생시킴
    # 기본 재귀 깊이는 1000회이며, sys.setrecursionlimit() 함수로 변경은 가능하지만 권장하지 않음
    # 재귀 깊이가 예상 가능 범위일 경우만 재귀 함수를 사용하는게 바람직할 것으로 보임
    def __find_sync_word(self) -> bytes:
        first_byte: Optional[bytes] = None
        second_byte: Optional[bytes] = None
        while True:
            if first_byte is None:
                first_byte = self.__fio.read(1)

            if MP3Reader.__get_bits(first_byte, SYNC_WORD_FIRST_BYTE_RANGE) == SYNC_WORD_FIRST_BYTE:
                second_byte = self.__fio.read(1)
                if MP3Reader.__get_bits(second_byte, SYNC_WORD_SECOND_BYTE_RANGE) == SYNC_WORD_SECOND_BYTE:
                    return first_byte + second_byte
            else:
                first_byte = second_byte

    @staticmethod
    def __parse_header(data: bytes) -> Optional[MP3FrameHeader]:
        return MP3FrameHeader(
            sync_word=MP3Reader.__get_bits(data, SYNC_WORD_RANGE),
            version=MP3Reader.__get_bits(data, VERSION_RANGE),
            layer=MP3Reader.__get_bits(data, LAYER_RANGE),
            protection_bit=MP3Reader.__get_bits(data, PROTECTION_BIT_RANGE),
            bitrate_index=MP3Reader.__get_bits(data, BITRATE_INDEX_RANGE),
            sampling_rate_index=MP3Reader.__get_bits(data, SAMPLING_RATE_RANGE),
            padding_bit=MP3Reader.__get_bits(data, PADDING_BIT_RANGE),
            private_bit=MP3Reader.__get_bits(data, PRIVATE_BIT_RANGE),
            channel_mode=MP3Reader.__get_bits(data, CHANNEL_MODE_RANGE),
            mode_extension=MP3Reader.__get_bits(data, MODE_EXTENSION_RANGE),
            copyright=MP3Reader.__get_bits(data, COPYRIGHT_RANGE),
            original=MP3Reader.__get_bits(data, ORIGINAL_RANGE),
            emphasis=MP3Reader.__get_bits(data, EMPHASIS_RANGE),
            audio_data=bytes(0)
        )

    @staticmethod
    def __get_bits(data: bytes, frame_header_range: FrameHeaderRange) -> int:
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
        self.__fio.reset()

        return self

    def __next__(self):
        while self.__fio.has_remain_bytes:
            header = self.__read_frame_header()

            return header

        raise EndOfMP3FrameError()

    def read_bytes_from_duration(self, seconds: int) -> bytes:
        duration = 0
        for header in self.headers:
            duration += header.audio_data_duration
            if duration >= seconds:
                data = self.__fio.read(self.__fio.file_size - self.__fio.current_position)
                return data

        return bytes()

    async def content_stream_from_duration(self, seconds: int, closable: bool = False) -> AsyncIterable[bytes]:
        duration = 0
        for header in self.headers:
            duration += header.audio_data_duration
            if duration < seconds:
                continue

            yield header.to_bytes() + header.audio_data

        if closable:
            self.__fio.close()
