from django.urls import path

from .views import (
    ArticleListView,
    ArticleCreateView,
    AuthorCreateView,
    TagCreateView,
    CategoryCreateView,
)

app_name = "blogapp"

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('article_create/', ArticleCreateView.as_view(), name='create'),
    path('author_create/', AuthorCreateView.as_view(), name='author_create'),
    path('tag_create/', TagCreateView.as_view(), name='tag_create'),
    path('category_create/', CategoryCreateView.as_view(), name='category_create'),

]


