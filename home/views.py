# Imports
# 3rd Party
from django.shortcuts import render
import os

# Internal


def index(request):
    """
    Display home page
    """
    return render(request, 'home/index.html')
