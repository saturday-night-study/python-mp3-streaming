import io
import os

from Tools.scripts.pep384_macrocheck import parse_file
from fastapi import FastAPI
from mp3_file_io import MP3FileIo
from fastapi.responses import StreamingResponse
from fastapi.responses import Response
app = FastAPI()

#     python -m uvicorn src.app:app --reload

@app.get("/health")
async def health_check():
    return {"status": "ok"}


@app.get("/stream-mp3/{file_name:path}")
async def stream_mp3(file_name: str):
    print(f"Current working directory: {os.getcwd()}")

    path = f"../resource/{file_name}"
    mp3_io = MP3FileIo()

    if not mp3_io.file_exists(path):
        return Response(status_code=404, content="파일을 찾을 수 없습니다")
    try:
        mp3_io.open(path)
        mp3_io.read_all()
    except Exception as e:
        return Response(status_code=500, content="알 수 없는 오류가 발생했습니다")
    finally:
        mp3_io.close()

# 추후 MP3 클래스를 사용하여 MP3 파일을 일부만 읽어오는 방법을 구현할 수 있습니다.
    # mp3 = MP3(mp3_io)
    # mp3.set_header()
    # mp3.set_frame_size()
    # mp3.set_frame_count()
    # mp3.set_play_time()

    headers = {
        "Content-Disposition": f"inline; filename={os.path.basename(path)}",
        "Content-Type": "audio/mpeg",
        "Content-Length": str(mp3_io.get_size())
    }

    return StreamingResponse(io.BytesIO(mp3_io.get_all()), headers=headers)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)