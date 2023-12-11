from django.contrib import admin
from catalog.models import Product, Categoties, Blog, Contact, Versions


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


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','phone','message')

@admin.register(Versions)
class VersionsAdmin(admin.ModelAdmin):
    list_display = ('is_active',)