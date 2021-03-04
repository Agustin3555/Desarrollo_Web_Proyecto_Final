from django.conf.urls import url
from . import views as login_views


urlpatterns = [
    url(r'^entrar/', login_views.entrar,name="entrar"),
]
