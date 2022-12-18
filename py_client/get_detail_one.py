import requests
from urllib.parse import unquote
endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.get(endpoint)
try:

    a=get_response.json()
    print(a)
except:
    print('empty inside')
