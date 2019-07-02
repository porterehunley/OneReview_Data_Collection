from app.api import bp
from app import db
from app.models import Video, Server_Controller, Admin
from flask import jsonify
from flask import request
from app.api.errors import error_response
from flask_login import current_user, login_user

import requests


@bp.route('/serverstatus', methods=['GET'])
def return_server_status():
	server_controller = Server_Controller.query.get(1)

	if (server_controller == None):
		return error_response(404, 'no collection running')

	return_dict = {'CurrentMovie' : server_controller.CURRENT_MOVIE }
	return_dict['isRunning'] = server_controller.is_running

	if (server_controller.CURRENT_MOVIE // 50  == 0):
		return_dict['currentYear'] = 2014
	if (server_controller.CURRENT_MOVIE // 50  == 1):
		return_dict['currentYear'] = 2015
	if (server_controller.CURRENT_MOVIE // 50  == 2):
		return_dict['currentYear'] = 2016
	if (server_controller.CURRENT_MOVIE // 50  == 3):
		return_dict['currentYear'] = 2017
	if (server_controller.CURRENT_MOVIE // 50  == 4):
		return_dict['currentYear'] = 2018

	return(jsonify(return_dict))


@bp.route('/authentication', methods=['POST'])
def check_auth():
	data = request.get_json() or {}
	presumed_admin = Admin.query.filter_by(username=data['username']).first()
	return_dict= {'loginStatus' : True}

	if (presumed_admin == None):
		return_dict['loginStatus'] = False
		return(error_response(401, 'username or password incorrect'))

	if (presumed_admin.check_password(data['password']) != True):
		return_dict['loginStatus'] = False
		return(error_response(401, 'username or password incorrect'))


	login_user(presumed_admin)
	return(jsonify(return_dict))

@bp.route('/controlauthentication', methods=['POST'])
def check_control_auth():
	data = request.get_json() or {}
	return_dict= {'status' : 'success'}


	if current_user.is_authenticated:
		requests.get('http://127.0.0.1:5000/api/startservercontroller/'+ data['maxVideos'],
		  headers={'Authorization': 'Bearer '+ current_user.token})
		return(jsonify(return_dict))


	return(error_response(401, 'not logged in'))

