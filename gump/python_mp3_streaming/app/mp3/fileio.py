from typing import BinaryIO, Optional, cast


# PEP 8 정의에 따라서 클래스 네이밍
# https://peps.python.org/pep-0008/
class FileIO:
    def __init__(self, path: str, mode: str = "rb"):
        self.__file: Optional[BinaryIO] = None

        if not isinstance(path, str):
            raise ValueError(f"입력된 파일 경로가 문자열이 아닙니다: path{type(path)}=[{path}]")
        if mode not in ["rb", "wb", "ab", "rb+", "wb+", "ab+"]:
            raise ValueError(f"모드가 올바르지 않습니다: mode{type(mode)}=[{mode}]")

        self.__file = FileIO.__open(path, mode)

    @staticmethod
    def __open(path: str, mode: str) -> BinaryIO:
        try:
            return cast(BinaryIO, open(path, mode))
        except FileNotFoundError as e:
            raise FileNotFoundError(f"파일을 찾을 수 없습니다: {e}")
        except IsADirectoryError as e:
            raise IsADirectoryError(f"파일 경로가 디렉터리입니다: {e}")
        except IOError as e:
            raise IOError(f"파일을 열 수 없습니다: {e}")
        except Exception as e:
            raise Exception(f"알 수 없는 오류 발생: {e}")

    def __del__(self):
        self.close()

    def close(self):
        if self.__file is None or self.__file.closed:
            return

        try:
            self.__file.close()
        except Exception as e:
            raise Exception(f"파일을 닫는 중 오류 발생: {e}")
        finally:
            self.__file = None

    @property
    def closed(self) -> bool:
        return self.__file is None or self.__file.closed

    @property
    def file_size(self) -> int:
        if self.closed:
            return 0

        # https://docs.python.org/3/library/io.html#io.IOBase.seek
        current_position = self.__file.tell()
        self.__file.seek(0, 2)
        file_size = self.__file.tell()
        self.__file.seek(current_position, 0)

        return file_size

    @property
    def has_remain_bytes(self) -> bool:
        if self.closed:
            return False

        return self.file_size > self.__file.tell()

    @property
    def current_position(self) -> int:
        if self.closed:
            raise IOError("파일이 닫혀 있습니다.")

        return self.__file.tell()

    def read(self, n: int) -> bytes:
        if self.closed:
            raise IOError("파일이 닫혀 있습니다.")

        data = self.__file.read(n)
        data_length = len(data)
        if data_length == 0:
            raise EOFError()

        return data

    def skip(self, n: int):
        if self.closed:
            raise IOError("파일이 닫혀 있습니다.")

        self.__file.seek(n, 1)

    def reset(self):
        if self.closed:
            raise IOError("파일이 닫혀 있습니다.")

        self.__file.seek(0, 0)

    def write(self, data: bytes):
        if self.closed:
            raise IOError("파일이 닫혀 있습니다.")

        self.__file.write(data)
