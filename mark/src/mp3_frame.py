from dataclasses import dataclass

from mp3_header import MP3Header


@dataclass
class MP3Frame:
    def __init__(self, header:MP3Header, header_bytes, data_bytes:bytes):
        self.header = header
        self.header_bytes = header_bytes
        self.data_bytes = data_bytes

    def to_bytes(self):
        return self.header_bytes + self.data_bytes
