import io
import os

from fastapi import FastAPI
from mp3 import MP3
from mp3_file_io import MP3FileIo
from fastapi.responses import StreamingResponse

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "ok"}

@app.get("/stream-mp3")
async def stream_mp3():
    path = "../resource/input.mp3"
    mp3_io = MP3FileIo()
    mp3_io.open(path)
    mp3_io.read_all()
    mp3_io.close()

    mp3 = MP3(mp3_io)
    mp3.set_header()
    mp3.set_frame_size()
    mp3.set_frame_count()
    mp3.set_play_time()

    headers = {
        "Content-Disposition": f"inline; filename={os.path.basename(path)}",
        "Content-Type": "audio/mpeg",
        "Content-Length": str(mp3_io.get_size())
    }

    return StreamingResponse(io.BytesIO(mp3_io.get_all()), headers=headers)