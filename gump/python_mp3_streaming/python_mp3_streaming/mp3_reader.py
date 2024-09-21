from typing import Optional

from python_mp3_streaming.file_io import FileIO
from python_mp3_streaming.mp3_frame_header import MP3FrameHeader


class MP3Reader:
    def __init__(self, file_io: FileIO):
        self.__file: FileIO = file_io

    def read_nth_frame_header(self, n: int) -> Optional[MP3FrameHeader]:
        if not isinstance(n, int):
            print(f"입력 파라미터 타입 오류: n{type(n)}=[{n}]")
            return None
        elif n < 0:
            print(f"입력 파라미터 범위 오류: n{type(n)}=[{n}]")
            return None

        return MP3FrameHeader()
