from mp3_file_io import MP3FileIo
from mp3_frame import MP3Frame
from mp3_header_factory import MP3HeaderFactory


class Mp3FrameFactory:
    @staticmethod
    def create(io : MP3FileIo) -> list[MP3Frame]:
        frames = []
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

            frame = MP3Frame(header, header_bytes, data_bytes)
            frames.append(frame)

        return frames
