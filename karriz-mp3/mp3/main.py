from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from mp3.reader import MP3FileReader
from mp3.trimmer import MP3FileTrimmer
from mp3.streamer import MP3Streamer

app = FastAPI()

@app.get("/")
async def root():
    return {"code": 200, "message": "success", "data": None}

@app.get("/mp3/play")
async def play(filename: str, offset: int = -1, size: int = -1):
    reader = MP3FileReader(f"assets/{filename}")

    mp3_file = reader.read()

    if offset < 0 and size < 0:
        mp3_streamer = MP3Streamer(mp3_file)
        return StreamingResponse(mp3_streamer.streaming(), media_type="audio/mpeg")
    
    mp3_file_trimmer = MP3FileTrimmer(mp3_file)
    trimmed_mp3 = mp3_file_trimmer.trim(offset, size, f"assets/trimmed_{filename}")

    print(trimmed_mp3)
    
    mp3_streamer = MP3Streamer(trimmed_mp3)

    return StreamingResponse(mp3_streamer.streaming(), media_type="audio/mpeg")