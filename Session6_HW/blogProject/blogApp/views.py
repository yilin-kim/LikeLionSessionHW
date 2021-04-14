from django.shortcuts import render, redirect
from .models import Article
import time
# Create your views here.


def index(request):
    movie_num = Article.objects.filter(category='movie').count()
    drama_num = Article.objects.filter(category='drama').count()
    programming_num = Article.objects.filter(category='programming').count()
    return render(request, 'index.html', {'movie_num': movie_num, 'drama_num': drama_num, 'programming_num': programming_num})


def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    return render(request, 'detail.html', {'article': article})


def new(request):
    if request.method == 'POST':
        # POST 요청일 경우
        print(request)  # data확인
        new_article = Article.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            time=time.ctime(time.time()),
            category=request.POST['category'],
        )
        return redirect('detail', article_pk=new_article.pk)

    # POST 요청이 아닐 경우
    return render(request, 'new.html')


def movie(request):
    article_movie = Article.objects.filter(category='movie')
    return render(request, 'movie.html', {'articles': article_movie})


def drama(request):
    article_drama = Article.objects.filter(category='drama')
    return render(request, 'drama.html', {'articles': article_drama})


def programming(request):
    article_programming = Article.objects.filter(category='programming')
    return render(request, 'programming.html', {'articles': article_programming})
