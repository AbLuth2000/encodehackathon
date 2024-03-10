import requests
from api_login import get_login
from api_logout import logout
from dotenv import load_dotenv
import os
from pymongo import MongoClient
from bson import ObjectId

# Load variables from .env into environment
load_dotenv()

# Constants
url = "https://portal.your.md/v4/chat"
key = os.getenv('HEALTHILY_API_KEY')
mongo_username = os.getenv('MONGODB_USERNAME')
mongo_password = os.getenv('MONGODB_PASSWORD')


def get_mongo_values():
    mongo_uri = f"mongodb+srv://{mongo_username}:{mongo_password}@healthilycluster.q61yhul.mongodb.net/"
    client = MongoClient(mongo_uri)
    db = client['Conversations']
    collection = db['HealthilyCluster']

    # Find the document by its _id field
    document = collection.find_one({"_id": ObjectId('65eccdcca76d4803694c0cb2')})
    print(document)

    if document:
        return document
    else:
        print("No document found with the specified _id.")
        return None


def chat(bearer_token, conversation, payload_answer):
    payload = {
        "answer": payload_answer,
        "conversation": {
            "id": conversation
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
                "output": response,

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


def main():
    mongo_values = get_mongo_values()

    print(chat(mongo_values['bearer_token'], mongo_values['conversation_id']))


main()