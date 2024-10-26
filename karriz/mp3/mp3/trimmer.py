from . import model, parser, error

class MP3FileTrimmer:
    def __init__(self, mp3:model.MP3):
        self.__mp3 = mp3

    def trim(self, start:int, end:int, output_file_path:str) -> model.MP3:
        mp3_file = open(self.__mp3.file_path, 'rb')
        trimmed_output_file = open(output_file_path, 'wb')

        trimmed_mp3 = model.MP3()
        current_frame = 0

        while True:
            try:
                frame_header_bytes = mp3_file.read(4)
                frame_header_parser = parser.MP3FrameHeaderParser(frame_header_bytes)

                trimmed_mp3.total_duration += frame_header_parser.get_frame_duration()
                frame_bytes = mp3_file.read(frame_header_parser.get_frame_size()-4)
                
                current_frame += 1

                if current_frame >= start and current_frame <= end:
                    trimmed_output_file.write(frame_header_bytes)
                    trimmed_output_file.write(frame_bytes)

                if current_frame > end:
                    break

            except error.InValidFrameHeaderSizeError:
                break

        trimmed_mp3.total_frame = current_frame

        mp3_file.close()
        trimmed_output_file.close()

        return trimmed_mp3
