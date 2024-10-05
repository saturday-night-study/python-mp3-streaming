import os.path

import mp3_header
import mp3_header_factory



class MP3Opener:
    def __init__(self, file_path):
        self.file_path = file_path

    def file_exists(self):
        return os.path.exists(self.file_path)

    # TODO : 리팩터링 필요
    # open_with_check_file_header와 open_with_parse_header 메서드는 단일 책임 원칙을 위배하는것 같아. 그러다보니 재사용성과 테스트 용이성이 떨어진다는 생각이 들어. 구체적인 상황에 대해서만 사용할 수 있고, 많은 할일에 대한 세밀한 테스트 작성이 어려운거지 😇 리팩터링 해볼 수 있을까?
    def open_with_check_file_header(self):
        try:
            file_obj = open(self.file_path, 'rb')
            header = file_obj.read(2)
            file_obj.close()

            # Convert the header to an integer
            header_int = int.from_bytes(header, byteorder='big')

            # MP3 Sync Word가(=11비트) 1로 시작하는지 확인한다.
            # 0xFF = 1111 1111
            # 0xE0 = 1110 0000
            if (header_int & 0xFFE0) != 0xFFE0:
                print("MP3 SYNC WORD not detected")
                return False
            return True
        except IOError as e:
            if isinstance(e, EOFError):
                print(f"파일이 너무 작습니다: {e}")
            else:
                print(f"파일을 열 수 없습니다: {e}")

            return False

    def open_with_parse_header(self):
        try:
            file_obj = open(self.file_path, 'rb')
            header_bytes = file_obj.read(4)
            file_obj.close()

            if len(header_bytes) < 4:
                print("파일이 너무 작습니다")
                return None

            return mp3_header_factory.MP3HeaderFactory.create(bytes)
        except IOError as e:
            print(f"파일을 열 수 없습니다: {e}")
            return None
        pass
