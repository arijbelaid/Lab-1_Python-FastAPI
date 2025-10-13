#//GET Request//
import requests

url = "https://www.example.com"
response = requests.get(url)
# it will show the HTTP status code
print(response)
print(response.status_code)


import requests

response = requests.get("https://www.example.com")
print(response.content)

#//POST Request//
data = {"name": "Salah", "message": "Hello!"}
url = "https://httpbin.org/post"

response = requests.post(url, json=data)
response_data = response.json()
# Shows the data as a dictionary
print(response_data)

#//Handling Errors//
import requests

# here we use an endpoint that always gives a 404 status error
response = requests.get("https://httpbin.org/status/404")
# if status code is not 200 (successful response), then show error message
if response.status_code != 200:
    print(f"HTTP Error: {response.status_code}")


#//Setting a Timeout//
url = "https://httpbin.org/delay/10"

try:
    response = requests.get(url, timeout=5)
except requests.exceptions.Timeout as err:
    print(err)


#//HTTP Request Headers//
auth_token = "XXXXXXXX"

# here we set the authorization header with the 'bearer token' for authentication purposes.
headers = {
    "Authorization": f"Bearer {auth_token}"
}

url = "https://httpbin.org/headers"
response = requests.get(url, headers=headers)
print(response.json())


#//Web Scraping with BeautifulSoup//
import requests

url = "https://www.example.com"
# this will get all the HTML, javascript, css code
response = requests.get(url)


import requests
from bs4 import BeautifulSoup

url = "https://www.example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
title = soup.title.text
content = soup.find("p").text
links = [a["href"] for a in soup.find_all("a")]

print(title, content, links)

#//Requests vs urllib//
import urllib.request
import urllib.parse

# Préparer les données à envoyer
data = urllib.parse.urlencode({"name": "Salah", "message": "Hello!"}).encode("utf-8")

# Créer une requête POST vers httpbin.org
req = urllib.request.Request("https://httpbin.org/post", data=data, method="POST")

# Envoyer la requête et lire la réponse
with urllib.request.urlopen(req) as response:
    html = response.read().decode("utf-8")

print(html)

