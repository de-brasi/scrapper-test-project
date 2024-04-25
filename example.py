import requests

# URL and header information
url = "http://localhost:8080/scrapper/api/links"
headers = {"Tg-Chat-Id": "1031778568"}

# Send GET request 5 times
for _ in range(5):
    response = requests.get(url, headers=headers)
    print("Response:", response.text)
