from django.urls import path
from . import views as login_views


urlpatterns = [
    path('entrar/', login_views.entrar, name='entrar'),
]
