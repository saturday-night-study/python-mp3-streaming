import unittest
import reader

class CustomTests(unittest.TestCase):
   def test_empty_file_read(self):
       self.mp3FileReader = reader.MP3FileReader('./empty.mp3')
       print(self.mp3FileReader)

       mp3FileReadResult = self.mp3FileReader.read()

   def test_wrong_file_read(self):
       self.mp3FileReader = reader.MP3FileReader('./wrong.mp3')
       print(self.mp3FileReader)

       mp3FileReadResult = self.mp3FileReader.read()

       self.assertFalse(mp3FileReadResult)

   def test_origin_file_read(self):
       self.mp3FileReader = reader.MP3FileReader('./input.mp3')
       print(self.mp3FileReader)

       mp3FileReadResult = self.mp3FileReader.read()

       self.assertTrue(mp3FileReadResult)

if __name__ == '__main__':
   unittest.main()