from django.urls import path, re_path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.NewsList.as_view(), name='news_list'),
    path('new_news/', views.NewestNews.as_view(), name='new_news'),
    re_path(r'(?P<slug>[-\w]+)/', views.NewsDetail.as_view(), name='news_detail'),
]

