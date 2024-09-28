import unittest

from python_mp3_streaming.file_io import FileIO
from python_mp3_streaming.mp3_reader import MP3Reader


class TestMP3Reader(unittest.TestCase):
    def setUp(self):
        self.__exists_input_path = "./test_data/input.mp3"
        self.__fio = FileIO()
        self.__fio.open(self.__exists_input_path)

    def tearDown(self):
        self.__fio.close()

    def test_read_first_frame_header(self):
        reader = MP3Reader(self.__fio)
        header = reader.read_nth_frame_header(0)
        self.assertIsNotNone(header)

        print(header)

    def test_read_nth_frame_header_invalid_parameter(self):
        reader = MP3Reader(self.__fio)
        header = reader.read_nth_frame_header(-1)
        self.assertIsNone(header)


if __name__ == '__main__':
    unittest.main()
