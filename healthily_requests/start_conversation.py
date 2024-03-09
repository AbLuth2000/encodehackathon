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


def start_conversation(bearer_token):
    payload = {
        "answer": {
            "type": "entry",
            "name": "test",
            "gender": "male",
            "year_of_birth": 2000,
            "initial_symptom": "My stomach is hurting.",
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


def main():
    # Get bearer token to use for API calls
    get_login_output = get_login()
    bearer_token = "Bearer " + get_login_output['output']

    # Start conversation
    conversation_output = start_conversation(bearer_token)
    print(conversation_output)

    # Logout of bearer token
    logout(get_login_output['output'])

    return conversation_output

main()