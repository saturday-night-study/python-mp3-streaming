import unittest
import mp3_file_reader

from mp3_file_reader import InvalidFrameSyncError

class MP3FileParserTests(unittest.TestCase):    
    # [실패] mp3 file이 존재 하지 않는 경로로 읽는다    
    def test_new_mp3file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.mp3_file_reader = mp3_file_reader.MP3FileParser("./test.mp3")

    # [실패] file이 아닌 경로를 읽는다
    def test_new_mp3file_read_directory(self):
        with self.assertRaises(IsADirectoryError):
            self.mp3_file_reader = mp3_file_reader.MP3FileParser("./assets")

    # [성공] 정상경로에 있는 파일을 읽는다
    def test_new_mp3file_read(self):
        self.mp3_file_reader = mp3_file_reader.MP3FileParser("./assets/input.mp3")

        self.assertIsNotNone(self.mp3_file_reader)

    # [실패] 빈 MP3 파일을 파싱한다.
    def test_parse_empty_file(self):
        with self.assertRaises(ValueError):
            self.mp3_file_reader = mp3_file_reader.MP3FileParser("./assets/empty.mp3")
        
            self.mp3_file_reader.parse()

    # [실패] 잘못된 헤더 타입을 가진 파일을 파싱한다.
    def test_parse_wrong_file(self):
        with self.assertRaises(InvalidFrameSyncError):
            self.mp3_file_reader = mp3_file_reader.MP3FileParser("./assets/wrong.mp3")

            self.mp3_file_reader.parse()

    # [성공] 정상 테스트 MP3File 파싱
    def test_parse_file(self): 
        self.mp3_file_reader = mp3_file_reader.MP3FileParser("./assets/input.mp3")
        
        mp3_file = self.mp3_file_reader.parse()
        print(mp3_file)

class MP3FileTrimmerTests(unittest.TestCase):    
    # [실패] 잘못 된 파일로 트리밍 후 파일 저장 실패
    def test_trim_wrong_file(self):
        pass

if __name__ == '__main__':
   unittest.main()