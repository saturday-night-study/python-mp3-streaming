### MP3 Streaming

```bash
source .venv/bin/activate

pip install fastapi
pip install httpx
pip install uvicorn

uvicorn app.mp3_streaming:app --reload --port 7070
```

### Test coverage
```bash
source .venv/bin/activate

pip install coverage

coverage run -m unittest discover
coverage report -m
```