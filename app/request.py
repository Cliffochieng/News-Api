from app import app
import urllib.request
import json
from .models import News

News = news.News

#getting the Api key
api_key = app.config['NEWS_API_KEY']


def get_news(source):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = api_key

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_movies_response['results']:
            news_results_list = get_news_response['results']
            news_results = process_results(news_results_list)

    return news_results

