from django.urls import path
from . import views as registrate_views


urlpatterns = [
    path('registrate/', registrate_views.registro, name='registrate'),
]
