import requests

response = requests.get("http://b:5000/toto")
print(response.text)