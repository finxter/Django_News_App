from django.shortcuts import render
import requests

from decouple import config


API_KEY = config('NEWS_API_KEY')

COUNTRY = 'us'

def news_lists(request):
    if request.method == 'POST':
        url = f'https://newsapi.org/v2/top-headlines?country={COUNTRY}&apiKey={API_KEY}'
        res = requests.get(url).json()
        news_articles = res['articles']
        context = {
            'news_articles': news_articles
        }
        return render(request, 'home.html', context)
    return render(request, 'home.html')
