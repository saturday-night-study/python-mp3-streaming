import mp3_header_factory


class MP3:
    def __init__(self, file_reader):
        self.frame_size = 0
        self.frame_count = 0
        self.header = None
        self.file_reader = file_reader

    def set_header(self):
        header_bytes = self.file_reader.get(4)
        self.header = mp3_header_factory.MP3HeaderFactory.create(header_bytes)

    def get_header(self):
        return self.header

    def set_frame_size(self):
        self.frame_size = self.header.calc_frame_size()

    def get_frame_size(self):
        return self.frame_size

    def set_frame_count(self):
        offset = 4 # 태그 없어서 고정 offset 사용
        self.frame_count = (self.file_reader.get_size() - offset) // self.frame_size

    def get_frame_count(self):
        return self.set_frame_count

