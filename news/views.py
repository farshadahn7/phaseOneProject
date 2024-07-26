from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView

from news.models import News
from news.serializers import NewsSerializer


# class Home(TemplateView):
#     template_name = 'home.html'
# @api_view()
# def home(request):
#     news_data = News.objects.prefetch_related('category').all()
#     news_json_data = NewsSerializer(news_data, many=True)
#     return Response(news_json_data.data)


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer

    # queryset = News.objects.prefetch_related('category').all()
    # def get(self, request):
    #     news_data = News.objects.prefetch_related('category').all()
    #     news_json_data = NewsSerializer(news_data, many=True)
    #     return Response(news_json_data.data)
    def get_queryset(self):
        news_data = News.objects.all()
        category_id = self.request.query_params.get('category_id', None)
        if category_id is not None:
            news_data = news_data.filter(category__id=category_id)
        return news_data
