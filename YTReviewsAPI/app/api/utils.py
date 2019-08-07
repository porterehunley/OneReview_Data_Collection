from app import db
from app.YouTubeAPICalls import search_videos_list, get_video_stats, get_comment_threads
from app.models import Video, Description, Comment, Caption, Server_Controller, Admin
import pickle


def get_movie_titles(year, EARLIEST_YEAR):
	movieTitlesFile = open("movieTitles.txt", "r")
	movie_titles_JSON = {"type":"movie titles"}
	l_movie_titles = []

	#Reading the movie titles specific to that year
	counter_min = (int(year) - EARLIEST_YEAR) * 50
	counter_max = counter_min + 50
	counter = 0

	for line in movieTitlesFile:
		if (counter >= counter_min and counter < counter_max):
			l_movie_titles.append(line[:len(line) - 1])

		counter+=1

	movie_titles_JSON["titles"] = l_movie_titles
	return(movie_titles_JSON)

def get_youtube_list(title, max_results):
	with open('service1.pkl', 'rb') as input:
		youtube = pickle.load(input)

	max_results = 5
	queryTerm =  title + ' movie review'
	movieListJSON = search_videos_list(youtube, queryTerm, max_results)

	l_video_id = []

	for item in movieListJSON:
		videoId = item["id"]["videoId"]
		channelId = item["snippet"]["channelId"]
		videoTitle = item["snippet"]["title"]
		videoDescription = item["snippet"]["description"]
		channelTitle = item["snippet"]["channelTitle"]
		mediaTitle = title

		stats_response = get_video_stats(youtube, videoId)

		view_count = stats_response[0]["statistics"]["viewCount"]
		like_count = stats_response[0]["statistics"]["likeCount"]
		dislike_count = stats_response[0]["statistics"]["dislikeCount"]
		favorite_count = stats_response[0]["statistics"]["favoriteCount"]
		comment_count = stats_response[0]["statistics"]["commentCount"]

		l_video_id.append(videoId)

		video = Video(id=videoId, title=videoTitle, views=view_count, likeCount=like_count,
			dislikeCount=dislike_count, channel_id=channelTitle, favoriteCount=favorite_count, commentCount=comment_count, mediaTitle=mediaTitle)
		print(video)
		db.session.add(video)

		#Add video description
		description = Description(body=videoDescription, video_id=videoId)
		db.session.add(description)
		db.session.commit()
	print(l_video_id)
	return_JSON = {"video_IDs" : l_video_id}
	return return_JSON

def comment_threads(video_id, max_comment_threads):
	with open('service1.pkl', 'rb') as input:
		youtube = pickle.load(input)

	commentThreads = get_comment_threads(youtube, video_id, max_comment_threads)

	for item in commentThreads: 
		parentId = item["id"]
		topLevelComment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

		comment = Comment(body=topLevelComment, video_id=video_id)

		db.session.add(comment)

	db.session.commit()

	return_JSON = {"status" : 'success'}
	return return_JSON

def remove_video_entry(videoid):
	video = Video.query.filter_by(id=videoid).first()
	if (video is None):
		return('not found')

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


