from django.shortcuts import render
from rest_framework import generics, permissions
from articles.models import Article
from articles.serializers import ArticleSerializer


class ArticleListCreateView(generics.ListCreateAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Article.objects.filter(user=self.request.user)
        status = self.request.query_params.get('status')
        created_at = self.request.query_params.get('created_at')
        if status:
            queryset = queryset.filter(status=status)
        if created_at:
            queryset = queryset.filter(created_at=created_at)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ArticleDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.filter(user=self.request.user)

