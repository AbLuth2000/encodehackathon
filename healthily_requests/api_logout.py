import requests

## Constants
url = "https://portal.your.md/v4/logout"

def logout(bearer):
    headers = {
        "accept": "*/*",
        "authorization": "Bearer " + bearer
    }

    try:
        response = requests.post(url, headers=headers)

        statusCode = response.status_code
        response = response.json()

        if statusCode == 200:
            return {
                "statusCode": 200,
                "output": "Log out successful."
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