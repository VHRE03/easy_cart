from django.db import models
from category.models import Category

class Product(models.Model):
    name = models.CharField(max_length=100, null=None, blank=False)
    description = models.CharField(max_length=200, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, default=0)
    