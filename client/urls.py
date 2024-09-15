from django.urls import path
from .views import create_client, list_client

app_name = 'client'

urlpatterns = [
    path('create/', create_client, name='create_client'),
    path('list/', list_client, name='list_client'),
]
