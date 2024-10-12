import unittest

from fastapi.testclient import TestClient
from app import app

class TestMp3Stream(unittest.TestCase):

    def test_mp3_stream(self):
        client = TestClient(app)
        response = client.get("/stream-mp3/input.mp3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "audio/mpeg")

    def test_mp3_stream_fail(self):
        client = TestClient(app)
        response = client.get("/stream-mp3/not_found.mp3")
        self.assertEqual(response.status_code, 404)

    # 500 에러는 어떤 경우에 나올 수 있을까?

if __name__ == '__main__':
    unittest.main()
