import unittest

from mp3_file_io import MP3FileIo
from mp3_frame import MP3Frame
from mp3_header_factory import MP3HeaderFactory

# 삭제예정
class TestMP3New(unittest.TestCase):
    def test_all_situation(self):
        # load mp3 file
        io = MP3FileIo()
        io.open("../resource/input.mp3")

        frames: list[MP3Frame] = []
        while True:
            header_bytes = io.read(4)
            if len(header_bytes) < 4:
                break

            if MP3HeaderFactory.is_header(header_bytes) is False:
                break

            header = MP3HeaderFactory.create(header_bytes)
            frame_size = header.calc_frame_size()

            data_size = frame_size - 4
            data_bytes = io.read(data_size)
            if len(data_bytes) < data_size:
                break

            # Create the frame and add to the list
            frame = MP3Frame(header, header_bytes, data_bytes)
            frames.append(frame)

        io.close()

        len(frames)


if __name__ == '__main__':
    unittest.main()
