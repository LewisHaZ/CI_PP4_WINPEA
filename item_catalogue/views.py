# Imports
# 3rd Party
from django.shortcuts import render
from django.views import generic
# Internal
from .models import ProductItem


def item_menu(request):
    return render(request, 'catalogue.html')


class ProductList(generic.ListView):
    """
    This is the view for all the products available
    in the catalogue
    """
    model = ProductItem
    queryset = ProductItem.objects.filter(available=1).order_by('-item_type')
    template_name = 'catalogue.html'
