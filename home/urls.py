# 3rd Party Imports
from django.urls import path
# Internal
from . import views


urlpatterns = [
    path('', views.home, name='home'),
]
