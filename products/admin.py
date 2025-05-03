from django.contrib import admin
from .models import ProductCategory,Product,Basket

# admin.site.register(Product)
admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''   Крсивый вывод в админке  '''
    list_display = ('name','price','quantity','category')
    fields = ('image','name','description',('price','quantity'),'category')
    readonly_fields = ('description',)
    search_fields = ('name',)
    ordering = ('name',)

