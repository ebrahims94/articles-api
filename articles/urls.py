from django.urls import path
from articles.views import ArticleListCreateView, ArticleDetailView

urlpatterns = [
    path('articles', ArticleListCreateView.as_view(), name='article-list'),
    path('articles/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
]