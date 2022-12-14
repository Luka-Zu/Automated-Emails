# 9646d008451e4212b437cb0f9805d16d
# 7qz7sxra@spymail.one
# aeqoirnpt@10mail.orgimport
# mboczlxmc@supere.mlx
from filestack.utils import requests


class NewsFeed:
    """
        Representing multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "9646d008451e4212b437cb0f9805d16d"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.language = language
        self.to_date = to_date
        self.from_date = from_date
        self.interest = interest

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)
        # print(x)
        # pprint(content)

        email_body = ''
        for article in articles:
            email_body = email_body + article['title'] + '\n' + article['url'] + '\n\n'

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content['articles']
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"

        return url
