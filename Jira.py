# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST'])
def createJira():

    url = "https://veeramallaabhishek.atlassian.net/rest/api/3/issue"

    API_TOKEN="ATATT3xFfGF009KOiVEkOreq2-t-BYIiYEKmhOlHfEb0eUVSsDmxsUn1H8aAaw7m26iBDo-edAv6ZikQ9hNx5tUxxlVq7qK4OYWi0Y6sv6GcfEUljM0UpAMU2VEhauQFsPJ5Fg2ejEOuHU98AHGs2SYX_32hgeljTy4qxgAUTBjNLscGbUxizT0=27A8EA9C"

    auth = HTTPBasicAuth("jagadeeshkumar242@gmail.com", API_TOKEN)

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "MP"
        },
        "issuetype": {
            "id": "10004"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )


    response = requests.request(
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )

    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
