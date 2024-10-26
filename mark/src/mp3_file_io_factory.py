from mp3_file_io import MP3FileIo


class MP3FileIoFactory:
    @staticmethod
    def create_with_file(file_path: str) -> MP3FileIo:
        io = MP3FileIo()
        io.open(file_path)
        return io

    @staticmethod
    def create_with_bytes(file_bytes: bytes) -> MP3FileIo:
        io = MP3FileIo()
        io.file_bytes = file_bytes
        return io
