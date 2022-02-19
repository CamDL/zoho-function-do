import os
from requests_oauthlib import OAuth2Session

def main(args):
    ID = args.get("ID")
    expires  = str(os.environ.get('EXPIRES_IN'))
    return {"body": str(ID + expires)}