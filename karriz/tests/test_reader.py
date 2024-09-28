import unittest
import mp3_file_reader

class MP3FileReaderTests(unittest.TestCase):
    # [실패] mp3 file이 존재 하지 않는 경로로 읽는다    
    def test_new_mp3file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.mp3_file_reader = mp3_file_reader.MP3FileReader("./test.mp3")

    # [실패] file이 아닌 경로를 읽는다
    def test_new_mp3file_read_directory(self):
        with self.assertRaises(IsADirectoryError):
            self.mp3_file_reader = mp3_file_reader.MP3FileReader("./assets")

    # [성공] 정상경로에 있는 파일을 읽는다
    def test_new_mp3file_read(self):
        self.mp3_file_reader = mp3_file_reader.MP3FileReader("./assets/input.mp3")

        self.assertIsNotNone(self.mp3_file_reader)

    # 빈 MP3 파일을 읽는다
    def test_read_empty_file(self):
        self.assertFalse(False)

    # 잘못된 헤더 타입을 가진 파일을 읽는다
    def test_read_wrong_file(self):
        self.assertFalse(False)

if __name__ == '__main__':
   unittest.main()