class FileStreamNotLoadedError(Exception):
    def __init__(self):
        super().__init__('MP3 파일이 로드 되지않았습니다.')

class EmptySizeFileError(Exception):
    def __init__(self):
        super().__init__('빈 파일은 사용할 수 없습니다.')

class InValidFrameHeaderSizeError(ValueError):
    def __init__(self):
        super().__init__('프레임 헤더의 크기가 올바르지 않습니다.')

class InvalidFrameSyncError(Exception):
    def __init__(self):
        super().__init__('유효하지 않은 FrameSync 값 입니다.')

class VersionNotMatchedError(Exception):
    def __init__(self):
        super().__init__('MP3와 맞지 않는 버전 값 입니다.')   

class LayerNotMatchedError(Exception):
    def __init__(self):
        super().__init__('MP3와 맞지 않는 레이어 값 입니다.')     

class BadBitrateError(Exception):
    def __init__(self):
        super().__init__('잘못 된 Bitrate 값 입니다.')     

class InvalidFrequencyError(Exception):
    def __init__(self):
        super().__init__('잘못 된 Frequency 값 입니다.')     