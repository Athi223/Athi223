import chevron
import requests

try:
    response = requests.get("https://www.reddit.com/r/rProgrammerHumor.json")
    print(response)
    print(response.text)
    results = response.json()

    url = results["data"]["children"][0]["url"]
    with open("main.mustache", "r") as mustache:
        content = chevron.render(mustache, { "image": url })
        with open("README.md", "w") as readme:
            readme.write(content)
except Exception as e:
    print(e)
    print("Failed to generate README")
