import unittest
import os
import json
from app import create_app

class User_req_testcase (unittest.TestCase):
    """This class represents the user requests test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        self.userRequest = {'Andrew': ['phone1','repair','broken screen']}


    def test_request_creation(self):
        """Test API can create a request (POST request)"""
        res = self.client().post('/userRequests/', data=self.userRequest)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Andrew', str(res.data))

    def test_api_can_get_all_requests(self):
        """Test API can get a request (GET request)."""
        res = self.client().post('/userRequests/', data=self.userRequest)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/userRequests/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Andrew', str(res.data))

    def test__edit_request(self):
        """Test API can edit an existing requests. (PUT request)"""
        rv = self.client().post(
            '/userRequests/',
            data={'Andrew': ['TV03', 'repair', 'black screen']})
        self.assertEqual(rv.status_code, 201)
        rv = self.client().put(
            '/userRequests/1',
            data={
                "Andrew": ['BENZ43', 'maintenance', 'flat tires']
            })
        self.assertEqual(rv.status_code, 200)
        results = self.client().get('/userRequests/1')
        self.assertIn('flat tires', str(results.data))

    def test_bucketlist_deletion(self):
        """Test API can delete an existing request. (DELETE request)."""
        rv = self.client().post(
            '/userRequests/',
            data={'Andrew': ['TV03', 'repair', 'black screen']})
        self.assertEqual(rv.status_code, 201)
        res = self.client().delete('/userRequests/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/userRequests/1')
        self.assertEqual(result.status_code, 404)

    def tearDown(self):

# Make the tests executable
    if __name__ == "__main__":
        unittest.main()