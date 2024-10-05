import unittest
import mp3_file_reader

from mp3_file_reader import InvalidFrameSyncError

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

    # [실패] 빈 MP3 파일을 파싱한다.
    def test_parse_empty_file(self):
        with self.assertRaises(ValueError):
            self.mp3_file_reader = mp3_file_reader.MP3FileReader("./assets/empty.mp3")
        
            mp3_file = self.mp3_file_reader.parse()
            print(mp3_file)

    # [실패] 잘못된 헤더 타입을 가진 파일을 파싱한다.
    def test_parse_wrong_file(self):
        with self.assertRaises(InvalidFrameSyncError):
            self.mp3_file_reader = mp3_file_reader.MP3FileReader("./assets/wrong.mp3")

            mp3_file = self.mp3_file_reader.parse()
            print(mp3_file)

    # [성공] 정상 테스트 MP3File 파싱
    def test_parse_file(self): 
        self.mp3_file_reader = mp3_file_reader.MP3FileReader("./assets/input.mp3")
        
        mp3_file = self.mp3_file_reader.parse()
        print(mp3_file)

if __name__ == '__main__':
   unittest.main()