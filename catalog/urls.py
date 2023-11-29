from django.urls import path
from . import views
from catalog.apps import CatalogConfig
app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.CategotiesListView.as_view(), name='catalog'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:category_id>', views.product, name='product'),
    path('add_categories/', views.add_categories, name='add_categories'),
    path('views_product/<int:pk>', views.ProductDeleteView.as_view(), name='views_product'),

]
