import unittest

# PYTHONPATH=.. 으로 설정해야 패키지 import 가능
from python_mp3_streaming.file_io import FileIO

class TestFileIO(unittest.TestCase):
    # setUp 메서드는 각 테스트 메서드를 실행하기 전에 호출됨
    # setUp 메서드를 이용해서 중복된 초기화 작업을 줄임
    def setUp(self):
        self.__exists_input_path = "./test_data/input.mp3"
        self.__not_exists_input_path = "./test_data/not_exists.mp3"
        self.__file_io = FileIO()

    # 아래는 테스트 케이스
    # 테스트 케이스의 호출 순서는 정의 순서가 아닌 메서드 이름 알파벳 순서로 호출
    # 호출 순서를 강제하고 싶을 경우 unittest.TestSuite()를 사용

    # 메서드명 변경
    # 존재하는 파일이 입력된 경우 파일 객체를 반환하는지 확인
    def test_open_exists_file(self):
        file = self.__file_io.open(self.__exists_input_path)
        self.assertIsNotNone(file)

    # 존재하지 않는 파일이 입력된 경우 None을 반환하는지 확인
    def test_open_not_exists_file(self):
        file = self.__file_io.open(self.__not_exists_input_path)
        self.assertIsNone(file)

    # 파일 경로가 문자열이 아닌 타입으로 입력된 경우 None을 반환하는지 확인
    def test_open_invalid_parameter_type(self):
        file = self.__file_io.open(123)
        self.assertIsNone(file)

    # 파일 객체를 닫는지 확인
    def test_close_file(self):
        file = self.__file_io.open(self.__exists_input_path)
        self.assertIsNotNone(file)
        self.__file_io.close(file)
        self.assertTrue(file.closed)

# __main__ 변수는 모듈을 직접 실행하면 '__main__'이 되고, 임포트하면 모듈 이름이 됨
if __name__ == '__main__':
    unittest.main()