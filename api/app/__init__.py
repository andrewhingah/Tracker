from flask import Flask
from flask_api import FlaskAPI

from flask import request, jsonfy, abort

# local import
from instance.config import app_config

def create_app(config_name):
	from api.models import Requests
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    
    return app

@app.route('/userRequests/', methods = ['POST', 'GET'])
def userRequests ():
	if request.method == 'POST': #POST
		name = str(request.data.get('name', ''))
		if name:
                userRequest = UserRequest(name=name)
                userRequest.save()
                response = jsonify({
                    'name': userRequest[key],
                    'details': UserRequest['name']
                })
                response.status_code = 201
                return response
        else:
            # GET
            userRequests = models.user_req

            for userRequest in userRequests:
                obj = {
                    'name': userRequest[key],
                    'details': userRequest['name']
                }
                userRequest.append(obj)
            response = jsonify(userRequest)
            response.status_code = 200
            return response

    return app