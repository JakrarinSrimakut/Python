from django.conf.urls import url
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name="signup"), # instead of hardcode use signup name
    url(r'^login/$', views.login_view, name="login"),   # in html action="{% url 'accounts:login' %}" call this login under account namesspace
    url(r'^logout/$', views.logout_view, name="logout"),
]