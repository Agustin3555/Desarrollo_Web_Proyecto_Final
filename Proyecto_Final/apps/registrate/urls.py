from django.conf.urls import url
from . import views as registrate_views


urlpatterns = [
    url(r'^registrate/', registrate_views.registro),
]
