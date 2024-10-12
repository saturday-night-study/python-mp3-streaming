import unittest
from concurrent.futures import ThreadPoolExecutor

from app.mp3.errors import EndOfMP3FrameError
from app.mp3.fileio import FileIO
from app.mp3.reader import MP3Reader


class TestMP3Reader(unittest.TestCase):
    def setUp(self):
        # 메타데이터가 존재하는 original.mp3 변경
        self.__exists_input_path = "./test_data/original.mp3"
        self.__fio = FileIO(self.__exists_input_path)

    def tearDown(self):
        self.__fio.close()

    def test_read_first_frame_header(self):
        reader = MP3Reader(self.__fio)
        header = reader.headers.__next__()
        self.assertIsNotNone(header)
        self.assertTrue(header.is_valid_frame)

    def test_read_invalid_format(self):
        invalid_format_input_path = "./test_data/invalid_format.txt"
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
        for header in reader.headers:
            self.assertTrue(header.is_valid_frame)

    def test_read_all_frame_headers_within_the_timeout(self):
        def read_all_frame_headers():
            reader = MP3Reader(self.__fio)
            for _ in reader.headers:
                pass

        with ThreadPoolExecutor() as executor:
            future = executor.submit(read_all_frame_headers)
            timeout = 1
            try:
                future.result(timeout=timeout)
            except TimeoutError:
                self.fail(f"MP3 파일을 읽는 중에 {timeout}초 타임아웃이 발생했습니다.")

    def test_read_bytes_from_duration(self):
        reader = MP3Reader(self.__fio)
        thirty_seconds_data = reader.read_bytes_from_duration(30)
        self.assertGreater(len(thirty_seconds_data), 0)

        sixty_seconds_data = reader.read_bytes_from_duration(60)
        self.assertLess(len(sixty_seconds_data), len(thirty_seconds_data))


if __name__ == '__main__':
    unittest.main()
