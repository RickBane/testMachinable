import requests

url = "https://pet-demo.machinable.io/api/dogs/d60610cf-6a6b-47ff-b945-8d1f8ee4ff54"

headers = {}

response = requests.request("GET", url, headers=headers)

print(response.text)