from django.contrib import admin

from .models import Product


@admin.register(Product)  # registro por decorator
class ProductAdmin (admin.ModelAdmin):
    list_display = ('name', 'price', 'storage', 'slug',
                    'created', 'modify', 'active')
