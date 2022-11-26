from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=25)
    content = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)