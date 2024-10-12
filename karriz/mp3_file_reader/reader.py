import os

from . import enum, const 

from .model import MP3, MP3FrameHeader
from .error import EmptySizeFileError, InvalidFrameSyncError, InValidFrameHeaderSizeError, VersionNotMatchedError

class MP3FileReader:
    def __init__(self, file_path:str):
        file_size = os.path.getsize(file_path)

        if file_size == 0:
            raise EmptySizeFileError

        self.__file_path = file_path

    def read(self) -> MP3:
        mp3 = MP3()

        mp3_file = open(self.__file_path, 'rb')

        total_duration = 0.0
        while True:
            try:
                frame_header_parser = MP3FrameHeaderParser(mp3_file.read(4))

                total_duration += frame_header_parser.get_frame_duration()
                mp3_file.seek(frame_header_parser.get_frame_size()-4, 1)

            except InValidFrameHeaderSizeError:
                break

        mp3_file.close()

        mp3.total_duration = int(total_duration)
        
        return mp3

    def get_mp3_file(self):
        return self.__mp3_file

class MP3FrameHeaderParser:
    def __init__(self, data:bytes):
        if len(data) != 4:  
            raise InValidFrameHeaderSizeError

        header_bits = int.from_bytes(data, byteorder='big')
        
        syncword = (header_bits >> 21) & const.SYNC_WORD_MASK
        if syncword != const.SYNC_WORD_MASK:
            raise InvalidFrameSyncError

        # parse & masking all attributes
        version = (header_bits >> 19) & const.VERSION_MASK
        layer = (header_bits >> 17) & const.LAYER_MASK
        protection = (header_bits >> 16) & const.PROTECTION_MASK
        bitrate = (header_bits >> 12) & const.BITRATE_MASK
        sampling_rate_freq = (header_bits >> 10) & const.SAMPLING_RATE_MASK
        padding = (header_bits >> 9) & const.PADDING_MASK
        private = (header_bits >> 8) & const.PRIVATE_MASK
        channel_mode = (header_bits >> 6) & const.CHANNEL_MODE_MASK
        mode_extension = (header_bits >> 4) & const.MODE_EXTENSION_MASK
        copyright = (header_bits >> 3) & const.COPYRIGHT_MASK
        original = (header_bits >> 2) & const.ORIGINAL_MASK
        emphasis = (header_bits >> 0) & const.EMPHASIS_MASK

        # instantiate mp3_frame_header dataclass
        mp3_frame_header = MP3FrameHeader()
        
        # version
        mp3_frame_header.version = enum.MP3Version(version)

        # layer
        mp3_frame_header.layer = enum.MP3Layer(layer)

        # protection bit
        mp3_frame_header.protection = enum.MP3Protection(protection)

        # bitrate
        mp3_frame_header.bitrate = const.BITRATE_TABLE[version][layer][bitrate] * 1000 # kbps -> bps로 변환

        # sampling rate frequency
        mp3_frame_header.sampling_rate_freq = const.SAMPLE_RATE_TABLE[version][sampling_rate_freq]

        # padding
        mp3_frame_header.padding = enum.MP3PaddingBit(padding)

        # private 
        mp3_frame_header.private = private

        # channel mode
        mp3_frame_header.channel_mode = enum.MP3ChannelMode(channel_mode)

        # mode extension
        mp3_frame_header.mode_extension = mode_extension

        # copyright
        mp3_frame_header.copyright = enum.MP3Copyright(copyright)

        # original
        mp3_frame_header.original = enum.MP3Original(original)

        #emphasis 
        mp3_frame_header.emphasis = enum.MP3Emphasis(emphasis)

        self.__mp3_frame_header = mp3_frame_header

    def get_frame_size(self) -> int:
        return (144 * self.__mp3_frame_header.bitrate) // self.__mp3_frame_header.sampling_rate_freq + self.__mp3_frame_header.padding.value
        
    def get_frame_duration(self) -> float:
        return 1152 / self.__mp3_frame_header.sampling_rate_freq