import unittest

from fastapi.testclient import TestClient
from app import app

class TestHealthCheckApi(unittest.TestCase):
    def test_health_check(self):
        client = TestClient(app)
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}

if __name__ == '__main__':
    unittest.main()
