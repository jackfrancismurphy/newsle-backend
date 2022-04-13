import requests
from newsapi import NewsApiClient

whole_article = requests.get(url = 'https://newsapi.org/v2/top-headlines?country=gb&apiKey=e1d14d936ae24aa5b9a99e8ab7bed6e9')

whole_article_json = whole_article.json()

headline = whole_article_json["articles"][0]["title"]