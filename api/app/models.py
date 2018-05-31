class Requests():

	#initialize an empty list
	user_req = []
	
	def __init__(self, req_id, category, description):
		self.req_id = req_id
		self.category = category
		self.description = description

	def create_req (self, user_id, req_id, category, description):
		update = {user_id: [req_id, category, description]}
		user_req.append (update)


#returns all user requests as a list
	def get_all_reqs (self, user_id, req_id, category, description):
		for user in user_req:
			return user