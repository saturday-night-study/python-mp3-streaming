import unittest
import mp3_file_reader

class MP3FileReaderTests(unittest.TestCase):    
    def test_read_mp3_file_not_fund(self):
        with self.assertRaises(FileNotFoundError):
            reader = mp3_file_reader.MP3FileReader("./test.mp3")

            reader.read()

    def test_read_directory(self):
        with self.assertRaises(IsADirectoryError):
            reader = mp3_file_reader.MP3FileReader("./assets")

            reader.read()

    def test_read_mp3_file(self):
        reader = mp3_file_reader.MP3FileReader("./assets/input.mp3")

        reader.read()

if __name__ == '__main__':
   unittest.main()