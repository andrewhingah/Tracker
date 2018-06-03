import unittest
from flask import Flask, jsonify, request
from model.user_request import user_requests


class UserRequestsTestCase(unittest.TestCase):

    def setUp(self):
        self.userRequest = {'user1': ['phone1','broken screen']}
        print ('start of test')

    def test_get_all_maintenance_reqs(self):

        response = jsonify (user_requests)
        self.assertEqual(response.status_code, 200)
        self.assertIn('windows updates and virus protection', str(response.data))


if __name__ == "__main__":
    unittest.main()