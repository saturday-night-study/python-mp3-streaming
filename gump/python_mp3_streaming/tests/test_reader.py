import unittest

from mp3.errors import EndOfMP3FrameError
from mp3.fileio import FileIO
from mp3.reader import MP3Reader


class TestMP3Reader(unittest.TestCase):
    def setUp(self):
        self.__exists_input_path = "./test_data/input.mp3"
        self.__fio = FileIO(self.__exists_input_path)

    def tearDown(self):
        self.__fio.close()

    def test_read_first_frame_header(self):
        reader = MP3Reader(self.__fio)
        header = reader.headers.__next__()
        self.assertIsNotNone(header)
        self.assertTrue(header.is_valid_frame)

    def test_read_invalid_format(self):
        invalid_format_input_path = "./test_data/invalid_format.jpg"
        fio = FileIO(invalid_format_input_path)

        reader = MP3Reader(fio)
        self.assertRaises(EndOfMP3FrameError, reader.headers.__next__)

        fio.close()

    def test_audio_data_length(self):
        reader = MP3Reader(self.__fio)
        header = reader.headers.__next__()
        audio_data_length = header.audio_data_length

        # TODO: 계산해보지 않으면 오디오 프레임 길이를 알 수 없는데 테스트 코드를 어떻게 작성하지?
        self.assertGreater(audio_data_length, 0)

    def test_audio_data_duration(self):
        reader = MP3Reader(self.__fio)
        header = reader.headers.__next__()
        audio_data_duration = header.audio_data_duration

        # TODO: 계산해보지 않으면 오디오 오디오 재생시간을 알 수 없는데 테스트 코드를 어떻게 작성하지?
        self.assertGreater(audio_data_duration, 0)

    def test_read_all_frame_headers(self):
        reader = MP3Reader(self.__fio)
        position = 0
        for header in reader.headers:
            self.assertTrue(header.is_valid_frame)
            self.assertEqual(header.position, position)
            position = header.position + header.frame_length

    def test_read_bytes_from_duration(self):
        reader = MP3Reader(self.__fio)
        thirty_seconds_data = reader.read_bytes_from_duration(30)
        self.assertGreater(len(thirty_seconds_data), 0)

        sixty_seconds_data = reader.read_bytes_from_duration(60)
        self.assertLess(len(sixty_seconds_data), len(thirty_seconds_data))


if __name__ == '__main__':
    unittest.main()
