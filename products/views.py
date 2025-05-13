from django.shortcuts import render,HttpResponseRedirect
from .models import ProductCategory, Product, Basket
from django.contrib.auth.decorators import login_required # Декортор доступа
from django.core.paginator import  Paginator
from django.views.generic.base import TemplateView   # TemplateView отвечает за базовый шаблон
from django.views.generic.list import ListView       # ListView для страницы продуктов 
from common.views import TitleMixin

'''             Функциональное представление          '''

# def index(request):
#     context = {'title':'Store',}
#     return render(request,'products/index.html',context)


# def products(request,category_id=None,page_number=1): # Берём id продукта(она может и не передаваться)
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     per_page = 3
#     paginator = Paginator(products,per_page)
#     products_paginator = paginator.page(page_number)

#     context = {
#         'title':'Store - Каталог',
#         'products':products_paginator,
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request,'products/products.html',context)



'''     Классовое представление - CBV'''

class IndexView(TitleMixin,TemplateView):
    '''  Класовое представление для index   '''
    template_name = 'products/index.html'   # Данный метод рендерид страницу
    title = 'Store'                        # Добавил title из миксина


    # def get_context_data(self, **kwargs):   # Метод для добавление контекста
    #     context =  super(IndexView,self).get_context_data()
    #     context['title'] = 'Store'          # задаём titlе в контекст
    #     return context
    #

class ProductListView(TitleMixin,ListView):
    '''Класове представление для Products'''
    model = Product     # Указываем что работаем  моделья Product
    template_name = 'products/products.html'
    paginate_by = 3
    title =  'Каталог - Store'


    def get_queryset(self):
        queryset = super(ProductListView,self).get_queryset()
        category_id = self.kwargs.get('category_id')          # Получаем id категорий 

        return queryset.filter(category_id=category_id) if category_id else queryset  # Фильтруем queryset

    def get_context_data(self, **kwargs):
        context =  super(ProductListView,self).get_context_data()
        # context['title'] = 'Каталог Store'
        context['categories'] = ProductCategory.objects.all()
        return context
    



# Обработчики событий

@login_required           # Если ползователь не авторизован то перенаправим его в станичку login
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

@login_required
def basket_remove(request,basket_id):
    """   Контролер для удаление корзины """
    basket = Basket.objects.get(id=basket_id)
    basket.delete()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])








