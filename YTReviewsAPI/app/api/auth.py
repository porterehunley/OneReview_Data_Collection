from flask import g
from flask_httpauth import HTTPBasicAuth
from app.models import Admin
from app.api.errors import error_response
from flask_httpauth import HTTPTokenAuth

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()

@basic_auth.verify_password
def verify_password(username, password):
    admin = Admin.query.filter_by(username=username).first()
    if admin is None:
        return False
    g.current_user = admin
    return admin.check_password(password)

@basic_auth.error_handler
def basic_auth_error():
    return error_response(401)

@token_auth.verify_token
def verify_token(token):
	g.current_user = Admin.check_token(token) if token else None
	return g.current_user is not None

@token_auth.error_handler
def token_auth_error():
	return error_response(401)
