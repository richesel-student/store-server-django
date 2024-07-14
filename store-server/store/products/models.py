from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    discription = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=256)
    discription = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)


# Create your models here.
