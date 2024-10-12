import unittest
import mp3_file_reader

class MP3FileReaderTests(unittest.TestCase):
    def test_read_mp3_file(self):
        reader = mp3_file_reader.MP3FileReader("./assets/input.mp3")

        mp3 = reader.read()

        # 읽은 파일 경로 확인
        self.assertEqual(mp3.file_path, "./assets/input.mp3")

        # 재생 시간 3분 54초를 기준으로 계산
        self.assertEqual(int(mp3.total_duration), 234)

if __name__ == '__main__':
   unittest.main()