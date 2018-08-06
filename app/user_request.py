from flask_restful import Resource, abort, reqparse

user_requests = {
    'request1': {'title': 'Office furniture', 'description':'Cleaning, Repair, Painting'},
    'request2': {'title': 'Air Conditioners', 'description':'Repair and replacement'},
    'request3': {'title': 'Washrooms', 'description':'Repair and replacement of toilet bowls'},
}


def abort_if_request_doesnt_exist(request_id):
    if request_id not in user_requests:
        abort(404, message="{} doesn't exist".format(request_id))

parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('description')


# shows a single request, lets you add a request and delete a single request
class Request(Resource):
    def get(self, request_id):
        abort_if_request_doesnt_exist(request_id)
        return user_requests[request_id]

    def delete(self, request_id):
        abort_if_request_doesnt_exist(request_id)
        del user_requests[request_id]
        return '', 204

    def put(self, request_id):
        args = parser.parse_args()
        task = {'title': args['title'],'description': args['description']}
        
        user_requests[request_id] = task
        return task, 201


# shows a list of all user requests, and lets you POST to add new request
class RequestsList(Resource):
    def get(self):
        return user_requests

    def post(self):
        args = parser.parse_args()
        request_id = int(max(user_requests.keys()).lstrip('request')) + 1
        request_id = 'request%i' % request_id
        user_requests[request_id] = {'title': args['title'],'description': args['description']}
        return user_requests[request_id], 201
