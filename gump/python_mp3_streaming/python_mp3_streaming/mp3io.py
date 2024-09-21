# PEP 8 정의에 따라서 클래스 네이밍
# https://peps.python.org/pep-0008/
class MP3IO:
    # 타입 힌트 추가
    def open(self, path: str):
        if not isinstance(path, str):
            print(f"입력된 파일 경로가 문자열이 아닙니다: [{path}] => {type(path)}")
            return None

        try:
            with open(path, "rb") as f:
                return f
        except FileNotFoundError as e:
            print(f"파일을 찾을 수 없습니다: {e}")
            return None
        except IOError as e:
            print(f"파일을 열 수 없습니다: {e}")
            return None
        except Exception as e:
            print(f"알 수 없는 오류 발생: {e}")
            return None