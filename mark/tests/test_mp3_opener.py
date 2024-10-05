import unittest

from mp3_header import MP3Header
from mp3_file_io import MP3FileIo

# Red 단계에서 open_mp3_file_header 함수는 작성되지 않았지만, 테스트 코드를 작성하여 실패하는 테스트를 만들어 놓았다.
# Green 단계에서 open_mp3_file_header 함수를 작성하여 테스트를 통과시킨다.
# Refactor 단계에서 테스트 코드와 함수의 코드를 리팩토링한다.

# MP3 파일을 열기 위해 아래의 절차를 따른다.
# 1. MP3 파일이 존재하는지 확인한다.
# 2. MP3 파일의 헤더를 읽어서 MP3 파일인지 확인한다.
# 3. MP3 파일의 헤더를 분석하여 MP3 파일의 정보를 확인한다.
# 4. MP3 파일의 프레임을 분석하여 MP3 파일의 정보를 확인한다.
# 이 모든 과정이 성공적으로 진행되면, MP3 파일을 모두 읽어 메모리에 적재한다.

# 어떤 테스트를 작성하는것이 좋을까? 쓸데없는 테스트를 작성하는것은 불필요한 로드를 만드는것이다.
# 테스트 도출은 했으나 검사 방법이 잘못될 수도 있다.

file_path = "../resource/input.mp3"
permission_denied_path = "C:\Users\prtra\AppData\Local\Steam\local.vdf"

class TestMp3Opener(unittest.TestCase):
    # 파일이 존재하는지 확인
    def test_check_mp3_file_exist(self):
        mp3_opener = MP3FileIo(file_path)
        is_file_exists, message = mp3_opener.file_exists()
        self.assertTrue(is_file_exists)

    def test_check_mp3_file_exist_with_wrong_path(self):
        mp3_opener = MP3FileIo("../resource/not_exist.mp3")
        is_file_exists, message = mp3_opener.file_exists()
        print(message)
        self.assertFalse(is_file_exists)
        self.assertIn("파일을 찾을 수 없습니다", message, "파일을 찾을 수 없습니다 오류 메시지가 반환되지 않았습니다.")

    def test_check_mp3_file_exist_with_permission_error(self):
        mp3_opener = MP3FileIo(permission_denied_path)
        is_file_exists, message = mp3_opener.file_exists()
        print(message)
        self.assertFalse(is_file_exists)
        self.assertIn("권한이 없습니다", message, "권한 관련 오류 메시지가 반환되지 않았습니다.")

    # 파일 헤더 검사
    def test_open_with_check_header_is_mp3_file(self):
        mp3_opener = MP3FileIo(file_path)
        is_file_mp3 = mp3_opener.open_with_check_file_header()
        self.assertTrue(is_file_mp3)

    def test_open_with_check_header_is_not_mp3_file(self):
        mp3_opener = MP3FileIo("../resource/input.txt")
        is_file_mp3 = mp3_opener.open_with_check_file_header()
        self.assertFalse(is_file_mp3)

    # red : open_with_parse_header_is_mp3_file 함수를 작성하지 않았기 때문에 테스트가 실패한다.
    # green : open_with_parse_header_is_mp3_file 함수를 작성하여 테스트를 통과시킨다.
    # refactor : 헤더 클래스를 가져와서 헤더를 분석하는 코드를 분리하였다.
    def test_open_with_parse_header(self):
        mp3_opener = MP3FileIo(file_path)
        header = mp3_opener.open_with_parse_header()
        self.assertIsInstance(header, MP3Header)
        header.print()

    def test_open_with_parse_header_is_mp3_file(self):
        mp3_opener = MP3FileIo("../resource/input.txt")
        header = mp3_opener.open_with_parse_header()
        self.assertIsNone(header)


if __name__ == '__main__':
    unittest.main()
