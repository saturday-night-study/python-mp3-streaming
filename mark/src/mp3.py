import mp3_header_factory


class MP3:
    def __init__(self, file_reader):
        self.play_time = None
        self.frame_size = 0
        self.frame_count = 0
        self.header = None
        self.file_io = file_reader

    def set_header(self):
        header_bytes = self.file_io.get(4)
        self.header = mp3_header_factory.MP3HeaderFactory.create(header_bytes)

    def get_header(self):
        return self.header

    def set_frame_size(self):
        self.frame_size = self.header.calc_frame_size()

    def get_frame_size(self):
        return self.frame_size

    def set_frame_count(self):
        offset = 4 # 태그 없어서 고정 offset 사용
        self.frame_count = (self.file_io.get_size() - offset) // self.frame_size

    def get_frame_count(self):
        return self.set_frame_count

    def set_play_time(self):
        frame_duration = 1152 / self.header.sampling_rate
        self.play_time = self.frame_count * frame_duration

    def get_play_time(self):
        return self.play_time

    def cut(self, start_time, end_time):
        start_frame = int(start_time * self.header.sampling_rate / 1152)
        end_frame = int(end_time * self.header.sampling_rate / 1152)

        frame_size = self.header.calc_frame_size()
        start_byte = start_frame * frame_size
        end_byte = end_frame * frame_size

        io = self.file_io.cut_frames(start_byte, end_byte)
        return MP3(io)

    def save(self, file_path):
        self.file_io.save(file_path)
