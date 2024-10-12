import os
from typing import AsyncIterable

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
    data = reader.read_bytes_from_duration(ts)
    fio.close()

    return StreamingResponse(__data_to_generator(data), media_type="audio/mpeg")


async def __data_to_generator(data: bytes, chunk_size: int = 4096) -> AsyncIterable[bytes]:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


if __name__ == "__main__":
    uvicorn.run("app.mp3_streaming:app", host="127.0.0.1", port=7070, reload=True)
