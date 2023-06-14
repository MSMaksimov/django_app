from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from blogapp.models import Article, Author
from django.contrib.auth.mixins import LoginRequiredMixin


class ArticleListView(ListView):
    model = Article
    template_name = 'blogapp/article_list.html'
    context_object_name = 'articles'
    queryset = Article.objects.select_related('author', 'category').prefetch_related('tags').defer('content')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'blogapp/article_create.html'
    fields = ['title', 'content', 'author', 'category', 'tags']
    success_url = reverse_lazy("blogapp:articles")

    def form_valid(self, form):
        author_name = form.cleaned_data['author']
        author, created = Author.objects.get_or_create(name=author_name)
        form.instance.author = author
        return super().form_valid(form)


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'blogapp/author_create.html'
    fields = ['name', 'bio']
    success_url = reverse_lazy("blogapp:articles")

