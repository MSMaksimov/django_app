from django.urls import path

from .views import (
    ArticlesListVew,
    ArticlesDetailView,
)

app_name = "blogapp"

urlpatterns = [
    path("articles/", ArticlesListVew.as_view(), name='articles'),
    path("articles/<int:pk>/", ArticlesDetailView.as_view(), name='article'),
]
