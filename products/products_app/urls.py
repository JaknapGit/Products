from django.urls import path
from .views import *

urlpatterns = [
    path('product_view/', ProductView.as_view(), name='product_view')
]