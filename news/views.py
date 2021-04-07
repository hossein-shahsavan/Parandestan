from .models import News
from .serializers import NewsSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny


class NewsList(generics.ListAPIView):
    queryset = News.objects.filter(show=True)
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)


class NewsDetail(generics.RetrieveAPIView):
    queryset = News.objects.filter(show=True)
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)
    lookup_field = 'slug'


class NewestNews(generics.ListAPIView):
    queryset = News.objects.filter(show=True).order_by('-created')[:4]
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)



