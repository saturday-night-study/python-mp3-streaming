from python_mp3_streaming.file_io import FileIO
from python_mp3_streaming.mp3_reader import MP3Reader

input_file = FileIO("../tests/test_data/input.mp3")
reader = MP3Reader(input_file)
input_data = reader.read_bytes_from_duration(30)
input_file.close()

output_file = FileIO("../tests/test_data/output.mp3", "wb+")
output_file.write(input_data)
output_file.close()
