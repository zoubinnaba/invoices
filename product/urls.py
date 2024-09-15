from django.urls import path
from .views import create_product, create_category, list_product

app_name = 'product'

urlpatterns = [
    path('create_category/', create_category, name='create_category'),
    path('create_product/', create_product, name='create_product'),
    path('list_product/', list_product, name='list_product'),
]
