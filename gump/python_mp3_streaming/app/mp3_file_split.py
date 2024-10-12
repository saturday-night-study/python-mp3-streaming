from mp3.fileio import FileIO
from mp3.reader import MP3Reader

input_file = FileIO("../tests/test_data/original.mp3")
reader = MP3Reader(input_file)
input_data = reader.read_bytes_from_duration(30)
input_file.close()

output_file = FileIO("../tests/test_data/output.mp3", "wb+")
output_file.write(input_data)
output_file.close()
