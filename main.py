import requests
from send_email import send_email

topic = "tesla"

api_key = "cf9a1d5e4a314be49d74a36b89f450d2"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-08-04&" \
      "sortBy=publishedAt&apiKey=cf9a1d5e4a314be49d74a36b89f450d2&" \
      "language=en"


request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + \
               "\n" + body + article["title"] + "\n" \
               + article["description"] + \
               "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
