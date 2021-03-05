from django.urls import path
from django.conf.urls import url

from apps.home import views as home_views

from apps.registrate.views import registro


urlpatterns = [
    url(r'^$',home_views.index, name='index'),
]
