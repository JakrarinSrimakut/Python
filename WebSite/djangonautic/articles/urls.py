from django.conf.urls import url
from . import views

app_name = 'articles' # namespace so html that calls list or detail know it's articles:list or articles:detail

#runs a url by top to bottom scheme
urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'^create/$', views.article_create, name="create"),
    url(r'(?P<slug>[\w-]+)', views.article_detail, name="detail"), #(?P<slug>) name capture group; [\w-]+ means any a-Z,0-9,_, - hyphen included, + any length;  
]