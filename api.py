import requests
def make_api_call():
    URL = "https://dog.ceo/api/breeds/image/random"
    request_pic = requests.get(url = URL)
    data = request_pic.json()
    return data
print(make_api_call()
