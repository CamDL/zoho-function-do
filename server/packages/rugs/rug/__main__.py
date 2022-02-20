import os
from requests_oauthlib import OAuth2Session
from urllib.parse import urlparse
from urllib.parse import parse_qs

def main(args):
    #main({"ID":"3183625000003900011"})
    ID = args.get("ID")

    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')

    report_key = 'yMR3JSmwXqZq3B5jEt5fDON0z24R7R8HNZD7058ktb2EdTU93UbjS7V4sbpPMPaMrZVe3RGk4yhxGk8usFO540B6EhwrrVtyADxY'

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
        for item in list(rug['data']):
            if "Image" in item:
                value = rug['data'][item]
                parsed = urlparse(value)
                file_path = parse_qs(parsed.query)['filepath'][0]
                url = f'https://creator.zohopublic.com/troylusk/cleaning-process/Rug_Inspection_Report/{ID}/{item}/image-download/{report_key}/{file_path}'
                rug['data'][item] = url
        message = rug
        return {"body": message}
    else:
        message = "No rug could be found. Sorry!"
        return {"body": message}