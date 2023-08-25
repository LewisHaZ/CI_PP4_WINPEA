# 3rd Party Imports
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """
    A class for setting up
    the blog app and its models
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
