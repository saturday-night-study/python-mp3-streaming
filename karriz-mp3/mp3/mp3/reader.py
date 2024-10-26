import os

from . import model, error
from . import parser

class MP3FileReader:
    def __init__(self, file_path:str):
        file_size = os.path.getsize(file_path)

        if file_size == 0:
            raise error.EmptySizeFileError

        # CBR, VBR에 따라 비트레이트가 바뀔 수 있는데... reader가 필요할까
        # read -> trim -> 제공 하면 memory에 데이터가 너무 많이 쌓이는데 ..?
        self.__mp3 = model.MP3()
        self.__mp3.file_path = file_path

    def read(self) -> model.MP3:
        mp3_file = open(self.__mp3.file_path, 'rb')

        while True:
            try:
                frame_header_parser = parser.MP3FrameHeaderParser(mp3_file.read(4))

                self.__mp3.total_duration += frame_header_parser.get_frame_duration()
                mp3_file.seek(frame_header_parser.get_frame_size()-4, 1)

                self.__mp3.total_frame += 1

            except error.InValidFrameHeaderSizeError:
                break

        mp3_file.close()

        return self.__mp3

    def read_skip_frame(self, skipped_frame_size: int = 1) -> model.MP3:
        mp3_file = open(self.__mp3.file_path, 'rb')
        skipped_mp3_file = open(f"{self.__mp3.file_path}.skip", 'wb')

        frame_count = 0

        skipped_mp3 = model.MP3()
        skipped_mp3.file_path = f"{self.__mp3.file_path}.skip"

        while True:
            try:
                frame_header_bytes = mp3_file.read(4)
                frame_header_parser = parser.MP3FrameHeaderParser(frame_header_bytes)

                frame_bytes = mp3_file.read(frame_header_parser.get_frame_size()-4)

                if frame_count % skipped_frame_size != 0:
                    skipped_mp3_file.write(frame_header_bytes)
                    skipped_mp3_file.write(frame_bytes)
                    
                    skipped_mp3.total_duration += frame_header_parser.get_frame_duration()
                    skipped_mp3.total_frame += 1

                frame_count += 1
            
            except error.InvalidFrameSyncError:
                mp3_file.seek(-3, 1)

            except error.InValidFrameHeaderSizeError:
                break

        mp3_file.close()

        return skipped_mp3
