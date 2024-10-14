from rest_framework import serializers
from articles.models import Article

class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']