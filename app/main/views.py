from flask import Flask, render_template
from . import main
from ..request import get_news
from ..models import News


app = Flask(__name__)


@main.route('/')
def index():
    business_news= get_news('business')
    entertainment_news = get_news('entertainment')
    health_news  = get_news('health')
    science_news = get_news('science')
    technology_news = get_news('technology')
    
    return render_template('index.html', business = business_news,entertainment = entertainment_news, science=science_news,health=health_news,technology=technology_news)

