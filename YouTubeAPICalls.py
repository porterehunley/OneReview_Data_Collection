import pickle
import pandas as pd 
from pandas.io.json import json_normalize

with open('commentThread1.pkl', 'rb') as input:
	commentThread1 = pickle.load(input)

with open('service1.pkl', 'rb') as input:
	service1 = pickle.load(input)




def comment_threads_list_by_video_id(client, **kwargs):
  response = client.commentThreads().list(
    **kwargs
  ).execute()
  with open('commentThread1.pkl', 'wb') as output: 
  	pickle.dump(response, output, pickle.HIGHEST_PROTOCOL)
  return print(response)


def get_comments(youtube, parent_id):
  results = youtube.comments().list(
    part="snippet",
    parentId=parent_id,
    textFormat="plainText"
  ).execute()

  for item in results["items"]:
    author = item["snippet"]["authorDisplayName"]
    text = item["snippet"]["textDisplay"]
    print("Comment by %s: %s" % (author, text))

  return results["items"]

def get_comment_threads(youtube, video_id):
  results = youtube.commentThreads().list(
    part="snippet",
    videoId=video_id,
    textFormat="plainText"
  ).execute()


  for item in results["items"]:
    comment = item["snippet"]["topLevelComment"]
    author = comment["snippet"]["authorDisplayName"]
    text = comment["snippet"]["textDisplay"]
    print("Comment by %s: %s" % (author, text))

  return results["items"]

def get_list_of_movies(youtube, searchTerm):
  request = youtube.search().list(
        part="snippet",
        q=searchTerm
    )
  response = request.execute()
  return response


def main():
  movieTitlesFile = open("movieTitles.txt", "r")
  NUMBER_OF_LIST_REQUESTS = 1
  counter = 0

  for line in movieTitlesFile:

    if (counter == NUMBER_OF_LIST_REQUESTS):
      break

    queryTerm = line[:len(line) - 1] + ' movie review'
    print(get_list_of_movies(service1, queryTerm))

    counter += 1




if (__name__ == '__main__'):
  main()




# get_comment_threads(service1, "2b7KIczP2G4")

#get_comments(service1, commentThread1[0]["id"])





