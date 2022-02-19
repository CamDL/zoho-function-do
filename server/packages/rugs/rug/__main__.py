import os
from requests_oauthlib import OAuth2Session

def main(args):
    ID = args.get("ID")
    envars = os.environ
    client_id = envars['CLIENT_ID']
    client_secret = envars['CLIENT_SECRET']

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
    client = OAuth2Session(client_id, token=token, auto_refresh_url=refresh_url, auto_refresh_kwargs=extra)

    client.refresh_token(refresh_url)

    rug = client.get(f"https://creator.zoho.com/api/v2/troylusk/cleaning-process/report/Rug_Information_Report/{ID}").json()
    return {"body":rug}