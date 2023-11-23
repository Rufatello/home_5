from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('contact', views.catalog, name='contact'),
    path('catalog', views.contact, name='catalog'),

]