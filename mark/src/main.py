from mp3 import MP3
from mp3_file_reader import MP3FileReader

reader = MP3FileReader("../resource/input.mp3")
reader.open()
reader.read_all()

mp3 = MP3(reader)
mp3.set_header()
mp3.set_frame_size()
mp3.set_frame_count()
mp3.set_play_time()

print(mp3.header)
print(mp3.frame_size)
print(mp3.frame_count)
print(mp3.play_time)