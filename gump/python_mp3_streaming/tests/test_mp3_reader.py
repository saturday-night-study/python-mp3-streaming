import unittest

from python_mp3_streaming.file_io import FileIO
from python_mp3_streaming.mp3_reader import MP3Reader


class TestMP3Reader(unittest.TestCase):
    def setUp(self):
        self.__exists_input_path = "./test_data/input.mp3"
        self.__fio = FileIO(self.__exists_input_path)

    def tearDown(self):
        self.__fio.close()

    def test_read_first_frame_header(self):
        reader = MP3Reader(self.__fio)
        header = reader.read_nth_frame_header(0)
        self.assertIsNotNone(header)

        print(repr(header))
        print(str(header))

        self.assertTrue(header.is_valid_frame)

    def test_read_nth_frame_header_invalid_parameter(self):
        reader = MP3Reader(self.__fio)
        header = reader.read_nth_frame_header(-1)
        self.assertIsNone(header)

    def test_read_nth_frame_header_invalid_format(self):
        invalid_format_input_path = "./test_data/invalid_format.jpg"
        fio = FileIO(invalid_format_input_path)

        reader = MP3Reader(fio)
        header = reader.read_nth_frame_header(0)
        self.assertIsNotNone(header)
        self.assertFalse(header.is_valid_frame)

        fio.close()

    def test_frame_length(self):
        reader = MP3Reader(self.__fio)
        header = reader.read_nth_frame_header(0)
        audio_data_length = header.audio_data_length

        # TODO: 계산해보지 않으면 오디오 프레임 길이를 알 수 없는데 테스트 코드를 어떻게 작성하지?
        self.assertGreater(audio_data_length, 0)

    # def test_read_all_frame_headers(self):
    #     reader = MP3Reader(self.__fio)
    #     for header in reader.headers:
    #         self.assertTrue(header.is_valid_frame)
        

if __name__ == '__main__':
    unittest.main()
