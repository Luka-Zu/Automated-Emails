# 9646d008451e4212b437cb0f9805d16d
import requests
from pprint import pprint


class NewsFeed:
    """
        Representing multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "9646d008451e4212b437cb0f9805d16d"

    def __init__(self, interest, from_date, to_date, language):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"

        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        # print(x)
        # pprint(content)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body


new_feed = NewsFeed("tesla", "2022-07-23", "2022-07-23", "en")
print(new_feed.get())

# url = "https://newsapi.org/v2/everything?" \
#       "qInTitle=tesla&" \
#       "from=2022-07-23&" \
#       "to=2022-07-23&" \
#       "language=en&" \
#       "apiKey=9646d008451e4212b437cb0f9805d16d"
#
# response = requests.get(url)
# content = response.json()
# articles = content['articles']
# # print(x)
# # pprint(content)
#
#
# email_body = ''
# for article in articles:
#     email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'
#
# print(email_body)
