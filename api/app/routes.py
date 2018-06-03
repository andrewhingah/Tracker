
from flask import Blueprint, request
from api.app.helper import response, response_auth


auth = Blueprint('auth', __name__)


class RegisterUser:
    """
    View function to register a user via the api
    """

    def post(self):
        """
        Register a user, generate their token and add them to a data structure
        :return: Json Response with the user`s token
        """
        response = self.app.post('/api/auth/register',
                                 data=json.dumps(self.data),
                                 content_type="application/json")
        result = json.loads(response.data)
        
        return response_auth('Congratulations', 'Registration successful', token, 201)
        
class LoginUser(MethodView):
    def post(self):
        """
        Login a user if the supplied credentials are correct.
        :return: Http Json response
        """
        request.content_type == 'application/json'

        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')

        if email in 'email' and password in 'password':
            return response_auth('success', 'Successfully logged In', user.encode_auth_token(user.id), 200)
        else:
            return response('failed', 'User does not exist or password is incorrect', 401)



# Register classes as views
registration_view = RegisterUser.as_view('register')
login_view = LoginUser.as_view('login')

# Add rules for the api Endpoints
auth.add_url_rule('/auth/register', view_func=registration_view, methods=['POST'])
auth.add_url_rule('/auth/login', view_func=login_view, methods=['POST'])
