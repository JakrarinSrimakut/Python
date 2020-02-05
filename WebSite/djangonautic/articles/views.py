from django.shortcuts import render, redirect
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required #decorators extends functions
from .import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles}) # display html and with param 'articles'

def article_detail(request, slug): #slug pass from url name capture group ?P<slug>
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug) # query for Article with the same input slug
    return render(request, 'articles/article_detail.html', {'article':article}) 

#Ensure login to access article_create redirect to login page if not
@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES) # request.POST data is validating to CreateArticle Model Form like user creation form
                                                                # request.FILES contain the actual data content
        if form.is_valid():
            # save article to db
            instance = form.save(commit=False) # commit holds off saving for the moment
            instance.author = request.user # save logged in user to record 
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})