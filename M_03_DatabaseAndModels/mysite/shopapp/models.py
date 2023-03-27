# from timeit import

from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=False, blank=True)
    # weight = models.DecimalField(max_digits=6, decimal_places=2)
    # code_num = models.PositiveSmallIntegerField()
