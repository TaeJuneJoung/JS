from django.urls import path
from . import views

app_name = 'apps'

urlpatterns = [
    path('likes', views.likes, name='likes'),
    path('like_click', views.like_click, name='like_click'),
]