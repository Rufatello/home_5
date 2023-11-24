from django.contrib import admin
from catalog.models import Product, Categoties

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'categories', 'descripsions')
    list_filter = ('categories', )
    search_fields = ('name', 'descripsions', )

@admin.register(Categoties)
class CategotiesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','image')


