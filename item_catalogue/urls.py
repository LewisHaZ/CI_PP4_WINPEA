# Imports
# 3rd Party
from django.urls import path

# Internal
from . import views

urlpatterns = [
    path('item_menu/', views.ProductList.as_view(), name='item_menu'),
]