from django.contrib import admin
from catalog.models import Product, Categoties, Block

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'categories', 'descripsions')
    list_filter = ('categories', )
    search_fields = ('name', 'descripsions', )

@admin.register(Categoties)
class CategotiesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','image')


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title','body','slug')