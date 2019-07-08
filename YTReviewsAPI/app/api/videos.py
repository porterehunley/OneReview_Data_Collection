from app.api import bp
from app import db
from app.models import Video, Server_Controller, Admin, Description, Comment, Caption
from flask import jsonify
from flask import request
from app.api.errors import error_response
from app.api.auth import token_auth

import requests

@bp.route('/checkvideos/<videoid>', methods=['GET'])
@token_auth.login_required
def check_video(videoid):
	video = Video.query.filter_by(id=videoid)
	return_dict = {'status' : 'success'}
	if (video == None):
		return error_response(404, 'video not found')

	return(jsonify(return_dict))

@bp.route('/checkmedia/<title>', methods=['GET'])
@token_auth.login_required
def check_media(title):
	videos = Video.query.filter_by(mediaTitle=title).all()
	return_dict = {'status' : 'success'}
	if (not videos):
		return error_response(404, 'Videos with that title not found')

	return(jsonify(return_dict))


@bp.route('/videos/<title>', methods=['GET', 'DELETE', 'POST'])
@token_auth.login_required
def return_videos(title):
	if (request.method == 'GET'):
		returnAllVideos = title=='all'

		if (returnAllVideos):
			videos = Video.query.all()		
			return_dict = {'list':'resource'}
			l_video_dict = []

			for video in videos:
				l_video_dict.append(video.to_dict())

			return_dict['videos'] = l_video_dict


			return(jsonify(return_dict))


		videos = Video.query.filter_by(mediaTitle=title)
			
		return_dict = {'list':'resource'}
		l_video_dict = []

		for video in videos:
			l_video_dict.append(video.to_dict())

		return_dict['videos'] = l_video_dict

		if (len(l_video_dict) == 0):
			return error_response(404, title + ' not found')


		return(jsonify(return_dict))

	if (request.method == 'DELETE'):
		access_token = Admin.query.get(1).token
		videos = Video.query.filter_by(mediaTitle=title)

		if not videos:
			return error_response(404, 'Videos with that title not found')

		for video in videos:
			response = requests.delete('https://3.220.32.205/api/videoentry/'+video.id,
			 headers={'Authorization': 'Bearer '+access_token}, verify=False)

			if (response.status_code != 200):
				return error_response(response.status_code, "error getting videos")

	if (request.method == 'POST'):
		access_token = Admin.query.get(1).token
		videoIDs_JSON = requests.post('https://3.220.32.205/api/youtube_list/'+ title, headers={'Authorization': 'Bearer '+access_token}, verify=False)
		videoIDs_JSON = videoIDs_JSON.json()

		l_videoIDs = videoIDs_JSON['video_IDs']

		for video_id in l_videoIDs:

			#Get the comment threads
			response = requests.get('https://3.220.32.205/api/comment_threads/'+video_id, headers={'Authorization': 'Bearer '+access_token}, verify=False)
			if (response.status_code != requests.codes.ok):
				pass

			#Get the captions
			response = requests.get('https://3.220.32.205/api/video_caption/'+video_id, headers={'Authorization': 'Bearer '+access_token}, verify=False)
			if (response.status_code != requests.codes.ok):
				pass

	return(jsonify({"status": "success"}))


@bp.route('/videoentry/<videoid>', methods=['DELETE', 'POST'])
@token_auth.login_required
def edit_video_entry(videoid):
	return_dict= {'status' : 'success'}

	if (request.method == 'DELETE'):
		video = Video.query.filter_by(id=videoid).first()
		if (video is None):
			return(error_response(404, 'video not found'))

		description = Description.query.filter_by(video_id=videoid).first()
		if (description is not None):
			db.session.delete(description)

		comments = Comment.query.filter_by(video_id=videoid).all()
		if (comments is not None):
			for comment in comments:
				db.session.delete(comment)

		caption = Caption.query.filter_by(video_id=videoid).first()
		if (caption is not None):
			db.session.delete(caption)

		db.session.delete(video)
		db.session.commit()

	if (request.method == 'POST'):
		video = Video.query.filter_by(id=videoid).first()
		access_token = Admin.query.get(1).token

		if (video is not None):
			return(error_response(405, 'video is already in database'))

		#TODO


	return(jsonify(return_dict))
		









		




