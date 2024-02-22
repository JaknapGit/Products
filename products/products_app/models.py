from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.CharField(max_length=30)
    price = models.IntegerField()