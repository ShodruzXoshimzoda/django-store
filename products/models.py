from django.db import models
from users.models import User   # Импортируем пользвателья из приложения users
class ProductCategory(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=7,decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)  # Количество товаров на складе
    image = models.ImageField(upload_to='products_image/')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f' Продукт: {self.name} | {self.category.name}'

class BasketQuerySet(models.QuerySet):
    '''  Менеджер объектов который посчитывает количество товаров и их общую сумму - objects'''

    def total_quantity(self):
        return sum(basket.quantity for basket in self)

    def total_sum(self):
        return sum(basket.sum() for basket in self)


class Basket(models.Model):
    '''  Класс корзины   '''

    user = models.ForeignKey(to=User, on_delete=models.CASCADE)         # Привязываем пользователья к корзине
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE)   # Привязываем продукты к корзине
    quantity = models.PositiveSmallIntegerField(default=0)              # Количество товаров
    created_timestamp = models.DateTimeField(auto_now_add=True)         # Время добавление

    objects = BasketQuerySet.as_manager()               # Используем созданный нами класс как менеджер
    def __str__(self):
        return f'Корзина для {self.user.username} Продукт: {self.product.name}'

    def sum(self):
        ''' Эта функция возвращет суму  товаров одного типа  '''
        return  self.product.price * self.quantity
