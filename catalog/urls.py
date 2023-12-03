from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.HomeCreateView.as_view(), name='home'),
    path('catalog/', views.CategotiesListView.as_view(), name='catalog'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('product/<int:category_id>/details/', views.ProductListView.as_view(), name='product'),
    path('add_categories/', views.AddCategoriesCreateView.as_view(), name='add_categories'),
    path('views_product/<int:pk>/details/', views.ProductDetailView.as_view(), name='views_product'),
    path('block/', views.BlogListView.as_view(), name='block_list'),
    path('block_create/', views.BlogCreateView.as_view(), name='block_create'),
    path('block_detail/<int:pk>/details/', views.BlogDetailView.as_view(), name='block_detail'),
    path('block_update/<int:pk>/update/', views.BlogUpdateView.as_view(), name='block_update'),

]
