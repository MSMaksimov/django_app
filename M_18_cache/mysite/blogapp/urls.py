from django.urls import path

from .views import (
    ArticlesListVew,
    ArticlesDetailView,
    LatestArticlesFeed
)

app_name = "blogapp"

urlpatterns = [
    path("articles/", ArticlesListVew.as_view(), name='articles'),
    path("articles/<int:pk>/", ArticlesDetailView.as_view(), name='article'),
    path("articles/latest/feed/", LatestArticlesFeed(), name='articles-feed'),
]
