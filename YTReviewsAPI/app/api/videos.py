from app.api import bp
from app import db
from app.models import Video
from flask import jsonify

@bp.route('/getvideos/<title>', methods=['GET'])
def return_videos(title):
	returnAllVideos = title == 'all'

	if (returnAllVideos):
		videos = Video.query.all()		
		return_dict = {'list':'resource'}
		l_video_dict = []

		for video in videos:
			l_video_dict.append(video.to_dict())

		return_dict['videos'] = l_video_dict

		print(return_dict)
		return(jsonify(return_dict))

		




