# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://karthikskrsappidi.atlassian.net/rest/api/2/project"

API_TOKEN= '*************'
auth = HTTPBasicAuth("karthikskrsappidi@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.loads(response.text)[0]["name"])
