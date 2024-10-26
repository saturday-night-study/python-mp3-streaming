from mp3 import MP3
from mp3_file_io import MP3FileIo
from mp3_frame_factory import Mp3FrameFactory


class MP3Factory:
    @staticmethod
    def create_by_file_path(file_path: str) -> MP3:
        io = MP3FileIo()
        io.open(file_path)
        frames = Mp3FrameFactory.create(io)
        io.close()

        return MP3Factory.create_by_frames(frames)

    @staticmethod
    def create_by_frames(frames) -> MP3:
        mp3 = MP3()
        mp3.set_frames(frames)
        return mp3

    @staticmethod
    def create_by_cut(mp3:MP3, start_time:int, end_time:int):
        # 첫번째 헤더를 기준으로 시작 프레임과 끝 프레임을 계산한다 (CBR만 가능)
        first_header = mp3._frames[0].header

        start_frame = int(start_time * first_header.sampling_rate / 1152)
        end_frame = int(end_time * first_header.sampling_rate / 1152)

        new_frames = mp3._frames[start_frame:end_frame]
        return MP3Factory.create_by_frames(new_frames)

    @staticmethod
    def create_speed_down(mp3:MP3, speed: int):
        if speed <= 0:
            raise ValueError("Speed must be greater than 0")

        new_frames = []
        for i in range(mp3._frame_count):
            for _ in range(speed):
                new_frames.append(mp3._frames[i])

        return MP3Factory.create_by_frames(new_frames)

    @staticmethod
    def create_speed_up(mp3:MP3, speed: int):
        if speed <= 0:
            raise ValueError("Speed must be greater than 0")

        new_frames = []
        for i in range(mp3._frame_count):
            if i % speed == 0:
                frame = mp3._frames[i]
                new_frames.append(frame)

        return MP3Factory.create_by_frames(new_frames)
