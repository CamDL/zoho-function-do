import os
import boto3
from dotenv import load_dotenv

load_dotenv()

def main(args):
    bucket = 'cdl-doserverless'
    session = boto3.session.Session()
    client = session.client('s3', region_name='nyc3',
        endpoint_url='https://nyc3.digitaloceanspaces.com',
        aws_access_key_id=os.environ.get('SPACES_KEY'),
        aws_secret_access_key=os.environ.get('SPACES_SECRET'))
    files = []
    response = client.list_objects(Bucket=bucket)
    for obj in response['Contents']:
        files.append(obj['Key'])
    return files