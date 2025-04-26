from django.shortcuts import render,HttpResponseRedirect
from .models import ProductCategory, Product, Basket
from users.models import  User
def index(request):
    context = {'title':'Store',}
    return render(request,'products/index.html',context)
def products(request):
    context = {
        'title':'Store - Каталог',
        'products':Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request,'products/products.html',context)

# Обработчики событий
def basket_add(request,product_id):
    ''' Обработчик для добавление товара в корзину '''

    product = Product.objects.get(id=product_id)                           # берём товар по id
    baskets = Basket.objects.filter(user=request.user, product=product)     # Берм корзину для пользователья и по продукту

    if not baskets.exists():    # Логика добавление в корзину
        # Если корзина пуста
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        # Если корзина не пуста
        basket = baskets.first()    # Берём существующий товар
        basket.quantity += 1        # Увеличываем количество товаров ели такой товар уже есть
        basket.save()               # Сохраняем корзину

    return HttpResponseRedirect(request.META['HTTP_REFERER'])       # Возвращаем пользователья в странице где он и находился


def basket_remove(request,basket_id):
    """   Контролер для удаление корзины """
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])








