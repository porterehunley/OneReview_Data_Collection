import requests 

#The server controller calls the internal APIs in sequential
#order and monitors their responses 

#TODO check quotas

class Server_Controller:

	running = False
	CURRENT_API = 0
	CURRENT_FILE_INDEX = 0
	l_movie_titles = []


	def __init__(self):
		self.set_media_titles()

	def run(self):
		for title in l_movie_titles:
			l_videoIDs = get_videos(title)
			for video_id in l_videoIDs:
				get_comment_threads(video_id)
				get_video_captions(video_id)

	def set_media_titles(self):
		movieTitlesFile = open("movieTitles.txt", "r")
		for line in movieTitlesFile:
			self.l_movie_titles.append(line[:len(line) - 1])

	def get_videos(self, title):
		videoIDs_JSON = requests.get('http://127.0.0.1:5000/youtube_list/'+ title)

		if (videoIDs_JSON.status_code == requests.codes.ok): 
			l_videoIDs = videoIDs_JSON['video_IDs']
			return l_videoIDs

		return None

	def get_comment_threads(self, l_videoIDs):
		for video_id in l_videoIDs:
			response = requests.get('http://127.0.0.1:5000/comment_threads/'+video_id)
			if (response.status_code != requests.codes.ok):
				pass

	def get_video_captions(self, l_videoIDs):
		for video_id in l_videoIDs:
			response = requests.get('http://127.0.0.1:5000/video_caption/'+video_id)
			if (response.status_code != requests.codes.ok):
				pass








	









