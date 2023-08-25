# 3rd Party Imports
from django.shortcuts import render
import os


def home(request):
    """
    Display home page
    """
    return render(request, 'home/index.html')
