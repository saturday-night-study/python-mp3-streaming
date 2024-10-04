import unittest

# PYTHONPATH=.. 으로 설정해야 패키지 import 가능
from python_mp3_streaming.file_io import FileIO


class TestFileIO(unittest.TestCase):
    # setUp 메서드는 각 테스트 메서드를 실행하기 전에 호출됨
    # setUp 메서드를 이용해서 중복된 초기화 작업을 줄임
    def setUp(self):
        self.__exists_input_path = "./test_data/input.mp3"
        self.__not_exists_input_path = "./test_data/not_exists.mp3"
        self.__empty_input_path = "./test_data/empty.mp3"
        self.__directory_input_path = "./test_data"
        self.__exists_input_file_size = 9375481

    # 아래는 테스트 케이스
    # 테스트 케이스의 호출 순서는 정의 순서가 아닌 메서드 이름 알파벳 순서로 호출
    # 호출 순서를 강제하고 싶을 경우 unittest.TestSuite()를 사용

    # 메서드명 변경
    # 존재하는 파일이 입력된 경우 파일 객체를 반환하는지 확인
    def test_open_exists_file(self):
        fio = FileIO(self.__exists_input_path)
        self.assertFalse(fio.closed)

    # 존재하지 않는 파일이 입력된 경우 Error를 발생시키는지 확인
    def test_open_not_exists_file(self):
        self.assertRaises(FileNotFoundError, FileIO, self.__not_exists_input_path)

    # 파일 경로가 문자열이 아닌 타입으로 입력된 경우 Error를 발생시키는지 확인
    def test_open_invalid_parameter_type(self):
        self.assertRaises(ValueError, FileIO, 123)

    # 파일 경로가 디렉터리일 경우 Error를 발생시키는지 확인
    def test_open_directory(self):
        self.assertRaises(IsADirectoryError, FileIO, self.__directory_input_path)

    # 파일 객체를 닫는지 확인
    def test_close(self):
        fio = FileIO(self.__exists_input_path)
        fio.close()
        self.assertTrue(fio.closed)

    def test_read(self):
        fio = FileIO(self.__exists_input_path)

        read_bytes = 4
        data: bytes = fio.read(read_bytes)
        self.assertEqual(len(data), read_bytes)

    def test_read_closed_file(self):
        fio = FileIO(self.__exists_input_path)
        fio.close()

        read_bytes = 1
        self.assertRaises(IOError, fio.read, read_bytes)

    def test_read_eof(self):
        fio = FileIO(self.__empty_input_path)

        read_bytes = 1
        self.assertRaises(EOFError, fio.read, read_bytes)

    def test_file_size(self):
        fio = FileIO(self.__exists_input_path)
        self.assertEqual(fio.file_size, self.__exists_input_file_size)

    def test_has_remain_bytes(self):
        fio = FileIO(self.__exists_input_path)
        self.assertTrue(fio.has_remain_bytes)

        fio.read(self.__exists_input_file_size)
        self.assertFalse(fio.has_remain_bytes)

    def test_current_position(self):
        fio = FileIO(self.__exists_input_path)
        self.assertEqual(fio.current_position, 0)

        read_bytes = 4
        fio.read(read_bytes)
        self.assertEqual(fio.current_position, read_bytes)

# __main__ 변수는 모듈을 직접 실행하면 '__main__'이 되고, 임포트하면 모듈 이름이 됨
if __name__ == '__main__':
    unittest.main()