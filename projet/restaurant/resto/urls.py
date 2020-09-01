from django.urls import path
from . import views


urlpatterns = [
    path('home', views.home, name="home"),
    path('', views.loginUser, name="connect"),
    path('inscription', views.registerUser, name="inscription"),
]
