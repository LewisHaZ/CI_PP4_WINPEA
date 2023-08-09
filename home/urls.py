# Imports
# 3rd Party
from django.urls import path


# Internal
from . import views


urlpatterns = [
    path('', views.index, name='index'),
]