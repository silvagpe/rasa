import requests
from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api

from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['DEBUG'] = True
app.config['JSON_SORT_KEYS'] = False

# Creating appi instance
api = Api(app)


class rasa(Resource):
    def get(self):
        return jsonify({"message": "Api rasa. utilize envio de mensagens por POST"})

    def post(self):

        if (request.get_json() == None):
            return Response("No content", status=204, mimetype='application/json')

        id = request.get_json()['id']
        msg = request.get_json()['msg']

        url = 'http://localhost:5005/webhooks/rest/webhook'

        data = {'sender': id, 'message': msg}

        result = requests.post(url, json=data)

        print("*"*40)
        print(result.json())
        print("*"*40)

        return jsonify(result.json())


api.add_resource(rasa, '/chat')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
