from flask import Flask
from flask_restful import Api
from app.user_request import Request, RequestsList

app = Flask(__name__)
api = Api(app)

##Api resource routing here
api.add_resource(RequestsList, '/requests')
api.add_resource(Request, '/requests/<request_id>')


if __name__ == '__main__':
    app.run(debug=True)