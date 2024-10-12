import unittest

from fastapi.testclient import TestClient
from app import app

class TestMp3Stream(unittest.TestCase):
    def test_mp3_stream(self):
        client = TestClient(app)
        response = client.get("/stream-mp3")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers["Content-Type"], "audio/mpeg")

if __name__ == '__main__':
    unittest.main()
