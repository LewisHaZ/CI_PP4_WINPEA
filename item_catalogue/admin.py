# 3rd Party Imports
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
# Internal
from .models import ProductItem


@admin.register(ProductItem)
class ProductItemAdmin(SummernoteModelAdmin):
    """
    A class for controlling the fields
    of the products in the catalogue
    from admin panel
    """

    list_display = ('item_name', 'item_type', 'price', 'available')
    search_fields = ('item_name', 'description')
    list_filter = ('available', 'item_type')
    summernote_fields = ('description')
