"""
Классы для отображения моделий приложения в
административной панели Django
с возможностью создавать экземпляры

"""
from django.contrib import admin
from .models import Article, Author, Category, Tag


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    pass

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
