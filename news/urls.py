from django.urls import path
from news import views

urlpatterns = [
    path('', views.NewsListAPIView.as_view(), name='home'),
]
