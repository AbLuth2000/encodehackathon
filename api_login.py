import requests

## Constants
url = "https://portal.your.md/v4/login"
auth = "token PzHgtWDsi6e68RHxw0lpcG8y8vR0XZXQ.6HOpZ7mz6ciEWTltkGAjxcR6Xjb9MFLT"
key = "5o9ncNup791OpzXmfvlVe1U5NezerRdc89b3I0xz"


def get_login():
    payload = {
        "id": "abhy3230", ## unique id
        "name": "Abhyuday", ## optional name
        "email": "abhyudayluthra2000@gmail.com" ## optional email
    }
    headers = {
        "accept": "*/*",
        "content-type": "application/json",
        "Authorization": auth,
        "x-api-key": key
    }

    response = requests.post(url, json=payload, headers=headers)

    print(response.text)
    return(response.json)


get_login()