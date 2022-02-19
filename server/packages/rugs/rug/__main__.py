import os
from requests_oauthlib import OAuth2Session

def main(args):
    #main({"ID":"3183625000003900011"})
    ID = args.get("ID")
    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')

    token = {
        'access_token': os.environ.get('ACCESS_TOKEN'),
        'refresh_token': os.environ.get('REFRESH_TOKEN'),
        'token_type': 'Bearer',
        'expires_in': os.environ.get('EXPIRES_IN'),
    }
    refresh_url = 'https://accounts.zoho.com/oauth/v2/token'
    extra = {
        'client_id': client_id,
        'client_secret': client_secret,
    }
    client = OAuth2Session(client_id, token=token, auto_refresh_url=refresh_url,
        auto_refresh_kwargs=extra)

    client.refresh_token(refresh_url)

    rug = client.get(f"https://creator.zoho.com/api/v2/troylusk/cleaning-process/report/Rug_Information_Report/{ID}").json()
    if rug:
        message = rug
    else:
        message = "No rug could be found. Sorry!"
    return {"body": message}