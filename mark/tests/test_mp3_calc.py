import unittest

from mp3 import MP3
from mp3_file_reader import MP3FileReader

file_path = "../resource/input.mp3"

class TestMp3Calc(unittest.TestCase):
    def setUp(self):
        reader = MP3FileReader(file_path)
        reader.open()
        reader.read_all()
        reader.close()

        self.reader = reader

    def test_calc_frame(self):
        mp3 = MP3(self.reader)
        mp3.set_header()
        mp3.set_frame_size()

        self.assertEqual(mp3.get_frame_size(), 1044)

    def test_calc_frame_size(self):
        mp3 = MP3(self.reader)
        mp3.set_header()
        mp3.set_frame_size()
        mp3.set_frame_count()

        self.assertEqual(mp3.get_frame_size(), 8980)

    def test_mp3_play_time(self):
        mp3 = MP3(self.reader)
        mp3.set_header()
        mp3.set_frame_size()
        mp3.set_frame_count()
        mp3.set_play_time()
        mp3_play_time = mp3.get_play_time()

        self.assertEqual(mp3_play_time, 234.5795918367347)

if __name__ == '__main__':
    unittest.main()
