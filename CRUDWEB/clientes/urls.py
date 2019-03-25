from django.urls import path
from .views import list_cliente, create_cliente, update_cliente, delete_cliente

urlpatterns = [
    path('', list_cliente, name='list_cliente'),
    path('new', create_cliente, name='create_cliente'),
    path('update/<int:id>/', update_cliente, name='update_cliente'),
    path('delete/<int:id>/', delete_cliente, name='delete_cliente'),
]
