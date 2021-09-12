from django.shortcuts import render
import requests
API_KEY = '0e55381042014509ade53f0065695efc'


# Create your views here.

def home(request):
    url = f'https://newsapi.org/v2/top-headlines?country=in&category=sports&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']


    context = {
        'articles' : articles
    }

    return render(request, 'API/home.html', context)
