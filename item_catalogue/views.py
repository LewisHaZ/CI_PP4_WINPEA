# Imports
# 3rd Party
from django.shortcuts import render
from django.views import generic
# Internal
from .models import ProductItem


class ProductList(generic.ListView):
    """
    This is the view for all the products available
    in the catalogue
    """
    model = ProductItem
    queryset = ProductItem.objects.filter(available=1).order_by('-item_name')
    template_name = 'catalogue.html'



