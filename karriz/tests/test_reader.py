import unittest
import mp3_file_reader

class MP3FileReaderTests(unittest.TestCase):
    def test_read_mp3_file(self):
        reader = mp3_file_reader.MP3FileReader("./assets/input.mp3")

        mp3_file = reader.read()

        # 읽은 파일 경로 확인
        self.assertEqual(mp3_file.file_path, "./assets/input.mp3")

        # 재생 시간 3분 54초를 기준으로 계산
        self.assertEqual(int(mp3_file.total_duration), 234)

class MP3FileTrimmerTests(unittest.TestCase):
    def setUp(self):
        reader = mp3_file_reader.MP3FileReader("./assets/input.mp3")
        
        self.mp3_file = reader.read()

    def test_trim_mp3_file(self):
        mp3_file_trimmer = mp3_file_reader.MP3FileTrimmer(self.mp3_file)

        # mp3 파일을 프레임 단위로 trimming
        trimmed_mp3 = mp3_file_trimmer.trim(0, 1000)

        # trimming 된 이후 총 duration이 1000 프레임 만큼 잘렸는지 확인
        # 1 프레임당 대략 0.026s = 1000 프레임은 26s
        self.assertEqual(int(trimmed_mp3.total_duration), 26)

if __name__ == '__main__':
   unittest.main()