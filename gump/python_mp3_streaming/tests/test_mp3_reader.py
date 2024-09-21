import unittest

from python_mp3_streaming.file_io import FileIO
from python_mp3_streaming.mp3_reader import MP3Reader


class TestMP3Reader(unittest.TestCase):
    def setUp(self):
        self.__exists_input_path = "./test_data/input.mp3"
        self.__file_io = FileIO()

    def test_read_first_frame_header(self):
        reader = MP3Reader(self.__file_io)
        frame_header = reader.read_nth_frame_header(0)
        self.assertIsNotNone(frame_header)

    def test_read_nth_frame_header_invalid_parameter(self):
        reader = MP3Reader(self.__file_io)
        frame_header = reader.read_nth_frame_header(-1)
        self.assertIsNone(frame_header)


if __name__ == '__main__':
    unittest.main()
