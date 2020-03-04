from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'carbohydrate', 'fat', 'protein')



admin.site.register(Product, ProductAdmin)
