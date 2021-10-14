import requests
from django.shortcuts import render
from integrate.models import News
from django.http import HttpResponse

def home(request):
    all_news = {}

    response = requests.get(f'https://saurav.tech/NewsAPI/top-headlines/category/sports/in.json')
    data = response.json()
    news = data['articles']

    for i in news:
        news_data = News(
            source=i['source'],
            author=i['author'],
            title=i['title'],
            description=i['description'],
            url=i['url'],
            image=i['urlToImage'],
            datetime=i['publishedAt'],
            content=i['content'],
            category= 'sports'
        )
        news_data.save()
        all_news = News.objects.all().order_by('-datetime')

    return HttpResponse({'success': 'data saved'}, status=200)