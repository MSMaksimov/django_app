from django.contrib.auth.models import User
from django.db import models
# from myauth.models import Profile


class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, null=False, blank=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    content = models.TextField(null=False, blank=True)
    pub_dat = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name="tags")

    def __str__(self):
        return self.title

