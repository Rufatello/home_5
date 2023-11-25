from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('catalog', views.catalog, name='catalog'),
    path('contact', views.contact, name='contact'),
    path('product', views.product, name='product')

]