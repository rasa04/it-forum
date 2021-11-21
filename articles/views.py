from django.shortcuts import render

def index(request):
    return render(request, 'articles/article_1.html')

def about_us(request):
    return render(request, 'articles/about_us.html')
def horoscope(request):
    return render(request, 'articles/horoscope.html')
