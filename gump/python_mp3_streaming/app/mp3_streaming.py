import os

import uvicorn
from fastapi import FastAPI
from fastapi.params import Query
from starlette.responses import StreamingResponse

from app.mp3.fileio import FileIO
from app.mp3.reader import MP3Reader

app = FastAPI()


@app.get("/play")
async def play(ts: int = Query(0, ge=0)) -> StreamingResponse:
    current_file_path = os.path.abspath(__file__)
    project_root = os.path.dirname(os.path.dirname(current_file_path))
    file_path = f"{project_root}/tests/test_data/original.mp3"
    fio = FileIO(file_path)
    reader = MP3Reader(fio)
    content_stream = reader.content_stream_from_duration(ts, True)

    return StreamingResponse(content_stream, media_type="audio/mpeg")


if __name__ == "__main__":
    uvicorn.run("app.mp3_streaming:app", host="127.0.0.1", port=7070, reload=True)
