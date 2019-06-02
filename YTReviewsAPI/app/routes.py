from app import app
from app import db
from app.models import Video, Description, Comment
from flask import Response
import requests 
import datetime
from lxml import html
from lxml.etree import tostring
import pickle



@app.route('/get_movie_titles')
def get_movie_titles():
	try:
		START_YEAR = 2014
		END_YEAR = 2018
		movieYear = START_YEAR

		for i in range(END_YEAR - START_YEAR):
			IMDBUrl = 'https://www.imdb.com/search/title?year=' + str(movieYear) + '&title_type=feature&'


			imdbMoviePage = requests.get(IMDBUrl)

			#Movie page is now in a tree an accessible with xpath
			movieTree = html.fromstring(imdbMoviePage.content)

			movieHeaders= movieTree.xpath('//h3[@class="lister-item-header"]')

			#Write movies to csv
			fileStream = open("movieTitles.txt", "a+")
			for header in movieHeaders:

				headerStr = html.tostring(header, encoding='unicode')
				startIndex = headerStr.index('/">')
				endIndex = headerStr.index('</a>')
				
				headerTitle = headerStr[startIndex + 3 : endIndex]
				
				fileStream.write(headerTitle + '\n')
			fileStream.close()	

			movieYear = movieYear + 1

		return Response("{'status':'success!'}", status=200, mimetype='application/json')
	except:
		return Response("{'status':'An error occurred!'}", status=500, mimetype='application/json')

@app.route('/list_of_movies', methods=['GET'])
def get_list_of_movies():
	with open('service1.pkl', 'rb') as input:
		youtube = pickle.load(input)

	movieTitlesFile = open("movieTitles.txt", "r")
	NUMBER_OF_LIST_REQUESTS = 1
	counter = 0
	MAX_COMMENT_THREADS = 100

	#Get the relevant JSON 
	for line in movieTitlesFile:

		if (counter == NUMBER_OF_LIST_REQUESTS):
			break

		queryTerm = line[:len(line) - 1] + ' movie review'

		request = youtube.search().list(
			part="snippet",
			q=queryTerm,
			type="video"
		)

		response = request.execute()
		movieListJSON = response

		for item in movieListJSON["items"]:

			videoId = item["id"]["videoId"]
			channelId = item["snippet"]["channelId"]
			videoTitle = item["snippet"]["title"] + "T%"
			videoDescription = item["snippet"]["description"]
			channelTitle = item["snippet"]["channelTitle"]

			video = Video(id=videoId, title=videoTitle,)
			db.session.add(video)

			description = Description(body=videoDescription, video_id=videoId)
			db.session.add(description)

			commentThreads = get_comment_threads(youtube, videoId, MAX_COMMENT_THREADS)
			for item in commentThreads: 
				parentId = item["id"]
				topLevelComment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]

				comment = Comment(body=topLevelComment, video_id=videoId)

				db.session.add(comment)

			db.session.commit()


		counter += 1

	return Response("{'status':'success!'}", status=200, mimetype='application/json')

def get_comment_threads(youtube, video_id, max_results):
	request = youtube.commentThreads().list(
		part="snippet",
		maxResults=100,
		textFormat="plainText",
		videoId=video_id
	)

	response = request.execute()

	return response["items"]

def get_comments(youtube, parent_id):
	request = youtube.comments().list(
		part="snippet",
		parentId=parent_id,
		textFormat="plainText"
	)

	response = request.execute()

	return response["items"]









	
