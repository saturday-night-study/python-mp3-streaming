import unittest
from http import HTTPStatus

from fastapi import FastAPI
from fastapi.testclient import TestClient


class TestMP3Reader(unittest.TestCase):
    def setUp(self):
        self.__client = TestClient(FastAPI())
        self.__base_url = "http://localhost:7070"
        self.__original_file_size = 9375481

    def test_http_get_play(self):
        response = self.__client.get(f"{self.__base_url}/play")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.headers["Content-Type"], "audio/mpeg")
        self.assertEqual(int(response.headers["Content-Length"]), self.__original_file_size)


if __name__ == '__main__':
    unittest.main()
