from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=None, blank=False)