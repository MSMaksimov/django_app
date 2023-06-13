from django.views.generic import ListView, CreateView, DetailView
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
    success_url = '/articles/create/success/'

    def form_valid(self, form):
        author_name = form.cleaned_data['author']
        author, created = Author.objects.get_or_create(name=author_name)
        form.instance.author = author
        return super().form_valid(form)