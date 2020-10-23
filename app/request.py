import urllib.request
import json
from .models import News

api_key = None
# Getting the movie base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_BASE_URL']



def get_news(source):
    '''
    Function that gets the json responce to our url request
    '''
    get_news_url = base_url.format(source,api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)

    return news_results

def process_results(news_results_list):
    news_results = []
    for news_item in news_results_list:
        name=news_item.get("id")
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
       

        if name:
            news_obj = News(id,name, description, url)
            news_results.append(news_obj)

    return news_results

