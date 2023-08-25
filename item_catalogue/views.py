# 3rd Party Imports
from django.shortcuts import render
from django.views import generic
# Internal
from .models import ProductItem


def catalogue_menu(request):
    product_list = ProductItem.objects.all()
    return render(
        request, 'item_catalogue/catalogue.html', {
            'product_list': product_list})