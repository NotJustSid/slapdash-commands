# Calculate using MathJS with
import util.slap_utils as su
import requests
import json
from urllib.parse import quote_plus

precision=14

base_url = f'https://api.mathjs.org/v4/?precision={precision}&expr='
query = su.get_arg('keywords')

response_text = ''

if query is None:
    response_text = 'Please enter a query'
else:
    response_text = requests.get(base_url + quote_plus(query)).content.decode('utf-8')

result = {
        "view": response_text
    }

print(json.dumps(result))