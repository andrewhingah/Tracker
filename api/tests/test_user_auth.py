"""user authentication test cases"""

import json
import unittest
from app import UserRequest


class TestUserAuth(unittest.TestCase):
    """handles Auth Endpoint test"""

    def setUp(self):
        UserRequest.testing = True
        self.app = UserRequest.test_client()
        self.data = {
            "username": "Andrew",
            "password": "password"
        }

    def test_user_registration(self):
        """Test for successful user registration"""
        response = self.app.post('/api/auth/register',
                                 data=json.dumps(self.data),
                                 content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["status"], "ok")
        self.assertEqual(result["username"], "Andrew")
        self.assertEqual(response.status_code, 201)


if __name__ == "__main__":
    unittest.main()