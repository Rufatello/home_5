from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('catalog/', views.catalog, name='catalog'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:category_id>/', views.product, name='product'),
    path('add_categories/', views.add_categories, name='add_categories')

]
