from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('connexion', views.loginUser, name="connect"),
    path('inscription', views.registerUser, name="inscription"),
]
