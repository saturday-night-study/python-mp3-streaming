import unittest

from mp3 import MP3
from mp3_file_io import MP3FileIo

file_path = "../resource/input.mp3"

class TestMp3(unittest.TestCase):
    def setUp(self):
        reader = MP3FileIo()
        reader.open(file_path)
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

    def test_mp3_cut(self):
        mp3 = MP3(self.reader)
        mp3.set_header()
        mp3.set_frame_size()
        mp3.set_frame_count()
        mp3.set_play_time()

        output = mp3.cut(0, 20)
        output.save("../resource/output.mp3")


    def test_mp3_set_down_speed(self):
        mp3 = MP3(self.reader)
        mp3.set_header()
        mp3.set_frame_size()
        mp3.set_frame_count()
        mp3.set_play_time()

        output = mp3.change_speed_down(2)
        output.save("../resource/output_down_x2.mp3")

    def test_mp3_set_up_speed(self):
        mp3 = MP3(self.reader)
        mp3.set_header()
        mp3.set_frame_size()
        mp3.set_frame_count()
        mp3.set_play_time()

        output = mp3.change_speed_up(2)
        output.save("../resource/output_up_x2.mp3")

if __name__ == '__main__':
    unittest.main()
