import pickle
import HelloYTAPI

print("Loading authorization")
with open('service1.pkl', 'rb') as input:
    service1 = pickle.load(input)



# print("This is probably going to time out")
# HelloYTAPI.channels_list_by_username(service1,
#       part='snippet,contentDetails,statistics',
#       forUsername='GoogleDevelopers')


# def remove_empty_kwargs(**kwargs):
#   good_kwargs = {}
#   if kwargs is not None:
#     for key, value in kwargs.iteritems():
#       if value:
#         good_kwargs[key] = value
#   return good_kwargs

def comment_threads_list_by_video_id(client, **kwargs):
  # See full sample for function
  # kwargs = remove_empty_kwargs(**kwargs)

  response = client.commentThreads().list(
    **kwargs
  ).execute()
  return print(response)

print("Calling commentThreads")


comment_threads_list_by_video_id(service1,
    part='snippet,replies',
    videoId='EKyirtVHsK0')
 