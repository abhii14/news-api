import requests


api_key = "cf9a1d5e4a314be49d74a36b89f450d2"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-04&sortBy=publishedAt&apiKey=cf9a1d5e4a314be49d74a36b89f450d2"
request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])