"""djangonautic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

# flow of request
# url.py->view.py->.html
# model provide class with methods

from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static # allows django to serve media files
from django.conf import settings
from articles import views as article_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'articles/',include('articles.urls')),
    url(r'^about/$', views.about),
    url(r'^$',article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns() #check if we're in debug mode then serve static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #Serve media url and path to folder
