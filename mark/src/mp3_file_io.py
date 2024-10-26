import os.path

class MP3FileIo:
    def __init__(self):
        self.file_obj = None
        self.file_bytes = None

    def file_exists(self, path):
        return os.path.exists(path)

    def open(self, file_path) -> bool:
        try:
            self.file_obj = open(file_path, 'rb')
        except IOError as e:
            print(f"파일을 열 수 없습니다: {e}")
            return False
        return True

    def close(self):
        if self.file_obj is not None:
            self.file_obj.close()

    def read(self, size):
        return self.file_obj.read(size)

    def get(self, size):
        return self.file_bytes[0:size]

    def get_bytes(self, start, end):
        return self.file_bytes[start:end]

    def get_all(self):
        return self.file_bytes

    def get_size(self):
        return len(self.file_bytes)

    def save(self, file_path):
        try:
            file_obj = open(file_path, 'wb')
            file_obj.write(self.file_bytes)
            file_obj.close()
        except IOError as e:
            print(f"파일을 저장할 수 없습니다: {e}")
            return
