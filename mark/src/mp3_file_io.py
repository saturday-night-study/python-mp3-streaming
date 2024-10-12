import os.path

import mp3_header_factory

class MP3FileIo:
    def __init__(self):
        self.file_obj = None
        self.bytes = None

    def file_exists(self):
        return os.path.exists(self.file_path)

    def open(self, file_path):
        try:
            self.file_obj = open(file_path, 'rb')
        except IOError as e:
            print(f"파일을 열 수 없습니다: {e}")
            return

    def close(self):
        if self.file_obj is not None:
            self.file_obj.close()

    def read_all(self):
        self.bytes = self.file_obj.read()

    def get(self, size):
        return self.bytes[0:size]

    def get_all(self):
        return self.bytes

    def get_size(self):
        return len(self.bytes)

    def check_header(self):
        try:
            file_obj = open(self.file_path, 'rb')
            header = file_obj.read(2)
            file_obj.close()

            # Convert the header to an integer
            header_int = int.from_bytes(header, byteorder='big')

            # MP3 Sync Word가(=11비트) 1로 시작하는지 확인한다.
            # 0xFF = 1111 1111
            # 0xE0 = 1110 0000
            if (header_int & 0xFFE0) != 0xFFE0:
                print("MP3 SYNC WORD not detected")
                return False
            return True
        except IOError as e:
            if isinstance(e, EOFError):
                print(f"파일이 너무 작습니다: {e}")
            else:
                print(f"파일을 열 수 없습니다: {e}")

            return False

    def cut_frames(self, start_byte, end_byte):
        io = MP3FileIo()
        io.bytes = self.bytes[0:4] + self.bytes[start_byte:end_byte]
        return io

    def save(self, file_path):
        try:
            file_obj = open(file_path, 'wb')
            file_obj.write(self.bytes)
            file_obj.close()
        except IOError as e:
            print(f"파일을 저장할 수 없습니다: {e}")
            return
