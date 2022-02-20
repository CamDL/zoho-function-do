import os
import boto3

def main(args):
    bucket = 'cdl-doserverless'
    key = os.environ.get('SPACES_KEY')
    secret = os.environ.get('SPACES_SECRET')
    session = boto3.session.Session()
    client = session.client('s3', region_name='nyc3',
        endpoint_url='https://nyc3.digitaloceanspaces.com',
        aws_access_key_id=key,
        aws_secret_access_key=secret)
    files = []
    response = client.list_objects(Bucket=bucket)
    for obj in response['Contents']:
        files.append(obj['Key'])
    return files