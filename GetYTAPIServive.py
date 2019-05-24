import os

import google.oauth2.credentials
import pickle

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl'] 
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
CLIENT_SECRETS_FILE = "client_secret.json"
OAUTH_CODE = ""


#This takes a while
def get_authenticated_service():
	flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
	credentials = flow.run_local_server()
	print(credentials)
	return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)



if __name__ == '__main__':
  # When running locally, disable OAuthlib's HTTPs verification. When
  # running in production *do not* leave this option enabled.
  os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '0'

  print("Getting authorization")

  service = get_authenticated_service()

  print("Saving service")
  with open('service1.pkl', 'wb') as output:
  	pickle.dump(service, output, pickle.HIGHEST_PROTOCOL)



