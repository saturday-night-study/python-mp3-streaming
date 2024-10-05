from dataclasses import dataclass


@dataclass
class MP3Header:
    version: str
    layer: str
    protection: int
    bitrate: int
    sampling_rate: int
    padding: int
    private: int
    channel_mode: str
    mode_extension: str
    copy_right: int
    original: int
    emphasis: str

    def print(self):
        print(f"version: {self.version}")
        print(f"layer: {self.layer}")
        print(f"protection: {self.protection}")
        print(f"bitrate: {self.bitrate}")
        print(f"sampling_rate: {self.sampling_rate}")
        print(f"padding: {self.padding}")
        print(f"private: {self.private}")
        print(f"channel_mode: {self.channel_mode}")
        print(f"mode_extension: {self.mode_extension}")
        print(f"copy_right: {self.copy_right}")
        print(f"original: {self.original}")
        print(f"emphasis: {self.emphasis}")

    def calc_frame_size(self):
        return int((144 * int(self.bitrate) * 1000) / self.sampling_rate + self.padding)
