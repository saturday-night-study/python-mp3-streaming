from typing import BinaryIO, Optional


# PEP 8 정의에 따라서 클래스 네이밍
# https://peps.python.org/pep-0008/
class FileIO:
    def __init__(self):
        self.__file: Optional[BinaryIO] = None

    # 타입 힌트 추가
    def open(self, path: str):
        if not isinstance(path, str):
            print(f"입력된 파일 경로가 문자열이 아닙니다: path{type(path)}=[{path}]")
            return

        try:
            self.__file = open(path, "rb")
            return
        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없습니다: {e}")
            return
        except IOError as e:
            print(f"파일을 열 수 없습니다: {e}")
            return False
        except Exception as e:
            print(f"알 수 없는 오류 발생: {e}")
            return

    def close(self):
        if self.__file.closed:
            return

        try:
            self.__file.close()
        except Exception as e:
            print(f"파일을 닫는 중 오류 발생: {e}")

        self.__file = None

    @property
    def closed(self) -> bool:
        return self.__file is None
