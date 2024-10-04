from typing import BinaryIO, Optional


# PEP 8 정의에 따라서 클래스 네이밍
# https://peps.python.org/pep-0008/
class FileIO:
    def __init__(self, path: str):
        self.__file: Optional[BinaryIO] = None
        self.__open(path)

    # 타입 힌트 추가
    def __open(self, path: str):
        if not isinstance(path, str):
            raise ValueError(f"입력된 파일 경로가 문자열이 아닙니다: path{type(path)}=[{path}]")

        try:
            self.__file = open(path, "rb")
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
        last_position = self.__file.tell()
        self.__file.seek(current_position, 0)

        return last_position - current_position

    def read(self, n: int) -> bytes:
        if self.closed:
            raise IOError("파일이 닫혀 있습니다.")

        data = self.__file.read(n)
        data_length = len(data)
        if data_length == 0:
            raise EOFError()

        return data
