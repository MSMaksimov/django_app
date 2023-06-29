from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Article


class ArticlesListVew(ListView):
    queryset = (
        Article.objects
        .filter(published_at__isnull=False)
        .order_by("-published_at")
    )


class ArticlesDetailView(DetailView):
    model = Article