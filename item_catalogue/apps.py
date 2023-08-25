# 3rd Party Imports
from django.apps import AppConfig


class ItemCatalogueConfig(AppConfig):
    """
    A class to load
    the item catalogue app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'item_catalogue'
