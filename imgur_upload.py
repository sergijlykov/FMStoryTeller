import base64
import json
import requests

from base64 import b64encode

client_id = 'my-client-id'

headers = {"Authorization": "Client-ID my-client-id"}

api_key = 'my-api-key'

url = "https://ali.imgur.com/3/upload.json"

j1 = requests.post(
    url,
    headers = headers,
    data = {
        'key': api_key,
        'image': b64encode(open('1.jpg', 'rb').read())
        'type': 'base64',
        'name': '1.jpg',
        'title': ' Picture np. 1'
    }
)