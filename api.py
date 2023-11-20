import requests

url = "https://api.nasa.gov/planetary/apod?api_key=fF8fImK6ng3LZtsMxGxZU8rmckfl0gfdNQFL6VeP"

api_key = "fF8fImK6ng3LZtsMxGxZU8rmckfl0gfdNQFL6VeP"

request = requests.get(url)
content = request.json()
print(content)

def get_title():
    title = content["title"]
    return title


response = requests.get(content["url"])

with open("image.jpg", "wb") as file:
    file.write(response.content)


def get_explanation():
    explanation = content["explanation"]
    return explanation


def get_copy():
    copy = content["copyright"]
    return copy
