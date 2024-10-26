import unittest

from mp3 import MP3
from mp3Factory import MP3Factory

file_path = "../resource/input.mp3"

class TestMp3(unittest.TestCase):
    def setUp(self):
        self.mp3 = MP3Factory.create_by_file_path(file_path)

    def test_mp3_cut(self):
        new_mp3 = MP3Factory.create_by_cut(self.mp3, 10, 20)
        new_mp3.save("../resource/output_cut_10_20.mp3")

    def test_mp3_set_down_speed(self):
        output = MP3Factory.create_speed_down(self.mp3,2)
        output.save("../resource/output_down_x2.mp3")

    def test_mp3_set_up_speed(self):
        output = MP3Factory.create_speed_up(self.mp3, 2)
        output.save("../resource/output_up_x2.mp3")

if __name__ == '__main__':
    unittest.main()
