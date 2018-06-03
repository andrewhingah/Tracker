import unittest
from flask import Flask, jsonify, request
from model.user_request import user_requests


class UserRequestsTestCase(unittest.TestCase):

    def setUp(self):
        self.userRequest = {'user1': ['phone1','broken screen']}
        print ('start of test')

    #test a user can get all their requests

    def test_get_all_maintenance_reqs(self):

        response = jsonify (user_requests)
        self.assertEqual(response.status_code, 200)
        self.assertIn('broken screen', str(response.data))

    #test a user can add a request

    def test_add_user_req(self):
        response = UserRequestSchema().load(request.get_json())
        user_requests.append(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('windows updates and virus protection', str(response.data))


if __name__ == "__main__":
    unittest.main()