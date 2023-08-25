# 3rd Party Imports
from django.apps import AppConfig


class HomeConfig(AppConfig):
    """
    A class that loads the configs for
    home app
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
