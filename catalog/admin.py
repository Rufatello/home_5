from django.contrib import admin
from catalog.models import Product, Categoties, Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'price', 'categories', 'descripsions')
    list_filter = ('categories',)
    search_fields = ('name', 'descripsions',)


@admin.register(Categoties)
class CategotiesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'image')


@admin.register(Blog)
class BlockAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'body', 'slug')
    list_filter = ('on_published',)
    readonly_fields = ('count_view',)
    prepopulated_fields = {'slug': ('title',)}
