import requests
from api_login import get_login
from api_logout import logout
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson import ObjectId
from enhance_output import enhance_output
from playsound import playsound
from text_to_speech import output_to_mp3

# Load variables from .env into environment
load_dotenv()

# Constants
url = "https://portal.your.md/v4/chat"
key = os.getenv('HEALTHILY_API_KEY')
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')


def start_conversation(bearer_token, name, gender, year_of_birth, initial_symptom):
    payload = {
        "answer": {
            "type": "entry",
            "name": name,
            "gender": gender,
            "year_of_birth": year_of_birth,
            "initial_symptom": initial_symptom,
            "other": True
        }
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": bearer_token,
        "x-api-key": key
    }

    try:
        response = requests.post(url, json=payload, headers=headers)

        statusCode = response.status_code
        response = response.json()

        if statusCode == 200:
            return {
                "statusCode": 200,
                "output": response
            }
        else:
            return {
                "statusCode": statusCode,
                "output": f"Error: {response['error']}"
            }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "output": f"An error occured: {e}"
        }


def update_mongo_db(bearer_token, conversation_id, latest_message):
    mongo_uri = f"mongodb+srv://{mongo_username}:{mongo_password}@healthilycluster.q61yhul.mongodb.net/"
    client = MongoClient(mongo_uri)
    db = client['Conversations']
    collection = db['HealthilyCluster']

    filter = {'_id': ObjectId('65eccdcca76d4803694c0cb2')}
    update_token = {
        '$set': {
            'bearer_token': bearer_token,
            'conversation_id': conversation_id,
            'latest_healthily_output': latest_message
        }
    }
    token_result = collection.update_one(filter, update_token)

    if token_result.modified_count > 0:
        print("MongoDB updated successfully.")
    else:
        print("No document found matching the provided filter.")


def main(name, gender, year_of_birth, initial_symptom):
    # Get bearer token to use for API calls
    get_login_output = get_login()
    bearer_token = "Bearer " + get_login_output['output']

    # Start conversation
    conversation_output = start_conversation(bearer_token, name, gender, year_of_birth, initial_symptom)
    print(conversation_output)

    update_mongo_db(bearer_token, conversation_output['output']['conversation']['id'], conversation_output['output']['question'])

    enhanced_output = enhance_output(conversation_output['output']['question'])
    output_to_mp3(enhanced_output)
    print(enhanced_output)

    playsound('requests/speech.mp3')
    print('Playing sound using  playsound')

    return conversation_output

main("Abhyuday", "male", 2000, "I have a rash on my neck.")

# Next choices confirm symptoms or restart conversation with updated initial symptoms