# Imports
# 3rd Party
from django.urls import path

# Internal
from . import views

urlpatterns = [
    path('catalogue', views.all_products.as_view(), name='item_menu'),
]
