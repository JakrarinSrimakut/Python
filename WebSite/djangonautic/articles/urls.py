from django.conf.urls import url
from . import views

app_name = 'articles' # namespace so html that calls list or detail know it's articles:list or articles:detail

urlpatterns = [
    url(r'^$', views.article_list, name="list"),
    url(r'(?P<slug>[\w-]+)', views.article_detail, name="detail"), #(?P<slug>) name capture group; [\w-]+ means any a-Z,0-9,_, - hyphen included, + any length;  
]