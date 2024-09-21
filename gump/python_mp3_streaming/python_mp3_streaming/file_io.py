from typing import BinaryIO, Optional


# PEP 8 정의에 따라서 클래스 네이밍
# https://peps.python.org/pep-0008/
class FileIO:
    def __init__(self):
        self.file: Optional[BinaryIO] = None

    # 타입 힌트 추가
    def open(self, path: str) -> bool:
        if not isinstance(path, str):
            print(f"입력된 파일 경로가 문자열이 아닙니다: [{path}] => {type(path)}")
            return False

        try:
            self.file = open(path, "rb")
            return True
        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없습니다: {e}")
            return False
        except IOError as e:
            print(f"파일을 열 수 없습니다: {e}")
            return False
        except Exception as e:
            print(f"알 수 없는 오류 발생: {e}")
            return False

    def close(self):
        if self.file.closed:
            return

        try:
            self.file.close()
        except Exception as e:
            print(f"파일을 닫는 중 오류 발생: {e}")

        self.file = None

    @property
    def closed(self) -> bool:
        return self.file is None