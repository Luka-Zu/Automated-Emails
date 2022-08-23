# 9646d008451e4212b437cb0f9805d16d
import requests
from pprint import pprint


class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


url = "https://newsapi.org/v2/everything?" \
      "qInTitle=tesla&" \
      "from=2022-07-23&" \
      "to=2022-07-23&" \
      "language=en&" \
      "apiKey=9646d008451e4212b437cb0f9805d16d"

response = requests.get(url)
content = response.json()
articles = content['articles']
# print(x)
# pprint(content)


email_body = ''
for article in articles:
    email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

print(email_body)
