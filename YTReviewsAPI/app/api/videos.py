from app.api import bp
from app import db
from app.models import Video, Server_Controller, Admin
from flask import jsonify
from flask import request
from app.api.errors import error_response

@bp.route('/getvideos/<title>', methods=['GET'])
def return_videos(title):
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









		




