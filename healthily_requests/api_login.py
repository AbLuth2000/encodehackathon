import requests
import uuid
from dotenv import load_dotenv
import os

# Load variables from .env into environment
load_dotenv()

# Constants
url = "https://portal.your.md/v4/login"
token = "token " + os.getenv('HEALTHILY_API_TOKEN')
key = os.getenv('HEALTHILY_API_KEY')


# Returns bearer token for API calls
def get_login():
    payload = {
        "id": str(uuid.uuid4())
    }
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "Authorization": token,
        "x-api-key": key
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        print(response.text)
        statusCode = response.status_code
        response = response.json()

        if statusCode == 200:
            return {
                "statusCode": 200,
                "output": response['access_token']
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
