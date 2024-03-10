from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from chatbot_start_conversation import Chatbot
import chatbot_general 
app = Flask('__name__')

CORS(app, resources={r"/api/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def home():
    return 'Welcome!'


@app.route('/user_start_covo', methods=['POST'])
@cross_origin()
def user_start_covo():
    usr_rqs = request.json
    prompt = usr_rqs['msg']

    response = my_chatbot.get_response(prompt)
    if "I'm Sorry" in response:
        result = False
    else:
        reuslt = True
    return result

@app.route('/user_chat_general', methods=['POST'])
@cross_origin()
def user_char_general():
    usr_rqs = request.json
    prompt = usr_rqs['msg']
    context = usr_rqs['context']

    my_general_chat = chatbot_general.Chatbot(context)
    result = my_general_chat.get_response(prompt)
    return result

if __name__ == "__main__":
    my_chatbot = Chatbot()
    app.run()
