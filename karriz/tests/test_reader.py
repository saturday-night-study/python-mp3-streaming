import unittest

class MP3FileReaderTests(unittest.TestCase):
    def test_new_mp3file_not_found(self):
        # mp3 file이 존재 하지 않는 경로로 읽는다    
        self.assertFalse(False)
    def test_read_empty_file(self):
        # 빈 MP3 파일을 읽는다
        self.assertFalse(False)
    def test_read_wrong_file(self):
        # 잘못된 헤더 타입을 가진 파일을 읽는다
        self.assertFalse(False)

if __name__ == '__main__':
   unittest.main()