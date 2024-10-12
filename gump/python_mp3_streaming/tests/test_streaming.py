import unittest
from http import HTTPStatus

from fastapi.testclient import TestClient

from app.mp3_streaming import app


class TestMP3Reader(unittest.TestCase):
    def setUp(self):
        self.__client = TestClient(app)
        self.__base_url = "http://localhost:7070"

    def test_http_get_play(self):
        response = self.__client.get(f"{self.__base_url}/play")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.headers["Content-Type"], "audio/mpeg")

    def test_http_get_play_invalid_ts(self):
        response = self.__client.get(f"{self.__base_url}/play?ts=-1")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

        response = self.__client.get(f"{self.__base_url}/play?ts=test")
        self.assertNotEqual(response.status_code, HTTPStatus.OK)

    # TODO: 오디오 스트리밍 기능 같은건 테스트를 어떻게 하지?

if __name__ == '__main__':
    unittest.main()
