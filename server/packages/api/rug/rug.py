import os
import requests
from dotenv import load_dotenv
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import json

load_dotenv()

envars = os.environ
client_id = envars['CLIENT_ID']
client_secret = envars['CLIENT_SECRET']

#Zoho API Settings
client = BackendApplicationClient(client_id=client_id)
oauth = OAuth2Session(client=client)

token = oauth.fetch_token(token_url='https://accounts.zoho.com/oauth/v2/token?grant_type=authorization_code', client_id=client_id,
    client_secret=client_secret)

def token_saver(token):
    envars['OAUTH_TOKEN'] = token

token = {
    'access_token': envars['ACCESS_TOKEN'],
    'refresh_token': envars['REFRESH_TOKEN'],
    'token_type': 'Bearer',
    'expires_in': envars['EXPIRES_IN'],
}
refresh_url = 'https://accounts.zoho.com/oauth/v2/token'
extra = {
    'client_id': client_id,
    'client_secret': client_secret,
}
# After updating the token you will most likely want to save it.
client = OAuth2Session(client_id, token=token, auto_refresh_url=refresh_url,
    auto_refresh_kwargs=extra, token_updater=token_saver)

#rugs = client.get('https://creator.zoho.com/api/v2/troylusk/cleaning-process/report/Rug_Information_Report').json()

#rug = client.get(f"https://creator.zoho.com/api/v2/troylusk/cleaning-process/report/Rug_Information_Report/{rugs['data'][1]['ID']}").json()

#jsonval  = json.dumps(rug['data'])

def main(args):
      ID = args.get("ID")
      rug = client.get(f"https://creator.zoho.com/api/v2/troylusk/cleaning-process/report/Rug_Information_Report/{ID}").json()
      return rug