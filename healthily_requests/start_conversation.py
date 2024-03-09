import requests
from api_login import get_login
from api_logout import logout
from dotenv import load_dotenv
import os

# Load variables from .env into environment
load_dotenv()

# Constants
url = "https://portal.your.md/v4/chat"
key = os.getenv('HEALTHILY_API_KEY')


def chat(bearer_token):
    payload = { "answer": {
            "type": "entry",
            "name": "test",
            "gender": "male",
            "year_of_birth": 2000,
            "initial_symptom": "coughing",
            "other": True
        } }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": bearer_token,
        "x-api-key": key
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    return response.json()


def main():
    # Get bearer token to use for API calls
    get_login_output = get_login()
    bearer_token = "Bearer " + get_login_output['output']
    print(bearer_token)

    print(chat(bearer_token))


main()