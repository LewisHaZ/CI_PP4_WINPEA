# Imports
# 3rd Party
from django.shortcuts import render
from django.views import generic
# Internal
from .models import ProductItem


def catalogueMenu(request):
    product_list = ProductItem.objects.all()
    return render(
        request,
        'item_catalogue/catalogue.html', {'product_list': product_list})


class ProductList(generic.ListView):
    """
    This is the view for all the products available
    in the catalogue
    """
    model = ProductItem
    template_name = 'catalogue.html'
    context_object_name = "product_item"

    def get_queryset(self):
        queryset = {
            'product_bags': ProductItem.objects.all().filter(
                available=True, product_type=0
            ),
            'product_necklaces': ProductItem.objects.all().filter(
                available=True, product_type=1
            ),
            'product_rings': ProductItem.objects.all().filter(
                available=True, product_type=2
            )
        }
        return queryset
