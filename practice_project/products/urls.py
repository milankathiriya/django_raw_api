from .views import addProduct, fetchProduct, index
from django.urls import path

urlpatterns = [
    path('', index, name='home'),
    path('add_product/', addProduct, name='add_product'),
    path('<int:id>', fetchProduct, name='fetch_product'),
]
