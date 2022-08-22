# 9646d008451e4212b437cb0f9805d16d
import  requests
from pprint import pprint
class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass

response = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2022-07-22&sortBy=publishedAt&apiKey=9646d008451e4212b437cb0f9805d16d")
content = response.text
pprint(content)