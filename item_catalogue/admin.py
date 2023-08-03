from django.contrib import admin
from .models import ProductItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ProductItem)
class ProductItemAdmin(SummernoteModelAdmin):

    list_display = ('item_name', 'item_type', 'price', 'available')
    search_fields = ('item_name', 'description')
    list_filter = ('available', 'item_type')
    summernote_fields = ('description')
