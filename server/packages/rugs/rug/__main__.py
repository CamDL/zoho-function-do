import os
from requests_oauthlib import OAuth2Session
import json
import boto3
import mimetypes

def store_image(id, field, response):
    bucket = 'cdl-doserverless'
    s3session = boto3.session.Session()
    s3client = s3session.client('s3', region_name='nyc3',
        endpoint_url='https://nyc3.digitaloceanspaces.com',
        aws_access_key_id=os.environ.get('SPACES_KEY'),
        aws_secret_access_key=os.environ.get('SPACES_SECRET'))
    ext = mimetypes.guess_extension(response.headers['Content-Type'].partition(';')[0].strip())
    key = f'{id}_{field}.{ext}'
    s3client.put_object(Bucket=bucket,
        Key=key,
        Body=response.content,
        ACL='private')
    url = s3client.generate_presigned_url(ClientMethod='get_object',
        Params={'Bucket': bucket, 'Key': key, 'ResponseContentDisposition' : 'inline; filename=image.jpg'}, ExpiresIn=300)
    return url

def main(args):
    #main({"ID":"3183625000003900011"})
    ID = args.get("ID")

    client_id = os.environ.get('CLIENT_ID')
    client_secret = os.environ.get('CLIENT_SECRET')

    base_url = 'https://creator.zoho.com'

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
                response = client.get(base_url + value)
                url = store_image(ID, item, response)
                rug['data'][item] = url
        return { "body": rug }
    else:
        message = "No rug could be found. Sorry!"
        return {"body": message}