import requests

def main(args):
    cat = args.get("category","all")
    payload = {'category' : cat}
    response = requests.get('https://inshortsapi.vercel.app/news', params=payload)
    return response.json()