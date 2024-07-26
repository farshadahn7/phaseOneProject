from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewsSerializer


# class Home(TemplateView):
#     template_name = 'home.html'
# @api_view()
# def home(request):
#     news_data = News.objects.prefetch_related('category').all()
#     news_json_data = NewsSerializer(news_data, many=True)
#     return Response(news_json_data.data)


class NewsListAPIView(APIView):
    def get(self, request):
        news_data = News.objects.prefetch_related('category').all()
        news_json_data = NewsSerializer(news_data, many=True)
        return Response(news_json_data.data)
