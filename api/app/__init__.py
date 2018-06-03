from flask import Flask, jsonify, request


from model.user_request import user_requests, UserRequest, UserRequestSchema

app = Flask(__name__)


@app.route('/maintenances')
def get_maintenances_reqs():
    schema = UserRequestSchema(many=True)
    
    response = jsonify (user_requests)
    response.status_code = 200

    return response


@app.route('/maintenances', methods=['POST'])
def add_maintenance_req():
    maintenance = UserRequestSchema().load(request.get_json())
    
    user_requests.append(maintenance.data)
    return "", 204