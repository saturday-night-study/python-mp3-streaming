from mp3_file_reader import MP3FileReader

opener = MP3FileReader("../resource/input.mp3")

if not opener.file_exists():
    print("This file does not exist.")
    exit(-1)

if not opener.open_with_check_file_header():
    print("This file is not mp3 file.")
    exit(-1)

header = opener.open_with_parse_header()
header.print()