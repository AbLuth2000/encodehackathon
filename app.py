from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from chatbot import Chatbot

app = Flask('__name__')

CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return 'Welcome!'


@app.route('/user', methods=['POST'])
@cross_origin()
def user():
    usr_rqs = request.json
    prompt = usr_rqs['msg']

    response = my_chatbot.get_response(prompt)
    result = f"{response['result']}"
    return result


if __name__ == "__main__":
    my_chatbot = Chatbot("./chroma", "sentence-transformers/all-MiniLM-L6-v2")
    app.run()

