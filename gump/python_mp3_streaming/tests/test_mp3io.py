import unittest

class TestMP3IO(unittest.TestCase):
    def test_file_exists(self):
        # PEP 8 정의에 따라서 클래스 네이밍
        # https://peps.python.org/pep-0008/
        mp3io = MP3IO()
        file = mp3io.open("./test_data/input.mp3")
        self.assertIsNotNone(file)

if __name__ == '__main__':
    unittest.main()