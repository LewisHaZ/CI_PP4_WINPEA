from django.contrib import admin
from .models import ProductItem
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ProductItem)
class ProductItemAdmin(SummernoteModelAdmin):

    summernote_fields = ('content')
