import util.slap_utils as su
import requests
import json
import base64
from urllib.parse import quote_plus

encoded = base64.b64encode(b'Hello World!')

app_id = su.get_tokens()['wolfram_alpha_id']

# Simple API base url
# base_url = f'http://api.wolframalpha.com/v1/simple?appid={app_id}&i='

# Full API base url

base_url = f'https://api.wolframalpha.com/v2/query?appid={app_id}&format=image&output=json&mag=3&input='
query = su.get_arg('query')

if query is None:
    result = {
        "view": {
            "type": "form",
            "title": "Search Wolfram|Alpha",
            "submitLabel": "Search",
            "fields": [
                {
                    "type": "text",
                    "id": "query",
                    "label": "Search query:"
                }
            ]
        }
    }
else:
    # Convert the query to a URL-friendly format
    query = quote_plus(query)

    response = requests.get(base_url + query).json()

    image_urls = []

    def store_all_images(obj):
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == 'img':
                    image_urls.append(value['src'])
                else:
                    store_all_images(value)
        elif isinstance(obj, list):
            for item in obj:
                store_all_images(item)

    store_all_images(response)

    result = {
        "view": {
            "type": "masonry",
            "options": [
                {
                    "imageURL": url,
                    "action": {
                        "type": "open-url",
                        "url": 'https://www.wolframalpha.com/input/?i=' + query
                    }
                }
                for index, url in enumerate(image_urls)
            ]
        }
    }

print(json.dumps(result))