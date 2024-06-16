import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/createJira", methods=["POST"])
def createJira():
    url = "https://karthikskrsappidi.atlassian.net/rest/api/2/issue"
    API_TOKEN = 'your_api_token_here'
    auth = HTTPBasicAuth("your_email_here", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps({
        "fields": {
            "description": "My First Jira Ticket.",
            "issuetype": {
                "id": "10001"
            },
            "project": {
                "key": "KAR"
            },
            "summary": "First Jira Ticket"
        }
    })

    response = requests.post(
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
