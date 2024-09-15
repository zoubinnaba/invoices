from django.urls import path
from .views import create_invoice, list_invoice, generate_invoice_pdf, delete_invoice_item, add_invoice_item, \
    get_products_by_category

app_name = 'invoice'

urlpatterns = [
    path('create/', create_invoice, name='create_invoice'),
    path('list/', list_invoice, name='list_invoice'),
    path('add_item/<int:invoice_id>/', add_invoice_item, name='add_invoice_item'),
    path('item/delete/<int:item_id>/', delete_invoice_item, name='delete_invoice_item'),
    path('get-products/<int:category_id>/', get_products_by_category, name='get_products_by_category'),
    path('generate_pdf/<int:invoice_id>/', generate_invoice_pdf, name='generate_invoice_pdf'),
]
