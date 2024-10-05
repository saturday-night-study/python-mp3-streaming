import unittest

from mp3_opener import MP3Opener

file_path = "../resource/input.mp3"

class TestMp3CalcFrame(unittest.TestCase):
    def test_calc_frame(self):
        mp3_opener = MP3Opener(file_path)
        header = mp3_opener.open_with_check_file_header()

        header.calc_frame()


if __name__ == '__main__':
    unittest.main()
