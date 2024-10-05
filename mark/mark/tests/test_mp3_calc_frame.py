import unittest

from mp3_opener import MP3Opener

file_path = "../resource/input.mp3"

class TestMp3CalcFrame(unittest.TestCase):
    def test_calc_frame(self):
        mp3_opener = MP3Opener(file_path)
        header = mp3_opener.open_with_parse_header()

        # 프레임 크기 = (144 * 320,000) / 44,100 + 0 = 1044.9(반올림)
        # = 1045 bytes
        frame_size = header.calc_frame()
        self.assertEqual(frame_size, 1045)

if __name__ == '__main__':
    unittest.main()
