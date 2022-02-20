import os
import boto3
from PIL import Image
from io import BytesIO

def main(args):
    file = args.get("file")
    if file:
        bucket = 'cdl-doserverless'
        key = os.environ.get('SPACES_KEY')
        secret = os.environ.get('SPACES_SECRET')
        session = boto3.session.Session()
        client = session.client('s3', region_name='nyc3',
            endpoint_url='https://nyc3.digitaloceanspaces.com',
            aws_access_key_id=key,
            aws_secret_access_key=secret)
        response = client.get_object(
            Bucket=bucket,
            Key=file
        )
        object_content = response['Body'].read()
        max_size = (1024,1024)
        prefix = '1024x1024'
        image = Image.open(BytesIO(object_content))
        image.thumbnail(max_size)
        img_byte_arr = BytesIO()
        image.save(img_byte_arr, format='JPEG')
        resized = img_byte_arr.getvalue()
        response = client.put_object(Bucket=bucket,
            Key= prefix+'_'+file,
            Body=resized,
            ACL='private')
        return {"body" : "Image saved!"}
    else:
        return {"body" : "No file was specified."}