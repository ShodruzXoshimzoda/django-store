from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)  # Количество товаров на складе
    image = models.ImageField(upload_to='products_image/')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)



