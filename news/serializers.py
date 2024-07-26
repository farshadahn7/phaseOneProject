from rest_framework import serializers
from news.models import News, Category


# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('name',)


class NewsSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'content', 'source')
