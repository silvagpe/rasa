import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False


@app.route("/chat", methods=['GET', 'POST'])
def rasa():

    if request.method == 'POST':

        if (request.get_json() == None):
            return "No content"

        id = request.get_json()['id']
        msg = request.get_json()['msg']

        url = 'http://localhost:5005/webhooks/rest/webhook'
        data = {'sender': id, 'message': msg}

        result = requests.post(url=url, json=data)
        print("*",40);
        print(result);
        print("*",40);

        return jsonify(result.json())

    return "API Flask Rasa"


if __name__ == "__main__":
    app.run()
