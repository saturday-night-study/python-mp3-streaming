from mp3_file_io_factory import MP3FileIoFactory
from mp3_frame import MP3Frame


class MP3:
    def __init__(self):
        self._frames = list[MP3Frame]
        self._frame_count = 0
        self._play_time = 0

    def set_frames(self, frames):
        self._frames = frames
        self._frame_count = len(frames)
        self._frame_count = len(frames)
        self._play_time = self._frame_count * 1152 / self._frames[0].header.sampling_rate

    def get_frame_count(self):
        return self._frame_count

    def get_play_time(self):
        return self._play_time


    def save(self, file_path):
        new_bytes = self.to_bytes()
        MP3FileIoFactory.create_with_bytes(new_bytes).save(file_path)

    def to_bytes(self) -> bytes:
        new_bytes = b''

        for frame in self._frames:
            new_bytes += frame.to_bytes()

        return new_bytes
