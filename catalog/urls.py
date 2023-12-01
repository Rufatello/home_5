from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.CategotiesListView.as_view(), name='catalog'),
    path('contact/', views.contact, name='contact'),
    path('product/<int:category_id>', views.product, name='product'),
    path('add_categories/', views.add_categoriesCreateView.as_view(), name='add_categories'),
    path('views_product/<int:pk>', views.ProductDeleteView.as_view(), name='views_product'),
    path('block/', views.BlogListView.as_view(), name='block_list'),
    path('block_create/', views.BlogCreateView.as_view(), name='block_create'),
    path('block_detail/<int:pk>', views.BlogDetailView.as_view(), name='block_detail'),
    path('block_update/<int:pk>', views.BlogUpdateView.as_view(), name='block_update'),

]
