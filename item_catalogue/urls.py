# Imports
# 3rd Party
from django.urls import path

# Internal
from item_catalogue import views

urlpatterns = [
    path('catalogue/', views.catalogue_menu, name='catalogue_menu'),
]
