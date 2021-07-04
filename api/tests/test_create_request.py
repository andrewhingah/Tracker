import unittest
from app import UserRequest

class RequestsTestCase (unittest.TestCase):
	def setUp(self):
        self.request=UserRequest("B01","broken screen")

    def tearDown(self):
        UserRequest.request_list=[]

    def test_initialize_request(self):
        self.assertEqual(self.request.request_id,"B01")
        self.assertEqual(self.request.description,"broken screen")

    def test_request_creation(self):
		self.assertEqual(res.status_code, 201)

    def test_save_request(self):
        self.request.save_request()
        self.assertEqual(len(UserRequest.request_list),1)

    def test_multiple_requests(self):
        self.request.save_request()
        self.test_request=UserRequest("B02","battery replacement")
        self.test_request.save_request()
        self.assertEqual(len(UserRequest.request_list),2)

    def test_delete_request(self):
        self.request.save_request()
        self.test_request=UserRequest("B02","battery replacement")
        self.test_request.save_request()
        self.test_request.deleteRequest()
        self.assertEqual(len(UserRequest.request_list),1)  

    def test_show_request(self):
        self.assertEqual(UserRequest.displayRequest(),UserRequest.request_list) 

		pass

if __name__ == "__main__":
	unittest.main()

