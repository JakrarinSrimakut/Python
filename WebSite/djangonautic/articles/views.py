from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles}) # display html and with param 'articles'

def article_detail(request, slug): #slug pass from url name capture group ?P<slug>
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug) # query for Article with the same input slug
    return render(request, 'articles/article_detail.html', {'article':article}) # 