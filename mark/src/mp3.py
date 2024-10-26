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

    def get_frame(self, index) -> bytes:
        offset = 4
        start = offset + index * self.frame_size
        end = start + self.frame_size
        frame = self.file_io.get_bytes(start, end)
        return frame

    def cut(self, start_time, end_time):
        start_frame = int(start_time * self.header.sampling_rate / 1152)
        end_frame = int(end_time * self.header.sampling_rate / 1152)

        frame_size = self.header.calc_frame_size()
        start_byte = start_frame * frame_size
        end_byte = end_frame * frame_size

        io = self.file_io.cut_frames(start_byte, end_byte)
        return MP3(io)

    def change_speed_down(self, speed: int):
        if speed <= 0:
            raise ValueError("Speed must be greater than 0")

        # 일단 전체 프레임을 배열로 저장한다
        frames = []
        for i in range(self.frame_count):
            frames.append(self.get_frame(i))

        new_frames = bytearray()
        for i in range(self.frame_count):
            for _ in range(speed):
                new_frames.extend(frames[i])

        io = self.file_io.change_frames(new_frames)
        return MP3(io)

    def change_speed_up(self, speed: int):
        if speed <= 0:
            raise ValueError("Speed must be greater than 0")

        # 일단 전체 프레임을 배열로 저장한다
        frames = []
        for i in range(self.frame_count):
            frames.append(self.get_frame(i))

        new_frames = bytearray()

        i = 0
        while i < self.frame_count:
            new_frames.extend(frames[i])
            i += speed

        io = self.file_io.change_frames(new_frames)
        return MP3(io)

    def save(self, file_path):
        self.file_io.save(file_path)

