from enum import Enum
from dataclasses import dataclass
from bitstring import ConstBitStream

@dataclass
class MP3File:
    frameSync:any = None

class FileState(Enum):
    NONE = 0
    NOT_READ = 1
    READED = 2
    CLOSED = 3

class MP3FileReader:
    def __init__(self, filePath):
        self.fileBitStream = ConstBitStream(filename=filePath)
        self.state = FileState.NOT_READ
        self.mp3File = MP3File()

    def read(self):
        frameSync = self.fileBitStream.read(11)

        if frameSync.uint == 2047:
            self.mp3File.frameSync = frameSync
            return True
        
        return False

