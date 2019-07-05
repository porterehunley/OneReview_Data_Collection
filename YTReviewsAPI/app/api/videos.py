from app.api import bp
from app import db
from app.models import Video, Server_Controller, Admin
from flask import jsonify
from flask import request
from app.api.errors import error_response
from app.api.auth import token_auth

@bp.route('/videos/<title>', methods=['GET', 'DELETE'])
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

		access_token = Admin.query.get(1).first().token
		videos = Video.query.filter_by(mediaTitle=title)

		if not videos:
			return error_response(404, 'Videos with that title not found')

		for video in videos:
			response = requests.get('http://127.0.0.1:5000/api/videoentry/'+video.id,
			 headers={'Authorization': 'Bearer '+access_token})

			if (response.status != 200):
				return error_response(response.status, "error getting videos")

	return(jsonify({"status": "success"}))


@bp.route('/videoentry/<videoid>', methods=['DELETE', 'POST'])
@token_auth.login_required
def edit_video_entry(videoid):
	return_dict= {'status' : 'success'}

	if (request.method == 'DELETE'):
		video = Video.query.filter_by(id=videoid)
		if (video is None):
			return(error_response(404, 'video not found'))

		description = Description.query.filter_by(video_id=videoid)
		if (description is not None):
			db.session.delete(description)

		comments = Comment.query.filter_by(video_id=videoid)
		if (comments is not None):
			for comment in comments:
				db.session.delete(comment)

		caption = Caption.query.filter_by(video_id=videoid)
		if (caption is not None):
			db.session.delete(caption)

		db.session.delete(video)
		db.session.commit()

	if (request.method == 'POST'):
		pass

	return(jsonify(return_dict))
		









		




